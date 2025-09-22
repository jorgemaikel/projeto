def soma(a, b):
    return a + b

def divisao(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b
