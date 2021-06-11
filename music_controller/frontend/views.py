from django.shortcuts import render

# Create your views here.

def index(request, *orgs, **kworgs):
    return render(request, 'frontend/index.html')