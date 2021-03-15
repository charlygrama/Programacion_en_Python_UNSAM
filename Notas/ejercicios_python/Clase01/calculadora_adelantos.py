# adelantos.py
# Ejercicio 1.9 y 1.10: Calculadora de Adelantos y Tabla

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
total_meses = 0

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0: 
    # if total_meses <= 12:
    #     saldo = saldo * (1 + tasa/12) - pago_extra   
    #     total_pagado = total_pagado + pago_extra 
    #     total_meses += 1]
    if  total_meses < pago_extra_mes_comienzo:
        saldo = saldo * (1 + tasa/12) - pago_mensual   
        total_pagado = total_pagado + pago_mensual 
        total_meses += 1
    elif pago_extra_mes_comienzo <= total_meses <= pago_extra_mes_fin:
        saldo = saldo * (1 + tasa/12) - pago_mensual - pago_extra  
        total_pagado = total_pagado + pago_mensual  + pago_extra
        total_meses += 1  
    elif total_meses > pago_extra_mes_fin: 
        saldo = saldo * (1 + tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual  
        total_meses += 1

        if saldo < 0:
            total_pagado += saldo
            saldo -= saldo
    print (total_meses, round(saldo, 2), round(total_pagado, 2))

print( 'Total pagado: ', round(total_pagado, 2))
print( 'Meses: ', total_meses)
print('saldo: ', saldo)