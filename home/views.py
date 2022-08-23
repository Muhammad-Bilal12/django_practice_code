from django.shortcuts import render,HttpResponse

# Create your views here.
def index(requset):
    return HttpResponse('"This is my first Home page')

def about(requset):
    return HttpResponse('"This is my first About page')

def services(requset):
    return HttpResponse('"This is my first Services page')

def contact(requset):
    return HttpResponse('"This is my first contact page')

def blogs(requset):
    return HttpResponse('"This is my first blogs page')


# congrats run myfirst django projects
