from django.shortcuts import render
from django.http import HttpResponse
import requests, json

def index(request):
    things = iTunesSearch(request)
    return render(request, 'requester/index.html', {'things':things})

def app(request, lookup):
    app = iTunesLookup(request, lookup)
    return render(request, 'requester/app.html', {'app':app})

def iTunesSearch(request):
    search = 'youtube'
    r = requests.get('https://itunes.apple.com/search?country=us&media=software&entity=iPadSoftware&term=' + search)
    return r.json()

def iTunesLookup(request, lookup):
    r = requests.get('https://itunes.apple.com/lookup?id=' + lookup)
    return r.json()
