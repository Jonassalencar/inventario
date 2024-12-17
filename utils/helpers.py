def validar_valor_positivo(valor):
    if valor < 0:
        raise ValueError("O valor deve ser positivo.")
    return valor
