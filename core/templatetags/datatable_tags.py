from django import template

register = template.Library()

@register.filter
def getattr_filter(obj, attr):
    """
    Filtro personalizado para obter atributos de objetos
    Uso: {{ object|getattr_filter:'attribute_name' }}
    """
    try:
        # Primeiro tenta acessar como atributo
        result = getattr(obj, attr)
        # Se for callable (método), executa
        if callable(result):
            return result()
        return result
    except (AttributeError, TypeError):
        try:
            # Tenta acessar como dicionário
            return obj[attr]
        except (KeyError, TypeError):
            return ''