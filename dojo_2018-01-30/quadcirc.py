from sympy import pi


class Quadrado:

    def __init__(self, x, y, lado):
        self.x = x
        self.y = y
        self.lado = lado

    @property
    def area(self):
        return self.lado ** 2


class Circulo:

    def __init__(self, x, y, raio):
        self.raio = raio

    @property
    def area(self):
        return pi * self.raio ** 2


def interarea(quadrado, circulo):
    if quadrado.x == quadrado.y:
        return min(circulo.area / 4, quadrado.area)
    if quadrado.x == quadrado.y - 5:
        return min(circulo.area / 2, quadrado.area)
    return min(circulo.area, quadrado.area)


def test_zero_dados():
    quadrado = Quadrado(x=0, y=0, lado=0)
    circulo = Circulo(x=0, y=0, raio=0)
    assert interarea(quadrado, circulo) == 0

def test_quadrado_area_1_no_circulo_gigante():
    quadrado = Quadrado(x=0, y=0, lado=1)
    circulo = Circulo(x=0, y=0, raio=10)
    assert interarea(quadrado, circulo) == 1

def test_quadrado_area_4_no_circulo_gigante():
    quadrado = Quadrado(x=0, y=0, lado=2)
    circulo = Circulo(x=0, y=0, raio=10)
    assert interarea(quadrado, circulo) == 4

def test_circulo_raio_1_no_quadrado_gigante():
    quadrado = Quadrado(x=-5, y=5, lado=10)
    circulo = Circulo(x=0, y=0, raio=1)
    assert interarea(quadrado, circulo) == pi

def test_circulo_raio_2_no_quadrado_gigante():
    quadrado = Quadrado(x=-5, y=5, lado=10)
    circulo = Circulo(x=0, y=0, raio=2)
    assert interarea(quadrado, circulo) == pi * 4

def test_quarto_de_area_do_circulo_unitario():
    quadrado = Quadrado(x=0, y=0, lado=10)
    circulo = Circulo(x=0, y=0, raio=1)
    assert interarea(quadrado, circulo) == pi / 4

def test_meia_area_do_circulo_unitario():
    quadrado = Quadrado(x=-5, y=0, lado=10)
    circulo = Circulo(x=0, y=0, raio=1)
    assert interarea(quadrado, circulo) == pi / 2
