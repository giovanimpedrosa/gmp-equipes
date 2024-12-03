from django.shortcuts import render

from core.utils.decimal_utils import str_to_decimal
 

def edicao(request):
    return render(request, 'teste/edicao.html')


# views.py
from django.http import JsonResponse
from django.shortcuts import render

def validate_input(request):
    field_name = request.POST.get("field_name", "")  # Nome do campo
    field_value = request.POST.get(field_name, "")  # Valor do campo correspondente

    if not field_name:
        return JsonResponse(
            {"status": "error", "message": "Nome do campo não especificado."},
            json_dumps_params={'ensure_ascii': False}
        )

    try:
        str_to_decimal(field_value)  # Tenta converter o valor para um número decimal
        return JsonResponse({"status": "success", "message": ""})
    except ValueError:
        return JsonResponse(
            {"status": "error", "message": f"Valor inválido no campo '{field_name}'. Use números e pontos/vírgulas."},
            json_dumps_params={'ensure_ascii': False}
        )


# validacao dos forms
from django.shortcuts import render
from django.http import JsonResponse
from .forms import InputModelForm
from .models import InputModel

def validate_text(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        if len(text) < 3:  # Exemplo de validação (mínimo de 3 caracteres)
            return JsonResponse({"status": "error", "message": "Texto muito curto!"}, status=400)
        return JsonResponse({"status": "success", "message": ""})

def validate_email(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        if "@" not in email:  # Exemplo simples de validação de e-mail
            return JsonResponse({"status": "error", "message": "E-mail inválido!"}, status=400)
        return JsonResponse({"status": "success", "message": ""})

def validate_password(request):
    if request.method == 'POST':
        password = request.POST.get('password', '')
        if len(password) < 6:  # Exemplo de validação de senha (mínimo de 6 caracteres)
            return JsonResponse({"status": "error", "message": "Senha muito curta!"}, status=400)
        return JsonResponse({"status": "success", "message": ""})

def validate_date(request):
    if request.method == 'POST':
        date = request.POST.get('date', '')
        if not date:  # Simples verificação de data
            return JsonResponse({"status": "error", "message": "Data inválida!"}, status=400)
        return JsonResponse({"status": "success", "message": ""})

def validate_number(request):
    if request.method == 'POST':
        number = request.POST.get('number', '')
        try:
            number = float(number)  # Tenta converter para número
        except ValueError:
            return JsonResponse({"status": "error", "message": "Valor inválido! Use números."}, status=400)
        return JsonResponse({"status": "success", "message": ""})

def validate_textarea(request):
    if request.method == 'POST':
        textarea = request.POST.get('textarea', '')
        if len(textarea) < 10:  # Exemplo de validação para o campo textarea
            return JsonResponse({"status": "error", "message": "Descrição muito curta!"})
        return JsonResponse({"status": "success", "message": ""})

def validate_checkbox(request):
    if request.method == 'POST':
        is_active = request.POST.get('is_active', False)
        # Validação simples
        return JsonResponse({"status": "success", "message": ""})

def validate_select(request):
    if request.method == 'POST':
        category = request.POST.get('category', '')
        if not category:  # Validação simples de dropdown
            return JsonResponse({"status": "error", "message": "Selecione uma categoria!"}, status=400)
        return JsonResponse({"status": "success", "message": ""})

def input_form(request):
    form = InputModelForm()  # Cria o formulário vazio
    return render(request, 'teste/number_input.html', {'form': form})
