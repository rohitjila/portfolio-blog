from django.shortcuts import render

# Create your views here.
from .models import Blog

def home(request):
    blogs=Blog.objects
    return render(request, 'home.html', {'blogs':blogs})
    