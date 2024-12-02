from datetime import datetime

def str_to_date(date_str, fmt="%Y-%m-%d"):
    """Converte uma string para um objeto de data."""
    try:
        return datetime.strptime(date_str, fmt)
    except ValueError as e:
        raise ValueError(f"Erro ao converter '{date_str}' para data com formato '{fmt}': {e}")

def date_to_str(date_obj, fmt="%Y-%m-%d"):
    """Converte um objeto de data para uma string."""
    return date_obj.strftime(fmt)
