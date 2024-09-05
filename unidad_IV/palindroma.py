cadena = input('Introduce una cadena:  ')
cadena = cadena.lower()
cadena = cadena.replace(' ', '')
print(cadena)
cadenaInvertida = cadena[::-1]
print(cadenaInvertida)
if cadena == cadenaInvertida:
    print('Es palindroma')
else:
    print('No es palindroma')