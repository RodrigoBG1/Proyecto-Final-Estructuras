import heapq
import pickle
from bitarray import bitarray
from PIL import Image
import librosa
import numpy as np

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
        """print("Diccionario:", frecuencia_letras)"""
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
            if bit == '0':
                nodo_actual = nodo_actual.hijo_izq
            else:
                nodo_actual = nodo_actual.hijo_der

            if nodo_actual.simbolo is not None:
                texto_recuperado += nodo_actual.simbolo
                nodo_actual = arbol_huffman

        with open("OneDrive\Documentos\Tercersemestre\Estructuras II\Parcial 3\Pruebas_txt\descomprimido.txt", 'w') as file:
            file.write(texto_recuperado)

        return texto_recuperado
    
class Image:
    def obtener_imagen(self, direccion):
        imagen = Image.open(direccion)
        ancho, alto = imagen.size
        return imagen, ancho, alto
    
    def frecuencia_simbolos_imagen(self, direccion):
        frecuencia_pixeles = {}
        imagen, a, b = self.obtener_imagen(direccion)

        for pixel in imagen.getdata():
            frecuencia_pixeles[pixel] = frecuencia_pixeles.get(pixel, 0) + 1

        return frecuencia_pixeles
    
    def codificar_imagen(self, imagen, diccionario):
        pixels = list(imagen.getdata())
        imagen_codificada = ''.join(diccionario[pixel] for pixel in pixels)
        return imagen_codificada
    
    def decodificar_imagen(self, bits, arbol_huffman, ancho, alto):
        texto_recuperado = []
        nodo_actual = arbol_huffman

        for bit in bits:
            if bit == '0':
                nodo_actual = nodo_actual.hijo_izq
            else:
                nodo_actual = nodo_actual.hijo_der

            if nodo_actual.simbolo is not None:
                texto_recuperado.append(nodo_actual.simbolo)
                nodo_actual = arbol_huffman

        # Crea la imagen con el tamaño proporcionado
        imagen_recuperada = Image.new('RGB', (ancho, alto))
        imagen_recuperada.putdata(texto_recuperado)

        imagen_recuperada.save("OneDrive\Documentos\Tercersemestre\Estructuras II\Parcial 3\imagen2_recuperada.jpg")

        # Muestra la imagen usando el visor de imágenes predeterminado
        imagen_recuperada.show()

        return imagen_recuperada
    
class Audio:
    """def audio_to_binary(self, file_path):
        # Carga el archivo de audio
        audio_data, sr = librosa.load(file_path)

        # Cuantización (normalización a valores entre -1 y 1)
        normalized_audio = audio_data / np.max(np.abs(audio_data))

        # Muestreo (convierte a valores enteros entre -32768 y 32767, por ejemplo, para audio de 16 bits)
        audio_int = np.int16(normalized_audio * 32767)

        # Convierte los valores enteros a binario
        binary_data = ''.join(format(sample, '016b') for sample in audio_int)
        return binary_data
    
    def calcular_frecuencia_binaria(self, binary_data, longitud_simbolo=16):
        frecuencia_binaria = {}
        # Divide los datos binarios en segmentos de longitud_simbolo
        simbolo = [binary_data[i:i+longitud_simbolo] for i in range(0, len(binary_data), longitud_simbolo)]

        # Cuenta la frecuencia de cada símbolo
        for simbolo in binary_data:
            frecuencia_binaria[simbolo] = frecuencia_binaria.get(simbolo, 0) + 1
        print(frecuencia_binaria)
        return frecuencia_binaria""" 


