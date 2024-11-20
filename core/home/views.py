from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# whole logic part is return in the views file.

def home(request):
    return HttpResponse("Hey I am a Django Server.")