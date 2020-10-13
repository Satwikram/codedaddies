from django.http import HttpResponseRedirect
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from django.urls import reverse
from requests.compat import quote_plus
from .models import Search

BASE_CRAIGLIST_URL = 'https://bangalore.craigslist.org/search/bbb?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'

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
        post_listings = soup.find_all('li', {'class': 'result-row'})

        final_postings = []

        for post in post_listings:
            post_title = post.find(class_='result-title').text
            post_url = post.find('a').get('href')

            if post.find(class_='result-price'):
                post_price = post.find(class_='result-price').text
            else:
                post_price = 'N/A'

            if post.find(class_='result-image').get('data-ids'):
                post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
                post_image_url = BASE_IMAGE_URL.format(post_image_id)
                print(post_image_url)
            else:
                post_image_url = 'https://craigslist.org/images/peace.jpg'

            final_postings.append((post_title, post_url, post_price, post_image_url))

        context = {
            'search': search,
            'final_postings': final_postings,
        }
        return render(request, 'search.html', context)
    else:
        return render(request, 'base.html')