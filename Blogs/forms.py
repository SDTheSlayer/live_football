from django import forms

from . import models


class commentform(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = [
            'text',
        ]
