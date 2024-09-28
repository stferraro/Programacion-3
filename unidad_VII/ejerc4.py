def nombre_localidad():
    localidad = input("Ingresa el nombre de la localidad: ")
    return localidad

def tempMaxima():
    tempMax = float(input("Ingresa la temperatura maxima: "))
    return tempMax

def tempMinima():
    tempMin = float(input("Ingresa la temperatura minima: "))
    return tempMin

def tempProm(tempMax, tempMin):
    return (tempMax + tempMin) / 2

def gradosFahrenheit(tempPromedio):
    return ((tempPromedio * 9) / 5) + 32

def imprime_valores(localidad, tempMax, tempMin, tempPromedio, gradosFahrenheit):
    print(localidad, tempMax, tempMin, tempPromedio, gradosFahrenheit)
    
def run():
    localidad = nombre_localidad()
    tempMax = tempMaxima()
    tempMin = tempMinima()
    tempPromedio = tempProm(tempMax, tempMin)
    grados = gradosFahrenheit(tempPromedio)
    imprime_valores(localidad, tempMax, tempMin, tempPromedio, grados)
    
run()
    
    