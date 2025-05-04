import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculadora.operaciones import sumar, restar, multiplicar, dividir


def test_sumar():
    assert sumar(2, 3) == 5

def test_restar():
    assert restar(5, 3) == 2

def test_multiplicar():
    assert multiplicar(3, 4) == 12

def test_dividir():
    assert dividir(10, 2) == 5

def test_division_por_cero():
    with pytest.raises(ValueError):
        dividir(5, 0)
