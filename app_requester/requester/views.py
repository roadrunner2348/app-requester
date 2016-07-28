from django.shortcuts import render
from django.http import HttpResponse
import requests, json

def index(request):
    if request.method == "POST":
        query = request.POST.get('search')
        results = iTunesSearch(request, query)
        return render(request, 'requester/index.html', {'results':results})
    else:
        return render(request, 'requester/index.html')

def app(request, lookup):
    app = iTunesLookup(request, lookup)
    return render(request, 'requester/app.html', {'app':app})

def iTunesSearch(request, query):
    r = requests.get('https://itunes.apple.com/search?country=us&media=software&entity=iPadSoftware&term=' + query)
    return r.json()

def iTunesLookup(request, lookup):
    r = requests.get('https://itunes.apple.com/lookup?id=' + lookup)
    return r.json()
