from django.shortcuts import render, redirect
from . import models



def index(request):
    """index"""
    banners = models.Banner.objects.all()
    abouts = []
    for about in models.About.objects.all():
        about.body = about.body.split(',')
        abouts.append(about)

    services = models.Service.objects.all()
    blogs = models.Blog.objects.all()
    portfolio = models.Portfolio.objects.all()
    workers = models.Workers.objects.all()

    context = {
        'banners': banners,
        'abouts': abouts,
        'services': services,
        'blogs': blogs,
        'portfolio': portfolio,
        'workers': workers
    }

    return render(request, 'index.html', context)


def service(request):
    '''Xizmatlar'''
    services = models.Service.objects.all()
    data = {
        "services": services
    }

    return render(request, 'service.html', context=data)


def about(request):
    """biz haqimizda"""
    abouts = []
    for about in models.About.objects.all():
        about.body = about.body.split(',')
        abouts.append(about)

    workers = models.Workers.objects.all()

    data = {
        'abouts': abouts,
        'workers': workers,
    }
    return render(request, 'about.html', context=data)


def blog(request):
    """bloglar"""
    blogs = models.Blog.objects.all()
    data = {
        "blogs": blogs
    }
    return render(request, 'blog.html', context=data)


def contact(request):
    """foydalanuvchilarning contactlari"""
    if request.method == 'POST':
        try:
            models.Contact.objects.create(
                full_name=request.POST['ful_name'],
                tel=request.POST['tel'],
                email=request.POST['email'],
                message=request.POST['message'],
            )

        except:
            ...
    return render(request, 'contact.html')


def portfolio(request):
    """Loyihalarimiz"""
    portfolio = models.Portfolio.objects.all()
    data = {
        "portfolio": portfolio
    }
    return render(request, 'portfolio.html', context=data)
