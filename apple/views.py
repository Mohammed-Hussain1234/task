from django.shortcuts import render,HttpResponse


def simple(self):
    return HttpResponse('hello hussain')

def about_view(request):
    return render(request,'about.html')

def lak(request):
    return render(request,'contact.html')

def home(request,name):
    return HttpResponse(request,f"home page- welcome {name}")

def hrs(request,number):
    return HttpResponse(f'hrs page-welcome {number**2}')

# Create your views here.
