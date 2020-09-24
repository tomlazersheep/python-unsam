# Ejercicio 7.6: Ordenar el árbol de archivos (optativo)
# Escribí un programa que te permita ordenar las imágenes PNG de esta carpeta. 
# Guardalo en un archivo ordenar_imgs.py.

# Creá un nuevo directorio Data/imgs_procesadas/.
# Usá os.walk() para recorrer los archivos en la carpeta Data/ordenar/ (y sus subcarpetas).
# Cuando encuentres archivos con extensión png los vas a procesar. En este caso procesar significa:
# Leer la fecha que se encuentra codificada en los últimos 8 caracteres 
# de su nombre en el formato AAAAMMDD (año en 4 dígitos, mes en 2 y día en 2).
# Usar la fecha obtenida para setear la fecha de última modificación y de último acceso.
# Cambiarle el nombre al archivo para que no tenga más esos dígitos (ni el guión bajo).
# Mover el archivo a la carpeta Data/imgs_procesadas/.
# Los archivos que no son png no los modifiques.
# Borrá todas las subcarpetas de Data/ordenar/ que hayan quedado vacías.
# Observación: Al final, tu script debería poder ejecutarse desde la línea de 
# comandos recibiendo como parámetro el directorio a leer original y un 
# directorio destino (que debería ser creado si no existe).

# Observación: Este tipo de tareas se repite con mucha frecuencia. 
# Tener la capacidad de automatizarlas mediante un script de Python 
# te puede ahorrar muchísimo tiempo.

# Algunos puntos importantes:

# Te recomendamos que modularices el procesamiento de los archivos png. 
# Podés, por ejemplo, escribir una función que manipule strings (que tome 
# el nombre de un archivo y devuelva la fecha y el nombre corregido) y otra 
# función que precese cada archivo (que use la función anterior para renombrar, 
# mover y modificar la fecha de cada archivo). La modularización del código es clave para que 
# otras personas lo puedan entender y que sea sencillo de mantener.
# Usá docstrings y comentarios en tu código de manera que sea legible.


import os
import sys
import datetime

# creo la clase file que es como voy a guardar los datos de cada foto de la carpeta origen
class File:
  def __init__(self, filename, path):
    self.filename = filename
    self.path = path
  
  def __str__(self):
    return(f'\n\nfile name: {self.filename} \npath: {self.path} \
    \nnew_name: {self.new_name} \ndate: {self.date}')

  date = None
  new_name = ''


# tomo todos los files del directorio origen y creo instancias de File,
# también filtro para quedarme solo con los pngs
def get_imgs(path):
  '''
  Toma un path y devuelve una lista con los objetos File de los archivos .png en ese path
  '''
  directory_tree = os.walk(path, topdown=True)
  
  all_files = []
  
  for dirpath,_,files in directory_tree:
    for sing_file in files:
      all_files.append(File(sing_file,dirpath))
  
  png_files = []
  
  for sing_file in all_files:
    if sing_file.filename[-4:] == '.png':
      png_files.append(sing_file)

  return png_files

def process_imgs(imgs_list):
  '''
  Toma una lista de objetos File y les agrega el nuevo nombre y la fecha,
  devuelve la lista con los objetos modificados 
  '''
  for img in imgs_list:
    img.date = datetime.datetime.strptime(img.filename[-12:-4], '%Y%m%d')
    img.new_name = img.filename[:-13] + img.filename[-4:]
  return imgs_list

def move_images(images, destination):
  '''
  Toma lista de objetos File y los mueve desde el path de cada uno hasta el path destination,
  si no existe el directorio especificado en destination, lo crea. devuelve la lista con el path
  actualizado
  '''
  if not os.path.isdir(destination):
    os.mkdir(destination)
    
  for img in images:
    os.rename(os.path.join(img.path,img.filename), os.path.join(destination, img.new_name))
    img.path = destination
  return images

def change_dates(images):
  '''
  Toma una lista de objetos File y cambia las fechas de acceso y modificacion de los 
  archivos encontrados en path/new_name por la fecha en date
  '''
  for img in images:
    os.utime(os.path.join(img.path,img.new_name), (img.date.timestamp(),img.date.timestamp()))
  return images

def main(argv):
  all_imgs = get_imgs(argv[1])
  all_imgs = process_imgs(all_imgs)
  all_imgs = move_images(all_imgs, argv[2])
  all_imgs = change_dates(all_imgs)

if __name__ == '__main__':
  main(sys.argv)
