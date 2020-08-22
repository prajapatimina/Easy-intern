from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello ,I m student ")

def main(request):
    return render(request,"main.html")
