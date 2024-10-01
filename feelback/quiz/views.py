from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    context = {" ": " "}
    template = loader.get_template("quiz/index.html")
    return HttpResponse(template.render(context, request))

def dashboard(request):
    context = {" ": " "}
    template = loader.get_template("quiz/dashboard.html")
    return HttpResponse(template.render(context, request))

def feedbackform(request):
    context = {" ": " "}
    template = loader.get_template("quiz/feedbackform.html")
    return HttpResponse(template.render(context, request))
