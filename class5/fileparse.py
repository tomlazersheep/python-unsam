# fileparse.py
import csv


def parse_csv(nombre_archivo, select=[], types=[],  has_headers=True):
  '''
  Parsea un archivo CSV en una lista de registros
  '''
  if not(has_headers) and len(select):
    raise RuntimeError('select parameter invalid when has_headers is set to True')

  with open(nombre_archivo) as f:
    rows = csv.reader(f)

    if has_headers:
      # Lee los encabezados
      headers = next(rows)

    registros = []
    for row in rows:
      if not row:    # Saltea filas sin datos
        continue
      
      if has_headers:
        registros.append(dict(zip(headers, row)))
      else: 
        registros.append(list(row))

  remove_headers = []

  if len(select):
    remove_headers = [ header for header in headers if not(header in select)]
    for header_to_remove in remove_headers:
      for register in registros:
        register.pop(header_to_remove, None)

  if len(types):
    if has_headers:
        
      if len(types) != (len(headers)-len(remove_headers)):
        raise RuntimeError('TypesSizeUncompatible')
      
      for register in registros:
        keywords = dict(zip(register.keys(),types))
        for key,single_type in keywords.items():
          register[key] = single_type(register[key])
    else:
      typed_registers = []
      # breakpoint()
      for register in registros:
        typed_register = []
        for i,data in enumerate(register):
          typed_register.append(types[i](data))
        typed_registers.append(tuple(typed_register))
      return typed_registers
  return registros


parse_csv('../Data/camion.csv',
                select=['cajones', 'precio'], types=[int, float])

parse_csv('../Data/precios.csv', types=[str, float], has_headers=False)
