def apply_cpf_mask(cpf: str) -> str:
    """Aplica máscara a um CPF."""
    cpf = remove_mask(cpf)  # Reutiliza string_utils.remove_mask
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    raise ValueError("CPF deve conter 11 dígitos.")

# Importa de utils.string_utils, para reutilização:
from .string_utils import remove_mask
