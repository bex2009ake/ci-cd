from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def resp(res):
    return HttpResponse('<h1>Hello, Devops !!!</h1>')


def resp2(res):
    return HttpResponse('<h1>Hello, Python !!!</h1>')

def resp3(res):
    return HttpResponse('<h1>Hello, GitHub Actions !!!</h1>')
