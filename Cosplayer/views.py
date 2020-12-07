from django.shortcuts import render

# Create your views here.
"""home page view"""
def home(request):
    return render(request, 'home.html', {})
