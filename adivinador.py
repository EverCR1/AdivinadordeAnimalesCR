# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Clases
# -----------------------------------------------------------

class Arbol:
    def __init__(self, carga=None, izq=None, der=None):
        self.carga = carga
        self.izquierda = izq
        self.derecha = der

    def __str__(self):

        return str(self.carga)


# -----------------------------------------------------------

# Funciones
# -----------------------------------------------------------

def si(preg):

    resp = input(preg)
    return (resp[0] == 's')


# -----------------------------------------------------------

def main():


    print("Probando el versionamiento de código - CR")

    bucle = True
    raiz = Arbol("pajaro")
    while bucle:
        if not si("Estas pensando en un animal? "): break

        arbol = raiz
        while arbol.izquierda != None:
            if si(arbol.carga + "? "):
                arbol = arbol.izquierda
            else:
                arbol = arbol.derecha

        # adivinar
        animal = arbol.carga
        if si("Es un " + animal + "? "):
            print
            "Soy el más grande!"
            continue









        # obtener informacion
        nuevo = input("Qué animal era? ")
        info = input("Qué diferencia a un " + animal + " de un " + nuevo + "? ")
        indicador = "Si el animal fuera un " + animal + " cual seria la respuesta? "
        arbol.carga = info
        if si(indicador):
            arbol.izquierda = Arbol(animal)
            arbol.derecha = Arbol(nuevo)
        else:
            arbol.derecha = Arbol(animal)
            arbol.izquierda = Arbol(nuevo)

    return 0


if __name__ == '__main__':
    main()