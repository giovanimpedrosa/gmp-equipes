from django.shortcuts import render

from teste.forms import NumberInputForm

def edicao(request):
    return render(request, 'teste/edicao.html')


# views.py
from django.http import JsonResponse
from django.shortcuts import render

def validate_input(request):
    value1 = request.POST.get("number_field1", "")
    value2 = request.POST.get("number_field2", "")
    try:
        float(value1)  # Tenta converter para um número decimal
        return JsonResponse({"status": "success", "message": ""})
    except ValueError:
        return JsonResponse({"status": "error", "message": "Valor inválido. Use números e pontos/virgulas."}, json_dumps_params={'ensure_ascii': False})

def process_data(request):
    # Lógica de processamento final
    return render(request, "example.html")



def number_input_view(request):
    form = NumberInputForm()
    return render(request, 'teste/number_input.html', {'form': form})

def validate_number(request):
    if request.method == 'POST':
        form = NumberInputForm(request.POST)
        if form.is_valid():
            return JsonResponse({'message': 'Número válido!'}, status=200)
        else:
            return render(request, 'components/input_error.html', {'errors': form.errors})

