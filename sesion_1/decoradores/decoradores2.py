def aviso(fn):
  def envoltura():
    print('Iniciando tarea...')
    print(fn())
    print('Terminando tarea...')
  return envoltura

@aviso
def tarea():
  return 'La tarea es urgente'

tarea()