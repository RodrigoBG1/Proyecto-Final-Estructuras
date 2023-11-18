class Node:
    def __init__(self, simbolo = None, frecuencia = 0):
        self.simbolo = simbolo
        self.frecuencia = frecuencia

class Frecuencia:
    def leer_archivo(self, direccion):
        frecuencia_letras = {}
        with open(direccion,'r') as file:
            text = file.read()
        for caracter in text:
            frecuencia_letras[caracter] = frecuencia_letras.get(caracter, 0) + 1

class NodoHuffman:
    def __init__(self, caracter=None, frecuencia=0, izquierda=None, derecha=None):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = izquierda
        self.derecha = derecha
