# Crear error propio creando una clase
class MiError(Exception):
  pass

class ConexionError(Exception):
  pass


try:
  numero = int(input('Escribe un número: '))

  if numero < 0:
    raise MiError('El número no puede ser negativo')
  print(numero)

except MiError as e:
  print(f'Error: {e}')

except Exception:
  print('Error genérico')

