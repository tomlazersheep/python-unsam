# Ejercicio 7.4: Días hábiles
# Escribí una función dias_habiles(inicio, fin, feriados) que calcule
#  los días hábiles entre dos fechas dadas. La función debe tener como
#  argumentos el día inicial, el día final, y una lista con las fechas 
# correspondientes a los feriados que haya en ese lapso, y debe devolver 
# una lista con las fechas de días hábiles del período, incluyendo la fecha 
# inicial y la fecha final indicadas. Las fechas de entrada y salida deben 
# manejarse en formato de texto.

# Consideramos día hábil a un día que no es feriado ni sábado ni domingo.

# Probala entre hoy y el 10 de octubre, sabiendo que no hay feriados en el medio. 
# Probala entre hoy y fin de año considerando los siguientes feriados de Argentina:

import datetime

feriados = ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']

def get_working_days (initial, final, non_working_days=[]):
    initial_date = datetime.datetime.strptime(initial, '%d/%m/%Y')
    final_date = datetime.datetime.strptime(final, '%d/%m/%Y')
    
    non_working_days_dates = [datetime.datetime.strptime(date, '%d/%m/%Y') for date in non_working_days]
    
    non_working_total_timedelta = datetime.timedelta(days=0)

    total_days = final_date - initial_date

print(get_working_days('23/09/2020','10/10/2020',feriados))