import os
import fitz
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from dotenv import load_dotenv
from openai import OpenAI
from .forms import UploadForm

load_dotenv()
client = OpenAI()

def home_view(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES['pdf_file']
            ext = os.path.splitext(file.name)[1]
            if ext.lower() not in ('.pdf',):
                form.add_error('pdf_file', 'Only PDF files are allowed.')
                return render(request, 'pages/home.html', {'form': form})
            fss = FileSystemStorage()
            filename = fss.save(file.name, file)
            uploaded_file_url = fss.url(filename)

            # Perform operations on the uploaded PDF using PyMuPDF
            with fitz.open(fss.path(filename)) as doc:
                text = ""
                for page in doc:
                    text += page.get_text()

            # You can add your custom logic here to process the extracted text or perform other PDF operations




            os.remove(fss.path(filename))  # Remove the uploaded file after processing
            response_data = {'message': text, 'file_url': uploaded_file_url}
            return JsonResponse(response_data)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        form = UploadForm()
    context = {'form': form}
    return render(request, 'pages/home.html', context)

    '''completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a HR consultant, that helps workers to get hired at the jobs they seek."},
        {"role": "user", "content": "show me a website design where user uploads pdf of a resume and gets information on how to improve it in order to get hired"}
    ]
    )

    print(completion.choices[0].message)'''
