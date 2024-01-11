from django.shortcuts import render, redirect

# Create your views here.

def homepage_f(request):
    return render(request, 'index.html')