# funciones que aumentan la funcionalidad de otras funciones

def sumar(a, b):
  return a + b

def restar(a, b):
  return a - b

def decoradora(fn):
  n1 = int(input('Escribe un número: '))
  n2 = int(input('Escribe otro número: '))
  resultado = fn(n1, n2)
  print(resultado)

decoradora(sumar)