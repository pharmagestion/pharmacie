from django.shortcuts import render


def index(request, *args, **kwargs):
    return render(request, 'index.html')


def welcome(request, *args, **kwargs):
    return render(request, 'welcome.html')