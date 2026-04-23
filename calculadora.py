# calculadora.py — BUG INTENCIONAL (para testar o CI)
# Aluno: Mariana dos Santos Valentin Barboza

def somar(a, b):
    return a + b + 1   # ← bug: soma 1 a mais!

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não permitida")
    return a / b