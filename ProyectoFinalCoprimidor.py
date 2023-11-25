import heapq
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

class Huffman:
    def audio_to_binary(self, file_path):
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
        return frecuencia_binaria



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
        return diccionario
    
    def codificar_texto(self, texto, diccionario):
        texto_codificado = ''.join(diccionario[caracter] for caracter in texto)
        print(texto_codificado)
        return texto_codificado
    
    def decodificar_texto(self, bits, arbol_huffman):
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
        
        resultado = ''.join(texto_recuperado)
        print(resultado)
        return ''.join(texto_recuperado)
    
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


    
    def crear_archivo_bin(self, texto_codificado, archivo_salida):
        with open(archivo_salida, 'wb') as archivo:
            archivo.write(bytes(texto_codificado, 'utf-8'))


"""Objeto1 = Huffman()
Direccion = "OneDrive\Documentos\Tercersemestre\Estructuras II\Parcial 3\input.txt"
frecuencia_letras = Objeto1.frecuencia_simbolos(Direccion)
arbol_de_huffman = Objeto1.generar_arbol_huffman(frecuencia_letras)
diccionario_codigos_nuevos = Objeto1.diccionario_codigos_nuevos(arbol_de_huffman)
print(diccionario_codigos_nuevos)
text = Objeto1.obtener_texto(Direccion)

texto_codificado = Objeto1.codificar_texto(text, diccionario_codigos_nuevos)
texto_decodificado = Objeto1.decodificar_texto(texto_codificado, arbol_de_huffman)

archivo_salida = "OneDrive\Documentos\Tercersemestre\Estructuras II\Parcial 3\o.bin"
Objeto1.crear_archivo_bin(texto_codificado, archivo_salida)"""


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

Objeto3 = Huffman()
binary_data =Objeto3.audio_to_binary("OneDrive\Documentos\Tercersemestre\Estructuras II\Parcial 3\Audio.mp3")
Objeto3.calcular_frecuencia_binaria(binary_data)
