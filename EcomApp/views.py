from django.shortcuts import render
from django.views.generic import View

def index(request):
    return render(request,'base/index.html')

