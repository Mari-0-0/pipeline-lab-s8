# calculadora.py
# Aluno: Mariana dos Santos Valentin Barboza
# Semana 8 — Integração Contínua | Prof. Caetano Santos | FIEC

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não permitida")
    return a / b