from django import forms
from django.utils.translation import gettext_lazy as _
from .models import TableLink

import pysnooper
import short_url
import time


class TableLinkForm(forms.Form):
    full_link = forms.URLField(max_length=500, help_text=_('Enter full link!'))

    full_link.widget.attrs.update({'class': 'form-control'})


    def save_user(self, ssk):
        x = time.time()
        new_full_link = TableLink.objects.create(
            full_link=self.cleaned_data['full_link'],
            short_link=short_url.encode_url(int(x), min_length=8),
            user_login=ssk
        )
        return new_full_link

    def save_session(self, ssk):
        x = time.time()
        new_full_link = TableLink.objects.create(
            full_link=self.cleaned_data['full_link'],
            short_link=short_url.encode_url(int(x), min_length=8),
            session_key=ssk
        )
        return new_full_link
