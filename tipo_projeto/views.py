from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.db.models import Q
from .models import TipoProjeto

# Create your views here.

class TipoProjetoListView(LoginRequiredMixin, ListView):
    model = TipoProjeto
    template_name = 'tipo_projeto/tipo_projeto_list.html'
    context_object_name = 'tipos_projeto'

class TipoProjetoCreateView(LoginRequiredMixin, CreateView):
    model = TipoProjeto
    template_name = 'tipo_projeto/tipo_projeto_form.html'
    fields = ['descricao']
    success_url = reverse_lazy('tipo_projeto:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Criar'
        return context

class TipoProjetoUpdateView(LoginRequiredMixin, UpdateView):
    model = TipoProjeto
    template_name = 'tipo_projeto/tipo_projeto_form.html'
    fields = ['descricao']
    success_url = reverse_lazy('tipo_projeto:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Atualizar'
        return context

class TipoProjetoDeleteView(LoginRequiredMixin, DeleteView):
    model = TipoProjeto
    success_url = reverse_lazy('tipo_projeto:list')

class TipoProjetoDetailView(LoginRequiredMixin, DetailView):
    model = TipoProjeto
    template_name = 'tipo_projeto/tipo_projeto_detail.html'

def autocomplete(request):
    search = request.GET.get('q', '')
    tipos = TipoProjeto.objects.all()  # Retorna todos quando clica no botão
    
    if search:  # Filtra apenas se houver termo de busca
        tipos = tipos.filter(Q(descricao__icontains=search))
    
    tipos = tipos.order_by('descricao')[:10]
    
    return render(request, 'tipo_projeto/autocomplete.html', {
        'tipos': tipos,
        'search': search
    })

def select_tipo_projeto(request, pk):
    if pk == 0:  # Caso especial para limpar a seleção
        return render(request, 'tipo_projeto/selected.html', {
            'tipo': None
        })
    
    tipo = get_object_or_404(TipoProjeto, pk=pk)
    return render(request, 'tipo_projeto/selected.html', {
        'tipo': tipo
    })
