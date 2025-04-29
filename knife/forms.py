from django import forms
from .models import Knife

class KnifeForm(forms.ModelForm):
    class Meta:
        model = Knife
        fields = ['name', 'image', 'description', 'category', 'mechanism', 'price', 'available', 'post_office']
