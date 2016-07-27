from __future__ import unicode_literals

from django.db import models

class App(models.Model):
    lookup_id = models.IntegerField()
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Request(models.Model):
    email = models.EmailField(max_length=254, blank=True, null=True)
    device_number=models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    apps = models.ManyToManyField(App)

    def __str__(self):
        return self.email & " - " & self.timestamp
