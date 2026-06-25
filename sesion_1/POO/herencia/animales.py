class Animal:
  def __init__(self, nombre, peso = 44):
    self.nombre = nombre
    self.peso = peso

  def respirar(self):
    print(f"{self.nombre} está respirando")

  def comer(self, alimento):
    print(f'{self.nombre} está comiento un {alimento}')

class Perro(Animal):
  def __init__(self, nombre, peso, raza):
    super().__init__(nombre, peso)
    self.raza = raza

  def ladrar(self):
    print('Guau guau')

  def __str__(self):
    return f"Perro {self.nombre} peso {self.peso}"

lassie = Perro('Lassie', 44, 'Collie')
lassie.respirar()
print(lassie.raza)
print(lassie)