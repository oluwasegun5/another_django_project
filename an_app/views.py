from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def greet(request):
    return HttpResponse(f'<input>Hello, how are you?</input>')

