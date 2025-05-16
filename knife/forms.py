from django import forms
from .models import Knife
from .models import Order

class KnifeForm(forms.ModelForm):
    class Meta:
        model = Knife
        fields = ['name', 'image', 'description', 'category', 'mechanism', 'price', 'available', 'post_office']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email', 'quantity', 'card_number']
        widgets = {
            'card_number': forms.PasswordInput(attrs={'placeholder': 'XXXX-XXXX-XXXX-XXXX'}),
        }