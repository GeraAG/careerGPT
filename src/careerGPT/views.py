import fitz
from sanitize_filename import sanitize
from openai import OpenAI

from .forms import UploadForm

import os
import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.core.cache import cache

logger = logging.getLogger(__name__)
client = OpenAI()


def home_view(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES["pdf_file"]
            fss = FileSystemStorage()
            filename = fss.save(sanitize(file.name), file)
            uploaded_file_url = fss.url(filename)

            try_again = False
            if request.POST.get("try_again") == "1":
                try_again = True

            # Check for cached data
            cached_data = cache.get(uploaded_file_url)

            # If try_again is TRUE ignore cached data and make new API request
            if cached_data is None or try_again:

                # Perform operations on the uploaded PDF using PyMuPDF
                text = get_pdf_text(fss.path(filename))

                # Remove the uploaded file after processing
                os.remove(
                    fss.path(filename)
                )

                # Making operations on the extracted text from PDF
                data = openai_data(text)

                # Setting cache to avoid repeated requests
                cache.set(uploaded_file_url, data)
                logger.debug("API is requested. Money is spent!")
            else:
                data = cached_data
                logger.debug(data)

                # Remove the uploaded file after processing
                os.remove(
                    fss.path(filename)
                )

            # Sending response from openAI to webpage
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


def get_pdf_text(file_path):
    # Extracts text from pdf file
    text = ""
    with fitz.open(file_path) as doc:
        logger.debug("File opened successfully")
        for page in doc:
            text += page.get_text()
    return text


def openai_data(text):
    # function sends data through api and gets response
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
    return data
