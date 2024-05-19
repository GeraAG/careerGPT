import os
import fitz
import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from openai import OpenAI
from .forms import UploadForm
from django.core.cache import cache

logger = logging.getLogger(__name__)
client = OpenAI()


def home_view(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            # TODO: Sanitize file
            file = request.FILES["pdf_file"]
            fss = FileSystemStorage()
            filename = fss.save(file.name, file)
            uploaded_file_url = fss.url(filename)

            try_again = False
            if request.POST.get("try_again") == "1":
                try_again = True

            # Check for cached data
            cached_data = cache.get(uploaded_file_url)
            if cached_data is None or try_again:
                # Perform operations on the uploaded PDF using PyMuPDF
                with fitz.open(fss.path(filename)) as doc:
                    text = ""
                    for page in doc:
                        text += page.get_text()
                os.remove(
                    fss.path(filename)
                )  # Remove the uploaded file after processing

                # You can add your custom logic here to process the extracted text or perform other PDF operations

                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a career coach, that helps workers to get hired at the jobs they seek. You are provided text from CV. Give advice on how to improve it.",
                        },
                        {"role": "user", "content": text},
                    ],
                )
                data = completion.choices[0].message.content

                logger.debug(data)

                cache_timeout = 60 * 60 * 24 * 60  # Cache for 1 hour (adjust as needed)
                cache.set(uploaded_file_url, data, cache_timeout)
                logger.debug("API is requested. Money is spent!")
            else:
                data = cached_data
                logger.debug(data)
                os.remove(
                    fss.path(filename)
                )  # Remove the uploaded file after processing

            response_data = {"message": data, "file_url": uploaded_file_url}
            return JsonResponse(response_data)
        else:
            errors = form.errors
            logger.debug(errors)
            return JsonResponse({"errors": errors}, status=400)
    else:
        form = UploadForm()
    context = {"form": form}
    return render(request, "pages/home.html", context)
