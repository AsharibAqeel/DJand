from django.shortcuts import render

def portfolio_view(request):
    return render(request, 'portfolio/index.html')

def home(request):
    return render(request, 'portfolio/home.html')