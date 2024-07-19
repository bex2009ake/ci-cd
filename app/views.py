from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def resp(res):
    return HttpResponse('<h1>Hello, CiCd</h1>  <br > <h2>How are you ???</h2> <br > <h3>Do you like Devops ???</h3>')