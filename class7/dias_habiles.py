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
    # consigo objeto con la fecha inicial
    initial_date = datetime.datetime.strptime(initial, '%d/%m/%Y')
    
    # consigo objeto con la fecha final
    final_date = datetime.datetime.strptime(final, '%d/%m/%Y')
    
    # consigo todos los objetos con las fechas de feriados
    non_working_days_dates = [datetime.datetime.strptime(date, '%d/%m/%Y') for date in non_working_days]
    
    # armo timedelta para ir sumando los días no laborables
    non_working_total_timedelta = datetime.timedelta(days=-1)

    # consigo los días totales entre inicio y final
    total_days = final_date - initial_date

    # itero por todos los días entre inicio y final, agregando los días no laborables a mi contador
    for single_date in (initial_date + datetime.timedelta(days=n) for n in range(total_days.days)):
        if (single_date.isoweekday() in (5, 6)) or (single_date in non_working_days_dates):
           non_working_total_timedelta += datetime.timedelta(days=1)

    return (total_days - non_working_total_timedelta).days

print(get_working_days('23/09/2020','10/10/2020',feriados))