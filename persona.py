class Persona:
  
  def inicializar_persona(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido

  def mostrar_persona(self):
    print(f'''Persona:
          Nombre: {self.nombre}
          Apellido: {self.apellido}''')