class Huffman:   
    def generar_arbol_huffman(self, frecuencia_letras):
        cola_prioridad = [Node(caracter, frecuencia) for caracter, frecuencia in frecuencia_letras.items()]
        """print("Cola de prioridad sin heapify:")
        for i in range(len(cola_prioridad)):
            print(cola_prioridad[i].simbolo, cola_prioridad[i].frecuencia, end = "\t") #Si yo pusiera esto "cola_prioridad[i].caracter" me marca error porque no tiene atributo 'caracter' tiene 'simbolo'
        print()
        print("Cola de prioridad con heapify:")"""
        heapq.heapify(cola_prioridad)
        """for i in range(len(cola_prioridad)):
            print(cola_prioridad[i].simbolo, cola_prioridad[i].frecuencia, end = "\t")"""
        """print("Funcion pop:")
        heapq.heappop(cola_prioridad)
        for i in range(len(cola_prioridad)):
            print(cola_prioridad[i].simbolo, cola_prioridad[i].frecuencia, end = "\t")"""
        
        while len(cola_prioridad) > 1:
            izq = heapq.heappop(cola_prioridad)
            der = heapq.heappop(cola_prioridad)
            new_node = Node(frecuencia = izq.frecuencia + der.frecuencia, hijo_izq = izq, hijo_der = der)
            heapq.heappush(cola_prioridad, new_node)

        """print(cola_prioridad[0].simbolo, cola_prioridad[0].frecuencia)
        print(cola_prioridad[0].hijo_izq.simbolo, cola_prioridad[0].hijo_izq.frecuencia)
        print(cola_prioridad[0].hijo_der. simbolo, cola_prioridad[0].hijo_der.frecuencia)
        print(cola_prioridad[0].hijo_der.hijo_izq.simbolo, cola_prioridad[0].hijo_der.hijo_izq.frecuencia)
        print(cola_prioridad[0].hijo_der.hijo_der.simbolo, cola_prioridad[0].hijo_der.hijo_der.frecuencia)"""

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
Direccion = "OneDrive\Documentos\Tercersemestre\Estructuras II\Parcial 3\Pruebas_txt\input.txt"
frecuencia_letras = Obj1.frecuencia_simbolos(Direccion)
arbol_de_huffman = Obj.generar_arbol_huffman(frecuencia_letras)
diccionario_codigos_nuevos = Obj.diccionario_codigos_nuevos(arbol_de_huffman)
"""print(diccionario_codigos_nuevos)"""
text = Obj1.obtener_texto(Direccion)

texto_codificado = Obj1.codificar_texto(text, diccionario_codigos_nuevos)

archivo_comprimido = "OneDrive\Documentos\Tercersemestre\Estructuras II\Parcial 3\Pruebas_txt\o.bin"
archivo_huff_comprimido = "OneDrive\Documentos\Tercersemestre\Estructuras II\Parcial 3\Pruebas_txt\salida_arbol.pkl"
Obj1.comprimir(diccionario_codigos_nuevos, text, archivo_comprimido,arbol_de_huffman , archivo_huff_comprimido)
Obj1.descomprimir(archivo_comprimido, archivo_huff_comprimido)


"""Objeto2 = Huffman()
Direccion_imagen = "OneDrive\Documentos\Tercersemestre\Estructuras II\Parcial 3\imagen2.jpg"
frecuencia_pixeles = Objeto2.frecuencia_simbolos_imagen(Direccion_imagen)
arbol_huffman_imagen = Objeto2.generar_arbol_huffman(frecuencia_pixeles)
diccinario_codigos_nuevos_imagen = Objeto2.diccionario_codigos_nuevos(arbol_huffman_imagen)
print(diccinario_codigos_nuevos_imagen)
imagen, ancho, alto = Objeto2.obtener_imagen(Direccion_imagen)

imagen_codificada = Objeto2.codificar_imagen(imagen, diccinario_codigos_nuevos_imagen)
print(imagen_codificada)
imagen_decodificada = Objeto2.decodificar_imagen(imagen_codificada, arbol_huffman_imagen, ancho, alto)
print(imagen_decodificada)"""

"""Objeto3 = Huffman()
binary_data = Objeto3.audio_to_binary("OneDrive\Documentos\Tercersemestre\Estructuras II\Parcial 3\Audio.mp3")
frecuencia_binaria = Objeto3.calcular_frecuencia_binaria(binary_data)
arbol_huffman_audio = Objeto3.generar_arbol_huffman(frecuencia_binaria)"""
