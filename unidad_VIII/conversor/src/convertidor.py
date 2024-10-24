import requests
from bs4 import BeautifulSoup

class Convertidor:
    
    def __init__(self, cantidad_bs):
        self.__cantidad_bs = cantidad_bs

    @property
    def _cantidad_bs(self):
        return self.__cantidad_bs

    @_cantidad_bs.setter
    def _cantidad_bs(self, value):
        self.__cantidad_bs = value
        
    def obtener_tasas(self):
       url = 'https://www.bcv.org.ve/'
       try:
            response = requests.get(url)
            response.raise_for_status()  

            soup = BeautifulSoup(response.content, 'html.parser')
            tasa_euro = soup.find('img', {'src': '/sites/default/files/euro-04_2.png'}).find_next('strong').text.strip()
            tasa_euro = float(tasa_euro.replace(',', '.'))
            
            tasa_dolar = soup.find('img', {'src': '/sites/default/files/dollar-04_2.png'}).find_next('strong').text.strip()
            tasa_dolar = float(tasa_dolar.replace(',', '.'))
           
            return {
                'euro': tasa_euro, 
                'dolar': tasa_dolar
            }
            
       except (requests.RequestException, AttributeError) as e:
           print(f"Error al obtener las tasas: {e}")
           return {
                'euro': 0, 
                'dolar': 0
            }
       
    def convertir_bs_a_dolares(self):
        tasa_dolar = self.obtener_tasas()['dolar']
        try :
            return self._cantidad_bs / tasa_dolar
        except ZeroDivisionError:
            return 0
    
    def convertir_bs_a_euros(self):
        tasa_euro = self.obtener_tasas()['euro']
        try :
            return self._cantidad_bs / tasa_euro
        except ZeroDivisionError:
            return 0