# Ejercicio 7.5: Recorrer el árbol de archivos
# Escribí un programa que dado un directorio, imprima en pantalla los nombres de 
# todos los archivos .png que se encuentren en algún subdirectorio del él.

# Observación: Al final, tu script debería poder ejecutarse desde la línea de 
# comandos recibiendo como parámetro el directorio a leer original. 
# En la Sección 6.2 dimos un modelo de script que te puede servir.

import os
import sys

def list_imgs(path):
  directory_tree = os.walk(path, topdown=True)
  all_files = []
  for _,_,files in directory_tree:
    all_files.extend(files)
  
  png_files = []
  
  for sing_file in all_files:
    if sing_file[-4:] == '.png':
      png_files.append(sing_file)

  return png_files
  
if __name__ == '__main__':
  print(list_imgs(sys.argv[1]))