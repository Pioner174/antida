from django.db import models
from django.utils.translation import gettext_lazy as _

class Registration(models.Model):
    login = models.CharField(max_length=25, help_text=_('Enter login!'),unique = True)
    email = models.EmailField(max_length=100, help_text=_('Enter email!'),unique = True)
    password = models.CharField(max_length=25, help_text=_('Enter password!'), unique = True)
    date_create = models.DateField(auto_now_add=True)
    def __str__(self): 
        return self.login

class table_link(models.Model):
    full_link = models.URLField(max_length=500, help_text=_('Enter full link!'))
    short_link = models.URLField(help_text=_('Enter Short link!'), unique = True)
    number_of_clicks = models.IntegerField(help_text=_('Number of clicks on the link'),default=0)
    id_registration = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True, blank=True)  #Возможно надо поменять on_delete=SET_NULL
    def __str__(self):
        return self.short_link
