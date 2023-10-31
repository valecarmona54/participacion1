from pygame import mixer

mixer.init()

class Cancion:
    def __init__(self, nombre, artista):
        self.nombre:str = nombre

class ListaReproduccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_canciones= []
    def agregar_cancion_lista(self,cancion):
        self.lista_canciones.append(cancion)
    def eliminar_cancion_lista(self,nombre):
        for cancion in self.lista_canciones:
            if cancion.nombre ==nombre:
                self.lista_canciones.remove(cancion)
                return True
        return False
    def mostrar_cancion(self):
        for i, cancion in enumerate(self.lista_canciones):
            print (f"{i + 1}.{cancion.nombre}")
    def mostrar_canciones_lista(self):
        print (f"Canciones de la lista {self.nombre}: ")
        for i, cancion in enumerate(self.lista_canciones):
            print (f"{i + 1}.{cancion.nombre}")

class Reproductor:
    def __init__(self):
        self.lista_reproducciones= {} 
    def crear_lista_reproducciones(self):
        nombre_lista =input("Ingrese el nombre de la lista de producciones: ")
        if nombre_lista in self.lista_reproducciones:
            print ("Ya existe una lista con ese nombre")
        else:
            self.lista_reproducciones[nombre_lista] = ListaReproduccion(nombre_lista)
    def mostrar_listas(self):
        print ("Listas de reproducción creadas")
        for lista_nombre in self.lista_reproducciones:
            print (lista_nombre)

    def reproducir_cancion():
        mixer.music.load("cancion1.mp3")
        mixer.music.play()


class Cola:
    def __init__(self):
        self.lista_reproduccion:ListaReproduccion
    def agregar_a_cola(self):
        pass
    
class Usuario:
    def __init__(self,nombre,correo):
        self.nombre:str = nombre
        self.correo:str = correo
        self.lista_reproduccion:ListaReproduccion

class Software:
    def __init__(self, catalogo):
        self.catalogo = catalogo 

    def crear_cola(self):
        pass
    