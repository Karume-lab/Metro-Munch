from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "core/index.html")


def home(request):
    return render(request, "core/home.html")


def feedback(request):
    return render(request, "core/feedback.html")
def catering(request):
    return render(request,"core/catering.html")