from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<lookup>[0-9]+)/$', views.app, name="app"),
]
