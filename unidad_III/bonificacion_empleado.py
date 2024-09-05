sueldo_base = float(input('Introduce tu sueldo base:  '))

porcentaje_objetivo = float(input('Introduce el porcentaje de sueldo objetivo:  '))

if porcentaje_objetivo >= 90:
    sueldo_total = sueldo_base + (sueldo_base * 0.20)
elif porcentaje_objetivo >= 70 and porcentaje_objetivo < 90:
    sueldo_total = sueldo_base + (sueldo_base * 0.10)
elif porcentaje_objetivo >= 50 and porcentaje_objetivo < 70:
    sueldo_total = sueldo_base + (sueldo_base * 0.05)
else:
    sueldo_total = sueldo_base

print(f'El sueldo total es: {sueldo_total:.2f}')