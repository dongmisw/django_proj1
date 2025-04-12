from django.shortcuts import render

# Create your views here.

def landing(request):
    return render(request,'single_pages/landing.html')

def aboutme(request):
    return render(request, 'single_pages/about_me.html')