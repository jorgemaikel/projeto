# my_functions.py

def soma(a, b):
    """Esta função retorna a soma de dois números."""
    return a + b

def divisao(a, b):
    """
    Esta função retorna a divisão de a por b.
    Levanta uma exceção ValueError se b for zero.
    """
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b
