from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name='home'),
   path('blog/',views.blog,name='blog'),
   path('blog-detail/',views.blog_detail,name='blog_detail'),
   path('shop/',views.shop,name='shop'),
   path('contact/',views.contact,name='contact'),
   path('shopping/',views.shopping,name='shopping'),
   path('faq/',views.faq,name='faq'),
   path('checkout/',views.checkout,name='checkout'),
   path('register/',views.register,name='register'),
    path('login/',views.log_in,name='login')
]
