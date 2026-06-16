class Coche:

  def __init__(self, marca, modelo, color):
    self._marca = marca
    self._modelo = modelo
    self._color = color

  def conducir(self):
    print(f'''Conduciendo el coche:
          Marca: {self._marca}
          Modelo: {self._modelo}
          Color: {self._color}''')
    
  def get_marca(self):
    return self._marca
  
  def set_marca(self, marca):
    self._marca = marca

  def get_modelo(self):
    return self._modelo
  
  def set_modelo(self, modelo):
    self._modelo = modelo

  def get_color(self):
    return self._color
  
  def set_color(self, color):
    self._color = color

# Programa principal
if __name__ == '__main__':
  coche1 = Coche('Toyota', 'Yaris', 'Azul')
  coche1.conducir()

  # Utilizar el concepto de encapsulamiento (get/set)
  coche1.set_marca('Toyota 2')
  coche1.set_modelo('Yaris 2')
  coche1.set_color('Azul 2')
  coche1.conducir()
  print(f'Atributos del coche1: {coche1.__dict__}')

  coche2 = Coche('Chevrolet', 'Trax', 'Negro')
  print(f'Atributos del coche2: {coche2.__dict__}')