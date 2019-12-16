from django.db import models

class Registration(models.Model):
    login = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    