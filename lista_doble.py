import graphviz
import os

class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_al_principio(self, nombre, apellido, carnet):
        nuevo = Nodo(nombre, apellido, carnet)
        if not self.cabeza:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        self.generar_grafica()

    def insertar_al_final(self, nombre, apellido, carnet):
        nuevo = Nodo(nombre, apellido, carnet)
        if not self.cabeza:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo
        self.generar_grafica()

    def mostrar_lista(self):
        actual = self.cabeza
        print("None", end=" <- ")
        while actual:
            print(f"[{actual.nombre}]", end=" <-> " if actual.siguiente else " -> ")
            actual = actual.siguiente
        print("None")

    def generar_grafica(self):
        dot = graphviz.Digraph(comment='Lista Doblemente Enlazada', format='png')
        dot.attr(rankdir='LR') 
        
        actual = self.cabeza
        while actual:
            label = f"{actual.nombre} {actual.apellido}\n{actual.carnet}"
            dot.node(str(id(actual)), label)
            
            if actual.siguiente:
                dot.edge(str(id(actual)), str(id(actual.siguiente)), constraint='true')
                dot.edge(str(id(actual.siguiente)), str(id(actual)), constraint='true')
            actual = actual.siguiente
            
        dot.render('lista_doble_visual', view=False, cleanup=True)

    def eliminar_por_valor(self, carnet):
        actual = self.cabeza
        while actual:
            if actual.carnet == carnet:
                if actual == self.cabeza and actual == self.cola:
                    self.cabeza = None
                    self.cola = None
                elif actual == self.cabeza:
                    self.cabeza = actual.siguiente
                    self.cabeza.anterior = None
                elif actual == self.cola:
                    self.cola = actual.anterior
                    self.cola.siguiente = None
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                
                self.generar_grafica() 
                return True
            actual = actual.siguiente
        return False
    