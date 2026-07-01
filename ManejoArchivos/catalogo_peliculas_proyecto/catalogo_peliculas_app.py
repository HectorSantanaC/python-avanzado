from catalogo_peliculas_proyecto.pelicula import Pelicula
from catalogo_peliculas_proyecto.servicio_peliculas import ServicioPeliculas


class AppCatalogoPeliculas:
  def __init__(self):
    self.servicio_peliculas = ServicioPeliculas()

  def mostrar_menu(self):
    print('*** App Catálogo de Películas ***')

    while True:
      try:
        print(f'''Opciones: 
          1. Agregar película
          2. Listar películas
          3. Eliminar catálogo de películas
          4. Salir''')
      
        opcion = int(input('Escribe tu opción (1-4): '))

        if opcion == 1:
          nombre_pelicula = input('Escribe el nombre de la película: ')
          pelicula = Pelicula(nombre_pelicula)
          self.servicio_peliculas.agregar_pelicula(pelicula)

        elif opcion == 2:
          self.servicio_peliculas.listar_peliculas()

        elif opcion == 3:
          self.servicio_peliculas.eliminar_archivo_peliculas()

        elif opcion == 4:
          print('¡Saliendo del programa...!')
          break

        else:
          print('Opción inválida, introduce una valor entre 1 y 4')

      except ValueError:
        print('Error: Introduce un número válido')

      except Exception as e:
        print(f'Ocurrió un error: {e}')

# Programa principal
if __name__ == '__main__':
  catalogo_peliculas = AppCatalogoPeliculas()
  catalogo_peliculas.mostrar_menu()