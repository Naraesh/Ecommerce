from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html',{'home':'active'})
def blog(request):
    return render(request,'blog/blog.html',{'blog':'active'})
def blog_detail(request):
    return render(request,'blog/blog_detail.html',{'blog':'active'})
def shop(request):
    return render(request,'shop/shop.html',{'shop':'active'})
def contact(request):
    return render(request,'contact/contact.html',{'contact':'active'})
def shopping(request):
    return render(request,'pages/shopping-cart.html',{'shopping':'active'})
def faq(request):
    return render(request,'pages/FAQ.html',{'faq':'active'})
def checkout(request):
    return render(request,'pages/checkout.html',{'checkout':'active'})
def register(request):
    return render(request,'registration/register.html')

def log_in(request):
    return render(request,'registration/login.html')

