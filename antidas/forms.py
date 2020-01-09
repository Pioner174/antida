from django import forms
from django.utils.translation import gettext_lazy as _
import short_url
import time
import pysnooper
from django.db.models import F

from .models import TableLink


def create_sort_url():
    time_now = time.time()
    short_link = short_url.encode_url(int(time_now), min_length=8)
    if short_link not in TableLink.objects.values_list(F('short_link'), flat=True):
        return short_link
    else:
        create_sort_url()


class TableLinkForm(forms.Form):
    full_link = forms.URLField(max_length=500, help_text=_('Enter full link!'))

    full_link.widget.attrs.update({'class': 'form-control'})

    def save(self, **kwargs):
        if 'session_key' in kwargs.keys():
            new_full_link = TableLink.objects.create(
                full_link=self.cleaned_data['full_link'],
                short_link=create_sort_url(),
                session_key=kwargs.get('session_key')
            )
            return new_full_link
        else:
            new_full_link = TableLink.objects.create(
                full_link=self.cleaned_data['full_link'],
                short_link=create_sort_url(),
                user_login=kwargs.get('user_login')
            )
            return new_full_link
