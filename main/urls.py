from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('service/', views.service, name='service'),
    path('portfolio', views.portfolio, name='portfolio'),

]
