from django.db import models

# Create your models here.
class Container_list(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    comment = models.CharField(max_length=500)