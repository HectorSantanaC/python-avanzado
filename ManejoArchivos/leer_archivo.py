print('Leer archivo con Python')

nombre_archivo = 'mi_archivo.txt'

# Leer un archivo usando el método readLines
with open(nombre_archivo, 'r') as archivo:

  # Leer todas las líneas del archivo
  # print(archivo.readlines())
  lineas = archivo.readlines()
  for linea in lineas:
    print(linea.strip())

# Leer todo el contenido del archivo usando el método read

print('Leyendo el contenido con el método read')

with open(nombre_archivo, 'r') as archivo:
  print(archivo.read().strip())