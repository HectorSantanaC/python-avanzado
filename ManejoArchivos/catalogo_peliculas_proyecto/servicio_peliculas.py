import os

from catalogo_peliculas_proyecto.pelicula import Pelicula


class ServicioPeliculas:

  NOMBRE_ARCHIVO = "peliculas.txt"    

  def agregar_pelicula(self, pelicula):
    with open(self.NOMBRE_ARCHIVO, 'a', encoding='utf8') as archivo:
      archivo.write(f'{pelicula.nombre}\n')

  def listar_peliculas(self):
    with open(self.NOMBRE_ARCHIVO, 'r', encoding='utf8') as archivo:
      print('--- Listado de Películas ---')
      print(archivo.read())

  def eliminar_archivo_peliculas(self):
    os.remove(self.NOMBRE_ARCHIVO)
    print('Archivo eliminado: peliculas.txt')