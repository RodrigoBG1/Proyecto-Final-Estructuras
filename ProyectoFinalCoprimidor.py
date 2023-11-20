import heapq

class Node:
    def __init__(self, simbolo = None, frecuencia = 0, hijo_izq = None, hijo_der = None):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.hijo_izq = hijo_izq
        self.hijo_der = hijo_der
    
    def __lt__(self, otro): #Esto se usa para que al momento de utilizar la funcion "heapify" compare de acuerdo con la frecuencia
        return self.frecuencia < otro.frecuencia

class Huffman:
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
        return self.generar_arbol_huffman(frecuencia_letras)
    
    def generar_arbol_huffman(self, frecuencia_letras):
        cola_prioridad = [Node(caracter, frecuencia) for caracter, frecuencia in frecuencia_letras.items()]
        heapq.heapify(cola_prioridad)
        
        while len(cola_prioridad) > 1:
            izq = heapq.heappop(cola_prioridad)
            der = heapq.heappop(cola_prioridad)
            new_node = Node(frecuencia = izq.frecuencia + der.frecuencia, hijo_izq = izq, hijo_der = der)
            heapq.heappush(cola_prioridad, new_node)

        return cola_prioridad[0]
        return self.diccionario_codigos_nuevos(cola_prioridad[0])
    
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
    
    def codificar(self, texto, diccionario):
        texto_codificado = ''.join(diccionario[caracter] for caracter in texto)

        return texto_codificado
    
    def decodificar(self, bits, arbol_huffman):
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
    

Objeto1 = Huffman()
Direccion = "OneDrive\Documentos\Tercersemestre\Estructuras II\Parcial 3\input.txt"
frecuencia_letras = Objeto1.frecuencia_simbolos(Direccion)
arbol_de_huffman = Objeto1.generar_arbol_huffman(frecuencia_letras)
diccionario_codigos_nuevos = Objeto1.diccionario_codigos_nuevos(arbol_de_huffman)
text = Objeto1.obtener_texto(Direccion)

texto_codificado = Objeto1.codificar(text, diccionario_codigos_nuevos)
texto_decodificado = Objeto1.decodificar(texto_codificado, arbol_de_huffman)

