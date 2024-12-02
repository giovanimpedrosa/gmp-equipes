from django import forms
from .models import NumberInput

class NumberInputForm(forms.ModelForm):
    class Meta:
        model = NumberInput
        fields = ['value']
        widgets = {
            'value': forms.TextInput(attrs={
                'id': 'number-input',
                'hx-post': '/validate-number/',
                'hx-trigger': 'input',
                'hx-target': '#number-input-error',
                'hx-swap': 'outerHTML',
                'class': 'border-gray-300 focus:ring-blue-500 focus:border-blue-500 block w-full sm:text-sm rounded-md',
                'placeholder': '###,###,##0.00'
            }),
        }
