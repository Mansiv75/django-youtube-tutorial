from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# whole logic part is return in the views file.

def home(request):
    return render(request, 'home\index.html')

def success_page(request):
    return HttpResponse("<h1>This is a success page.</h1>")