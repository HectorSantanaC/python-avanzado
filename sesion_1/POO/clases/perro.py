class Perro:
  def __init__(self, nombre, raza, edad):
    self.nombre = nombre
    self.raza = raza
    self.edad = edad
    self.patas = 4

  def ladrar(self):
    print('Guau guau')

  def presentarse(self):
    print(f"Soy {self.nombre} y tegno {self.edad}")

lassie = Perro('Lassie', 'Collie', 62)
print(lassie.edad)
print(lassie.patas)