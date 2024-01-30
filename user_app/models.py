from django.db import models

import my_app.models


# Create your models here.
class User(models.Model):
    user_name = models.TextField()
    full_name = models.TextField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=256)
    categories = models.ManyToManyField(my_app.models.Category)

