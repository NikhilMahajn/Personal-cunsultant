from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as log
from home.models import Message
from home.keywords import healthCareKeyword,scienceKeywords,computerKeywords
import openai
from .config import API_KEY
from google import genai
# password for test user is Harry$$$***000
# Create your views here.

def login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            log(request, user)
            return redirect("home")
            # return render(request, 'index.html')

        else:
            # No backend authenticated the credentials
            
            return redirect("login")
        
    return render(request,"login.html")

def index(request):
    if request.user.is_anonymous:
        return redirect("login")
    else:
        if request.method=="POST":
            print(request.POST)
            name=request.POST['name']
            emailAdress=request.POST['email']
            subject=request.POST['subject']
            message=request.POST['message']
            msg=Message(name=name,eMail=emailAdress,subject=subject,userMessage=message)
            msg.save()
        return render(request,"index.html")



def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        Mobile = request.POST.get('mobile')
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        user = User.objects.create_user(username=Username, password=Password)
        user.first_name = fname
        user.last_name = lname
        user.save()

        return redirect("/")
    else:
        return render(request, "signup.html")
    

def logoutUser(request):
    logout(request)
    return redirect("/login")


def Healthpage(request):
    context = {}
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        client = genai.Client(api_key=API_KEY)
        response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
        )
        context["response"]= response.text

        
    return render(request, 'Healthcare.html',context )

def sciencePage(request):
    context={}
    flag=0
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        client = genai.Client(api_key=API_KEY)
        response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
        )
        context["response"]= response.text

    return render(request, 'science.html',context)

def computerPage(request):
    context={}
    flag=0
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        client = genai.Client(api_key=API_KEY)
        response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
        )
        context["response"]= response.text

    return render(request, 'computer.html',context)

def ImgGenerator(request):
    try:
        if request.method == "POST":
            prompt = request.POST.get("prompt")
            openai.api_key = apikey
            imgRespose = openai.Image.create(
                prompt=prompt,
                n=1,
                size="512x512"
            )
            context={
                "question":prompt,
                "img_url":imgRespose['data'][0]['url']
            }
            return render(request, 'ImageGenerate.html',context)
        else:
            context={
                "error":True
            }
            return render(request, 'ImageGenerate.html',context)
    except Exception as e:
        print(e)
        return render(request,'ImageGenerate.html')