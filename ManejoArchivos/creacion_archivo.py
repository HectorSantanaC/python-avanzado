# Crear Archivo
nombre_archivo = 'mi_archivo.txt'

#Abrir el archivo en modo escritura ('w')
with open(nombre_archivo, 'w') as archivo:
  archivo.write('Hola ¿Como estás?\n')
  archivo.write('Estoy agregando información al archivo\n')

# Abrir archivo
# archivo = open(nombre_archivo, 'w')
# archivo.write('Hola ¿Como estás?\n')
# archivo.write('Estoy agregando información al archivo\n')
# archivo.close()

print(f'Se creó el archivo: {nombre_archivo}')