import heapq
import pickle
from bitarray import bitarray
from PIL import Image
import librosa
import numpy as np
import os

class Node:
    def __init__(self, simbolo = None, frecuencia = 0, hijo_izq = None, hijo_der = None):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.hijo_izq = hijo_izq
        self.hijo_der = hijo_der
    
    def __lt__(self, otro): #Esto se usa para que al momento de utilizar la funcion "heapify" compare de acuerdo con la frecuencia
        return self.frecuencia < otro.frecuencia

class Text:
    def obtener_texto(self, direccion):
        with open(direccion,'r') as file:
            text = file.read() 
        return text

    def frecuencia_simbolos(self, direccion):
        frecuencia_letras = {}
        with open(direccion,'r') as file:
            text = file.read()
        for caracter in text:
            frecuencia_letras[caracter] = frecuencia_letras.get(caracter, 0) + 1
        return frecuencia_letras
    
    def codificar_texto(self, texto, diccionario):
        texto_codificado = ''.join(diccionario[caracter] for caracter in texto)
        """print(texto_codificado)"""
        return texto_codificado
    
    def comprimir(self, diccionario, texto, archivo_salida, arbol_huffman, archivo_salida_arbol):
        s = bitarray()
        s.encode({simbolo: bitarray(code) for simbolo, code in diccionario.items()}, texto)
        with open(archivo_salida, 'wb') as file:
            s.tofile(file)
        with open(archivo_salida_arbol, 'wb') as file:
            pickle.dump(arbol_huffman, file)

    def descomprimir(self, archivo_salida, archivo_salida_arbol):
        with open(archivo_salida, 'rb')as file:
            comprimido = bitarray()
            comprimido.fromfile(file)
        with open(archivo_salida_arbol, 'rb') as file:
            arbol = pickle.load(file)
        
        self.decodificar_texto(comprimido, arbol)
    
    def decodificar_texto(self, bits, arbol_huffman):
        texto_recuperado = ""
        nodo_actual = arbol_huffman

        for bit in bits:
            if str(bit) == '0':
                nodo_actual = nodo_actual.hijo_izq
            else:
                nodo_actual = nodo_actual.hijo_der

            if nodo_actual.simbolo is not None:
                texto_recuperado += nodo_actual.simbolo
                nodo_actual = arbol_huffman

        with open("C:/Users/Rodrigo/OneDrive/Documentos/Compresor/descomprimido.txt", 'w') as file:
            file.write(texto_recuperado)

        return texto_recuperado


class Imagen:
    def obtener_imagen(self, direccion):
        with open(direccion,'rb') as file:
            text = file.read() 
        return text

    def frecuencia_simbolos(self, direccion):
        frecuencia_letras = {}
        with open(direccion,'rb') as file:
            text = file.read()
        for caracter in text:
            frecuencia_letras[caracter] = frecuencia_letras.get(caracter, 0) + 1
        return frecuencia_letras
    
    def codificar_texto(self, texto, diccionario):
        texto_codificado = ''.join(diccionario[caracter] for caracter in texto)
        """print(texto_codificado)"""
        return texto_codificado
    
    def comprimir(self, diccionario, texto, archivo_salida, arbol_huffman, archivo_salida_arbol):
        s = bitarray()
        s.encode({simbolo: bitarray(code) for simbolo, code in diccionario.items()}, texto)
        with open(archivo_salida, 'wb') as file:
            s.tofile(file)
        with open(archivo_salida_arbol, 'wb') as file:
            pickle.dump(arbol_huffman, file)

    def descomprimir(self, archivo_salida, archivo_salida_arbol):
        with open(archivo_salida, 'rb')as file:
            comprimido = bitarray()
            comprimido.fromfile(file)
        with open(archivo_salida_arbol, 'rb') as file:
            arbol = pickle.load(file)
        
        self.decodificar_texto(comprimido, arbol)
    
    def decodificar_texto(self, bits, arbol_huffman):
        texto_recuperado = bytearray()
        nodo_actual = arbol_huffman

        for bit in bits:
            if str(bit) == '0':
                nodo_actual = nodo_actual.hijo_izq
            else:
                nodo_actual = nodo_actual.hijo_der

            if nodo_actual.simbolo is not None:
                texto_recuperado.append(nodo_actual.simbolo)  # convert to string before concatenating
                nodo_actual = arbol_huffman

        with open("C:/Users/Rodrigo/OneDrive/Documentos/Compresor/descomprimido.jpg", 'wb') as file:
            file.write(texto_recuperado)

        return texto_recuperado

