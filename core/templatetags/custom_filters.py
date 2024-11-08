from django import template

register = template.Library()

@register.filter
def get_attribute(obj, attr):
    """
    Retorna o valor de um atributo de um objeto
    Uso: {{ object|get_attribute:'attribute_name' }}
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