from django.db import models
from django.urls import reverse

# Create your models here


class Employee(models.Model):
    ename = models.CharField(max_length=64)
    eno = models.IntegerField()
    eaddress = models.CharField(max_length=64)
    esal = models.IntegerField()

    def get_absolute_url(self, *args, **kwargs):
        return reverse('get_data', kwargs={'pk': self.pk})