class Huffman:   
    def generar_arbol_huffman(self, frecuencia_letras):
        cola_prioridad = [Node(caracter, frecuencia) for caracter, frecuencia in frecuencia_letras.items()]
        heapq.heapify(cola_prioridad)

        
        while len(cola_prioridad) > 1:
            izq = heapq.heappop(cola_prioridad)
            der = heapq.heappop(cola_prioridad)
            new_node = Node(frecuencia = izq.frecuencia + der.frecuencia, hijo_izq = izq, hijo_der = der)
            heapq.heappush(cola_prioridad, new_node)

        return cola_prioridad[0]
    
    def diccionario_codigos_nuevos(self, arbol_huffman, codigo = '', diccionario = None):
        if diccionario is None:
            diccionario = {}
        if arbol_huffman.simbolo is not None:
            diccionario[arbol_huffman.simbolo] = codigo
        if arbol_huffman.hijo_izq is not None:
           self.diccionario_codigos_nuevos(arbol_huffman.hijo_izq, codigo + '0', diccionario)
        if arbol_huffman.hijo_der is not None:
            self.diccionario_codigos_nuevos(arbol_huffman.hijo_der, codigo + '1', diccionario)
        """print(diccionario)"""
        return diccionario
             
        

Obj = Huffman()

Obj1 = Text()
Direccion = "C:/Users/Rodrigo/OneDrive/Documentos/Compresor/input.txt"
frecuencia_letras = Obj1.frecuencia_simbolos(Direccion)
arbol_de_huffman = Obj.generar_arbol_huffman(frecuencia_letras)
diccionario_codigos_nuevos = Obj.diccionario_codigos_nuevos(arbol_de_huffman)
"""print(diccionario_codigos_nuevos)"""
text = Obj1.obtener_texto(Direccion)

texto_codificado = Obj1.codificar_texto(text, diccionario_codigos_nuevos)

archivo_comprimido = "C:/Users/Rodrigo/OneDrive/Documentos/Compresor/o.bin"
archivo_huff_comprimido = "C:/Users/Rodrigo/OneDrive/Documentos/Compresor/o.pkl"
Obj1.comprimir(diccionario_codigos_nuevos, text, archivo_comprimido,arbol_de_huffman , archivo_huff_comprimido)
Obj1.descomprimir(archivo_comprimido, archivo_huff_comprimido)

Obj2 = Imagen()
Direccion = "C:/Users/Rodrigo/OneDrive/Documentos/Compresor/img.bmp"
frecuencia_letras = Obj2.frecuencia_simbolos(Direccion)
arbol_de_huffman = Obj.generar_arbol_huffman(frecuencia_letras)
diccionario_codigos_nuevos = Obj.diccionario_codigos_nuevos(arbol_de_huffman)
text = Obj2.obtener_imagen(Direccion)

texto_codificado = Obj2.codificar_texto(text, diccionario_codigos_nuevos)

archivo_comprimido = "C:/Users/Rodrigo/OneDrive/Documentos/Compresor/img.bin"
archivo_huff_comprimido = "C:/Users/Rodrigo/OneDrive/Documentos/Compresor/arbol.pkl"
Obj2.comprimir(diccionario_codigos_nuevos, text, archivo_comprimido,arbol_de_huffman , archivo_huff_comprimido)
Obj2.descomprimir(archivo_comprimido, archivo_huff_comprimido)
