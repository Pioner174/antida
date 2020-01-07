from django.db import models
from django.utils.translation import gettext_lazy as _


class TableLink(models.Model):
    full_link = models.URLField(max_length=500, help_text=_('Enter full link!'))
    short_link = models.URLField(help_text=_('Enter Short link!'), unique = True)
    date_create = models.DateTimeField(auto_now_add=True)
    number_of_clicks = models.IntegerField(help_text=_('Number of clicks on the link'),default=0)
    # id_registration = models.ForeignKey( , on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=100,unique = False)
    user_login = models.CharField(max_length=100,unique = False, null=True)

    def __str__(self):
        return self.short_link
    
    

    
    

    

    
