class Persona:

  # Constructor __init__ (dunder - double underscore)
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido

  def mostrar_persona(self):
    print(f'''Persona:
          Nombre: {self.nombre}
          Apellido: {self.apellido}''')
    print(f'Dir. mem self: {id(self)}')
    print(f'Dir. mem hex self: {hex(id(self))}')

# Creación de objetos
if __name__ == '__main__':
  persona1 = Persona('Layla', 'Acosta')
  persona1.mostrar_persona()
  print(f'Dir. mem persona1: {id(persona1)}')
  print(f'Dir. mem hex persona1: {hex(id(persona1))}')

  persona2 = Persona('Ian', 'Sánchez')
  persona2.mostrar_persona()
  print(f'Dir. mem persona1: {id(persona2)}')
  print(f'Dir. mem hex persona1: {hex(id(persona2))}')