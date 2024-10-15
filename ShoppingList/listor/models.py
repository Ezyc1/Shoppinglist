from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class List(models.Model):
    list_name = models.CharField(max_length=255)
    list_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.list_name

    def get_absolute_url(self):
        return reverse('lista-sida',kwargs={'pk':self.pk})

class Item(models.Model):
    item_name = models.CharField(max_length=255)
    amount = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    list=models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name
    
    
    def get_absolute_url(self):
        return reverse('lista-sida',kwargs={'pk':self.list.pk})
