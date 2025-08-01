# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_view(request):
    print("Request received")
    return HttpResponse("We have a special message for you!")
