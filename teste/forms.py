from django import forms
from .models import InputModel, NumberInput

class NumberInputForm(forms.ModelForm):
    class Meta:
        model = NumberInput
        fields = ['value']
        widgets = {
            'value': forms.TextInput(attrs={
                'id': 'number-input',
                'hx-post': '/teste/validate_number/',
                'hx-trigger': 'input',
                'hx-target': '#number-input-error',
                'hx-swap': 'outerHTML',
                'class': 'w-full rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white border border-gray-300 dark:border-gray-600 focus:outline focus:outline-4 focus:outline-indigo-300 dark:focus:outline-indigo-500 focus:border-none focus:ring-0 transition-colors duration-200 px-2 py-2'
            }),
        }


class InputModelForm(forms.ModelForm):
    class Meta:
        model = InputModel
        fields = [
            'text', 'email', 'password', 'date', 
            'number', 'textarea', 'is_active', 'category'
        ]
        widgets = {
            'text': forms.TextInput(attrs={
                'id': 'text-input',
                'hx-post': '/validate_text/',
                'hx-trigger': 'input',
                'hx-target': '#text-input-error',
                'hx-swap': 'outerHTML',
                'class': 'w-full rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white border border-gray-300 dark:border-gray-600 focus:outline focus:outline-4 focus:outline-indigo-300 dark:focus:outline-indigo-500 focus:border-none focus:ring-0 transition-colors duration-200 px-2 py-2',
                'placeholder': 'Digite texto...'
            }),
            'email': forms.EmailInput(attrs={
                'id': 'email-input',
                'hx-post': '/validate_email/',
                'hx-trigger': 'input',
                'hx-target': '#email-input-error',
                'hx-swap': 'outerHTML',
                'class': 'w-full rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white border border-gray-300 dark:border-gray-600 focus:outline focus:outline-4 focus:outline-indigo-300 dark:focus:outline-indigo-500 focus:border-none focus:ring-0 transition-colors duration-200 px-2 py-2',
                'placeholder': 'Digite seu e-mail...'
            }),
            'password': forms.PasswordInput(attrs={
                'id': 'password-input',
                'hx-post': '/validate_password/',
                'hx-trigger': 'input',
                'hx-target': '#password-input-error',
                'hx-swap': 'outerHTML',
                'class': 'w-full rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white border border-gray-300 dark:border-gray-600 focus:outline focus:outline-4 focus:outline-indigo-300 dark:focus:outline-indigo-500 focus:border-none focus:ring-0 transition-colors duration-200 px-2 py-2',
                'placeholder': 'Digite sua senha...'
            }),
            'date': forms.DateInput(attrs={
                'id': 'date-input',
                'hx-post': '/validate_date/',
                'hx-trigger': 'input',
                'hx-target': '#date-input-error',
                'hx-swap': 'outerHTML',
                'class': 'w-full rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white border border-gray-300 dark:border-gray-600 focus:outline focus:outline-4 focus:outline-indigo-300 dark:focus:outline-indigo-500 focus:border-none focus:ring-0 transition-colors duration-200 px-2 py-2',
                'placeholder': 'Selecione uma data...',
                'type': 'date'
            }),
            'number': forms.NumberInput(attrs={
                'id': 'number-input',
                'hx-post': '/teste/validate_number/',
                'hx-trigger': 'input',
                'hx-target': '#number-input-error',
                'hx-swap': 'outerHTML',
                'class': 'w-full rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white border border-gray-300 dark:border-gray-600 focus:outline focus:outline-4 focus:outline-indigo-300 dark:focus:outline-indigo-500 focus:border-none focus:ring-0 transition-colors duration-200 px-2 py-2',
                'placeholder': 'Digite um número...'
            }),
            'textarea': forms.Textarea(attrs={
                'id': 'textarea-input',
                'hx-post': '/teste/validate_textarea/',
                'hx-trigger': 'input',
                'hx-target': '#textarea-input-error',
                'hx-swap': 'outerHTML',
                'class': 'w-full rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white border border-gray-300 dark:border-gray-600 focus:outline focus:outline-4 focus:outline-indigo-300 dark:focus:outline-indigo-500 focus:border-none focus:ring-0 transition-colors duration-200 px-2 py-2',
                'rows': 4,
                'placeholder': 'Digite uma descrição...'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'id': 'checkbox-input',
                'hx-post': '/validate_checkbox/',
                'hx-trigger': 'change',
                'hx-target': '#checkbox-input-error',
                'hx-swap': 'outerHTML',
                'class': 'rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white border border-gray-300 dark:border-gray-600 focus:outline focus:outline-4 focus:outline-indigo-300 dark:focus:outline-indigo-500 focus:border-none focus:ring-0 transition-colors duration-200 px-2 py-2',
            }),
            'category': forms.Select(attrs={
                'id': 'select-input',
                'hx-post': '/validate_select/',
                'hx-trigger': 'change',
                'hx-target': '#select-input-error',
                'hx-swap': 'outerHTML',
                'class': 'w-full rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white border border-gray-300 dark:border-gray-600 focus:outline focus:outline-4 focus:outline-indigo-300 dark:focus:outline-indigo-500 focus:border-none focus:ring-0 transition-colors duration-200 px-2 py-2'
            }),
        }

