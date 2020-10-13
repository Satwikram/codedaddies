from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.
def home(request):
    return render(request, 'base.html')

def search(request):
    return render(request, 'search.html')