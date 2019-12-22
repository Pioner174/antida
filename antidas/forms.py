from django import forms
from django.utils.translation import gettext_lazy as _
from .models import table_link

class TableLinkForm(forms.Form):
    full_link = forms.URLField(max_length=500, help_text=_('Enter full link!'))
    short_link = forms.URLField()

    full_link.widget.attrs.update({'class': 'form-control'})
    short_link.widget.attrs.update({'class': 'form-control'})

    def save(self):
        new_full_link = table_link.objects.create(
            full_link=self.cleaned_data['full_link'],
            short_link=self.cleaned_data['short_link']
        )
        return new_full_link