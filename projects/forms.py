from django import forms
from .models import Project
from ckeditor.widgets import CKEditorWidget
from tipo_projeto.models import TipoProjeto

class ProjectForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite um Título'}))
    detailed_description = forms.CharField(widget=CKEditorWidget(), required=False, label='Descrição detalhada')
    value = forms.DecimalField(
        widget=forms.NumberInput(attrs={
#            'step': '0.01',
#            'min': '0',

            'class': 'mt-1 block w-full rounded-md p-2.5 border border-gray-300 dark:border-gray-600 bg-gray-50 dark:bg-gray-700 focus:border-2 focus:border-indigo-500 dark:focus:border-indigo-500 focus:outline-none dark:text-white sm:text-sm'
        }),
        decimal_places=2,
        max_digits=10,
        required=True,
        localize=True
    )
    
    tipo_projeto = forms.ModelChoiceField(
        queryset=TipoProjeto.objects.all(),
        widget=forms.Select(attrs={
            'class': 'select2-autocomplete',
            'data-placeholder': 'Selecione um tipo de projeto'
        }),
        required=False
    )
    
    class Meta:
        model = Project
        fields = ['title', 'description', 'detailed_description', 'value', 'photo', 'tipo_projeto']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.initial['value'] = '{:.2f}'.format(self.instance.value)

