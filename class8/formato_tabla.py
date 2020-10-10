class FormatoTabla:
  def encabezado(self, headers):
    '''
    Crea el encabezado de la tabla.
    '''
    raise NotImplementedError()

  def fila(self, rowdata):
    '''
    Crea una única fila de datos de la tabla.
    '''
    raise NotImplementedError()
  

def crear_formateador(formato):
  '''
  crear un objeto formateador dado un tipo de salida como txt, csv, o html
  '''
  if formato == 'txt':
    return FormatoTablaTXT()
  elif formato == 'csv':
    return FormatoTablaCSV()
  elif formato == 'html':
    return FormatoTablaHTML()
  else:
    raise RuntimeError('Not a valid format')

class FormatoTablaTXT(FormatoTabla):
  '''
  Generar una tabla en formato TXT
  '''
  def encabezado(self, headers):
    for h in headers:
        print(f'{h:>10s}', end=' ')
    print()
    print(('-'*10 + ' ')*len(headers))

  def fila(self, data_fila):
    for d in data_fila:
        print(f'{d:>10s}', end=' ')
    print()


class FormatoTablaCSV(FormatoTabla):
  '''
  Generar una tabla en formato CSV
  '''
  def encabezado(self, headers):
    print(','.join(headers))

  def fila(self, data_fila):
    print(','.join(data_fila))


class FormatoTablaHTML(FormatoTabla):
  '''
  Generar tabla en HTML
  '''
  def encabezado(self,headers):
    print('<table>')
    print('<tr>')
    for header in headers:
      print(f'<th>{header}</th>')
    print('</tr>')
  
  def fila(self,data_fila):
    print('<tr>')
    for data in data_fila:
      print(f'<td>{data}</td>')
    print('</tr>')
  
  def end_table(self):
    print('</table>')