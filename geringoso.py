cadena = 'Geringosorelocoaaaa'
cadenaGeringoso = ''

for c in cadena:
    if c == 'a':
        cadenaGeringoso = cadenaGeringoso + c + 'pa'
    elif c == 'e':
        cadenaGeringoso = cadenaGeringoso + c + 'pe'
    elif c == 'i':
        cadenaGeringoso = cadenaGeringoso + c + 'pi'
    elif c == 'o':
        cadenaGeringoso = cadenaGeringoso + c + 'po'
    elif c == 'u':
        cadenaGeringoso = cadenaGeringoso + c + 'pu'
    else: 
        cadenaGeringoso = cadenaGeringoso + c

print(cadenaGeringoso)
