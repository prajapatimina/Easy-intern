from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello ,I m student ")

def main(request):
    return render(request,"main.html")

def sregister(request):
    return render(request,"student/sreg.html")


def slogin(request):
    return render(request,"student/slogin.html")
