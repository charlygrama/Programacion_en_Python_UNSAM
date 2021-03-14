# adelantos.py
# Ejercicio 1.9: Calculadora de Adelantos

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
total_meses = 0
adelanto = 0

while saldo > 0:
    if adelanto < 12000:
        saldo = saldo * (1 + tasa/12) - pago_mensual - 1000 
        total_pagado = total_pagado + pago_mensual + 1000 
        total_meses += 1
        adelanto += 1000
    else:
        saldo = saldo * (1 + tasa/12) - pago_mensual  
        total_pagado = total_pagado + pago_mensual  
        total_meses += 1

print('Total pagado: ', round(total_pagado, 2))
print('Total de meses: ', total_meses)