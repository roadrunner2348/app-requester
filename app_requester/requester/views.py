from django.shortcuts import render
from django.http import HttpResponse
from . import models
import requests, json

def index(request):
    if 'cartItems' not in request.session:
        request.session['cartItems'] = []
    cartCount = request.session.get('cartItems')
    if request.method == "POST":
        query = request.POST.get('search')
        results = iTunesSearch(request, query)
        return render(request, 'requester/index.html', {'results':results, 'cartCount':cartCount})
    else:
        return render(request, 'requester/index.html', {'cartCount':cartCount})

def app(request, lookup):
    app = iTunesLookup(request, lookup)
    return render(request, 'requester/app.html', {'app':app})

def iTunesSearch(request, query):
    r = requests.get('https://itunes.apple.com/search?country=us&media=software&entity=iPadSoftware&term=' + query)
    return r.json()

def iTunesLookup(request, lookup):
    r = requests.get('https://itunes.apple.com/lookup?id=' + lookup)
    return r.json()

def addToCart(request, lookup):
    if 'cartItems' in request.session:
        cartList = request.session.get('cartItems')
        cartList.append(lookup)
        request.session['cartItems'] = cartList
    else:
        request.session['cartItems'] = [lookup]
    return HttpResponse('Ok')

def getCartData(request):
    cart = request.session.get('cartItems')
    cartData = []
    for item in cart:
        data = iTunesLookup(request, item)
        cartData.append(data['results'][0])
    return cartData

def getCart(request):
    cartData = getCartData(request)
    return render(request, 'requester/cart.html', { 'cartData':cartData })

def emptyCart(request):
    request.session['cartItems'] = []
    return HttpResponse('OK')

def createRequest(request):
    cart = request.session.get('cartItems')
    cartData = getCartData(request)
    emptyCart(request)
    return HttpResponse(cartData)
