from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def resp(res):
    return HttpResponse('<h1>Hello, Devops</h1>')


