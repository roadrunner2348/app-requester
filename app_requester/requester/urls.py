from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<lookup>[0-9]+)/$', views.app, name="app"),
    url(r'^addtocart/(?P<lookup>[0-9]+)/$', views.addToCart, name="addToCart"),
    url(r'^cart$', views.getCart, name="getCart"),
    url(r'^emptycart$', views.emptyCart, name="emptyCart"),
    url(r'^checkout$', views.createRequest, name="createRequest"),

]
