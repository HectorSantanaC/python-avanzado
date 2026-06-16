class Aritmetica:

  def __init__(self, operando1, operando2):
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
  aritmetica1 = Aritmetica(5, 7)
  aritmetica1.sumar()

  aritmetica2 = Aritmetica(12, 16)
  aritmetica2.restar()