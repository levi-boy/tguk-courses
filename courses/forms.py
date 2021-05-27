from django import forms

from .models import Record


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['parent_name', 'parent_phone', 'name', 'phone', 'email', 'school', 'address']