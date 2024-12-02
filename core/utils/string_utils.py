def left_pad(value, width, fill_char="0"):
    """Preenche um valor com zeros (ou outro caractere) à esquerda."""
    return str(value).rjust(width, fill_char)

def remove_mask(value):
    """Remove caracteres não numéricos de uma string."""
    return ''.join(filter(str.isdigit, value))
