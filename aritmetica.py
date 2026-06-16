class Aritmetica:

  def __init__(self, operando1=None, operando2=None):
    self.operando1 = operando1
    self.operando2 = operando2

  def sumar(self):
    resultado = self.operando1 + self.operando2
    print(f'Resultado suma: {resultado}')

  def restar(self):
    resultado = self.operando1 - self.operando2
    print(f'Resultado resta: {resultado}')

# Programa principal
if __name__ == '__main__':
  print('*** Ejemplo Clase Aritmetica ***')
  print('Primer objeto')
  aritmetica1 = Aritmetica(5, 7)
  aritmetica1.sumar()

  print('Segundo objeto')
  aritmetica2 = Aritmetica(12, 16)
  aritmetica2.restar()

  print('Tercer objeto')
  aritmetica3 = Aritmetica(4)
  aritmetica3.operando2 = 7
  aritmetica3.sumar()

  print('Cuarto objeto')
  aritmetica4 = Aritmetica()
  aritmetica4.operando1 = 2
  aritmetica4.operando2 = 6
  aritmetica4.restar()

  print('Quinto objeto')
  aritmetica5 = Aritmetica(operando2=5, operando1=8)
  aritmetica5.sumar()