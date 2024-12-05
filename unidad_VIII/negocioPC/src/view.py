from orden import Orden
from computadora import Computadora
from teclado import Teclado
from mouse import Mouse
from monitor import Monitor

def agrega_datos():
    mouse1  = Mouse("Dell", "USB", 3)
    mouse2  = Mouse("HP", "USB", 4)
    mouse3  = Mouse("Lenovo", "USB", 5)

    teclado1 = Teclado("Dell", "USB", 3)
    teclado2 = Teclado("HP", "USB", 4)
    teclado3 = Teclado("Lenovo", "USB", 5)
    
    monitor1 = Monitor("Dell", '"24"', 100)
    monitor2 = Monitor("HP", '"17"', 60)
    monitor3 = Monitor("Lenovo", '"27"', 150)
    
    computadora1 = Computadora(teclado1, mouse1, monitor1, 100)
    computadora2 = Computadora(teclado2, mouse2, monitor2, 200)
    computadora3 = Computadora(teclado3, mouse3, monitor3, 300)
    
    orden = Orden([])
    orden2 = Orden([])
    
    orden.add_computadora(computadora1)
    orden.add_computadora(computadora2)
    
    orden2.add_computadora(computadora3)
    print(orden)
    print(orden2)
    
    txt1 = orden.create_txt('archivo1')
    txt2 = orden2.create_txt('archivo2')
    print(f'se crearon los archivos txt con los datos de las ordenes {txt1} y {txt2}')
    
if __name__ == '__main__':
    agrega_datos()