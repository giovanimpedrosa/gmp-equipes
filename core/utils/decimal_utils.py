from decimal import Decimal

def str_to_decimal(number_str: str) -> Decimal:
    """
    Converte uma string de apresentação de número decimal (ex.: "132.225.355,00")
    em um número Decimal.
    
    Args:
        number_str (str): A string representando o número com separadores de milhares e decimais.
        
    Returns:
        Decimal: O número convertido em formato Decimal.
    
    Raises:
        ValueError: Se a string não for válida como número decimal.
    """
    if not number_str:
        raise ValueError("A string fornecida está vazia.")

    # Remove separadores de milhares (ex.: '.' ou ',') e converte a vírgula decimal em ponto.
    normalized_str = number_str.replace(".", "").replace(",", ".")
    
    try:
        return Decimal(normalized_str)
    except Exception as e:
        raise ValueError(f"Erro ao converter '{number_str}' para Decimal: {e}")
