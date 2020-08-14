# hipoteca.py
# Archivo de ejemplo
# Ejercicio

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
pago_extra = 1000
extraPaymentInitialMonth = 61
extraPaymentFinalMonth = 108
pago_extra = 1000
mes = 0
total_pagado = 0.0
# Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca.

while saldo > 0:
    if mes <= extraPaymentFinalMonth and mes >= extraPaymentInitialMonth :
        saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra
    else: 
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual

    mes+=1
total_pagado = round(total_pagado,2)

print(f'Total pagado {total_pagado} en {mes} meses.')
