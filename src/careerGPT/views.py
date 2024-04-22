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

    '''
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
    )

    print(completion.choices[0].message)'''

    return render(request, "pages/home.html", {})
