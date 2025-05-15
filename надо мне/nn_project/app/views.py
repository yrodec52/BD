from django.shortcuts import render, redirect

def main(request):
    template = 'main.html'
    context = {}
    return render(request,template,context)

# Create your views here.
def signup(request):
    template = 'signup.html'
    context = {}
    return render(request,template,context)

def login(request):
    template = 'login.html'
    context = {}
    return render(request,template,context)

def newapp(request):
    template = 'newapp.html'
    context = {}
    return render(request,template,context)
def logout(request):
    return redirect('main')