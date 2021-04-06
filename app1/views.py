from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>welcome to index of app1</h1>")

def sample1(request):
    return render(request,"sample1.html")
    
def sample_view(request):
    return render(request,"sample_app1.html")

