# tests/test_calculadora.py
# Aluno: Mariana dos Santos Valentin Barboza
# Semana 8 — Integração Contínua | Prof. Caetano Santos | FIEC

from calculadora import somar, subtrair, multiplicar, dividir

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0

def test_subtrair():
    assert subtrair(10, 4) == 6

def test_multiplicar():
    assert multiplicar(3, 4) == 12

def test_dividir():
    assert dividir(10, 2) == 5.0