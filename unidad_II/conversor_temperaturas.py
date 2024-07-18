#aplicacion que convierte grados centigrados a fahrenheit y viceversa

grados = float(input('Introduce los grados a convertir: '))

fahrenheit = (grados * 9/5) + 32
celsius = (grados - 32) * 5/9

print(f'{grados}°C son {fahrenheit}°F')
print(f'{grados}°F son {celsius}°C')