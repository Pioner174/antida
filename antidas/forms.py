from django import forms
from django.utils.translation import gettext_lazy as _
from .models import table_link
from django.contrib.sessions.models import Session

import pysnooper
import short_url
import time

class TableLinkForm(forms.Form):
    full_link = forms.URLField(max_length=500, help_text=_('Enter full link!'))
    

    full_link.widget.attrs.update({'class': 'form-control'})
    
    
    def save(self, path , ssk):
        x = time.time()
        new_full_link = table_link.objects.create(
            full_link = self.cleaned_data['full_link'],
            short_link = path + short_url.encode_url(int(x), min_length = 7),
            session_key = ssk
        )
        return new_full_link