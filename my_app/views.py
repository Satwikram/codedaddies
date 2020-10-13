from django.http import HttpResponseRedirect
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from django.urls import reverse
from requests.compat import quote_plus
from .models import Search

BASE_CRAIGLIST_URL = 'https://bangalore.craigslist.org/search/bbb?query={}'

# Create your views here.
def home(request):
    return render(request, 'base.html')

def search(request):
    if request.method == "POST":
        search = request.POST.get('search')
        final_url = BASE_CRAIGLIST_URL.format(quote_plus(search))
        sobj = Search.objects.create(search = search)
        sobj.save()
        print("Final URL:", final_url)
        response = requests.get(final_url)
        data = response.text
        soup = BeautifulSoup(data, features = 'html.parser')
        post_titles = soup.find_all('a', {'class' : 'result-title'})
        print(post_titles)

        context = {
            'data': data,
        }
        return HttpResponseRedirect(reverse('search'))
    else:
        return render(request, 'base.html')