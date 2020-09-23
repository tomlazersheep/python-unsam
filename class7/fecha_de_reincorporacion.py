# Ejercicio 7.3: Fecha de reincorporación
# Si tenés una licencia por xaternidad que empieza el 26 de septiembre
# de 2020 y dura 200 días, ¿qué día te reincorporás al trabajo?

import datetime

fecha_salida = datetime.date(2020,9,26)
duracion_licencia = datetime.timedelta(days=200)
print(f'reincorporacion el día {fecha_salida + duracion_licencia}')