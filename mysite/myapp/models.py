from django.db import models

# Create your models here.

class Link(models.Model):
    def __str__(self):
        return self.name
    address_link=models.CharField(max_length=100000,null=True,blank=True)
    name=models.CharField(max_length=100000,null=True,blank=True)
