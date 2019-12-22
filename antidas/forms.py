from django import forms
from django.utils.translation import gettext_lazy as _
from .models import table_link
import short_url
import time

class TableLinkForm(forms.Form):
    full_link = forms.URLField(max_length=500, help_text=_('Enter full link!'))
    

    full_link.widget.attrs.update({'class': 'form-control'})

    def save(self):
        x = time.time()
        new_full_link = table_link.objects.create(
            full_link=self.cleaned_data['full_link'],
            short_link='http://localhost:8000/test/'+short_url.encode_url(int(x), min_length = 7)
        )
        return new_full_link