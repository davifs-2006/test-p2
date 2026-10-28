from calculadora import *

def test_soma():
    result = soma(3,4)
    assert result == 7

def test_sub():
    result = sub(3,4)
    assert result == -1

def test_mult():
    result = mult(3,4)
    assert result == 12

def test_calculadora():
    result = calculadora(1, 5, 6)
    assert result == 11