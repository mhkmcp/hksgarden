from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'pizza/home.html', context)


def order(request):
    context = {}
    return render(request, 'pizza/order.html', context)
