from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def home_view(request):
    if request.method == "POST":
        return render(request, "pages/home.html", {})


    '''completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a HR consultant, that helps workers to get hired at the jobs they seek."},
        {"role": "user", "content": "show me a website design where user uploads pdf of a resume and gets information on how to improve it in order to get hired"}
    ]
    )

    print(completion.choices[0].message)'''

    return render(request, "pages/home.html", {})
