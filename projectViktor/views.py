from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello, world!</h1>")

def Second(request):
    return render(request, 'Second.html')
def Page1(request):
    return render(request, 'Page1.html')
def Page2(request):
    return render(request, 'Page2.html')
def Page3(request):
    return render(request, 'Page3.html')
def Page4(request):
    return render(request, 'Page4.html')
def Page5(request):
    return render(request, 'Page5.html')