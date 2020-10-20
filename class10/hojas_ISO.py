# Ejercicio 10.13: Hojas ISO y recursión
# La norma ISO 216 especifica tamaños de papel. Es el estándar que define el
#  popular tamaño de papel A4 (210mm de ancho y 297mm de largo).
#  Las hojas A0 miden 841mm de ancho y 1189mm de largo. A partir de la A0 las
#  siguientes medidas, digamos la A(N+1), se definen doblando al medio la hoja A(N).
#  Siempre se miden en milímetros con números enteros: entonces la hoja A1 mide 594mm de ancho
#  (y no 594.5) por 841mm de largo.

# Escribí una función recursiva que para una entrada N mayor que cero, devuelva
#  el ancho y el largo de la hoja A(N) calculada recursivamente a partir de las medidas de la hoja 
# A(N−1), usando la hoja A0 como caso base.

A0_ancho_mm = 841
A0_largo_mm = 1189

def iso_N(N,ancho,largo):
  if N == 1:
    return ancho,largo//2
  else:
    return iso_N(N-1,largo//2,ancho)

print(iso_N(4,A0_ancho_mm,A0_largo_mm))