from os.path import exists

def leer_tabla_multiplicar():  
  n = int(input('Introduce un número entero entre 1 y 10: '))
  file_name = 'tabla-' + str(n) + '.txt'
  try: 
      f = open(file_name, 'r')
  except FileNotFoundError:
      print('No existe archivo con la tabla del', n)
  else:
      print(f.read())
  f.close()

leer_tabla_multiplicar()

file_exists = exists('./tabla-5.txt')

print(file_exists)