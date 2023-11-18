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
    def frecuencia_simbolos(self, direccion):
        frecuencia_letras = {}
        with open(direccion,'r') as file:
            text = file.read()
        for caracter in text:
            frecuencia_letras[caracter] = frecuencia_letras.get(caracter, 0) + 1
        self.generar_arbol_huffman(frecuencia_letras)
    
    def generar_arbol_huffman(self, frecuencia_letras):
        cola_prioridad = [Node(caracter, frecuencia) for caracter, frecuencia in frecuencia_letras.items()]
        heapq.heapify(cola_prioridad)
        while len(cola_prioridad) > 1:
            izq = heapq.heappop(cola_prioridad)
            der = heapq.heappop(cola_prioridad)
            new_node = Node(frecuencia = izq.frecuencia + der.frecuencia, hijo_izq = izq, hijo_der = der)
            heapq.heappush(cola_prioridad, new_node)

        self.diccionario_codigos_nuevos(arbol_huffman=cola_prioridad[0])
    
    def diccionario_codigos_nuevos(self, arbol_huffman, codigo = '', table = None):
        if table is None:
            table = {}
        if arbol_huffman.simbolo is not None:
            table[arbol_huffman.simbolo] = codigo
        if arbol_huffman.hijo_izq is not None:
           self.diccionario_codigos_nuevos(arbol_huffman.hijo_izq, codigo + '0', table)
        if arbol_huffman.hijo_der is not None:
            self.diccionario_codigos_nuevos(arbol_huffman.hijo_der, codigo + '1', table)
        print(table)

