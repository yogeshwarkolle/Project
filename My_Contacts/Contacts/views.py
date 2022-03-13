from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Credentials, Data
from .forms import RegistrationForm, ContactForm


def signin(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            dataset = Credentials.objects.get(email=email)
            if dataset.password==password:
                return redirect("phonebook")
            else:
                messages.info(request,"Invalid Credentials")
                return render(request,"signin.html")
        except:
            messages.info(request, "Invalid Credentials")
            return render(request,"signin.html")
    return render(request, 'signin.html')


def signup(request):
    context = {}
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        while True:
            try:
                form.save()
                break
            except:
                messages.info(request,'Email Already Exists')
    context['form'] = form
    return render(request, "signup.html", context)



def phonebook(request):
    context = {}
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "phonebook.html", context)


def display(request):
    obj = Data.objects.all()
    return render(request, 'display.html', {'obj': obj})


