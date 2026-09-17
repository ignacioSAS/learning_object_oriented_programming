#-------------------------------METODOS:INSTANCIA,CLASE Y ESTATICOS------------------------------------#
'''Como ya hemos visto se pueden crear metodos con < def > dentro de una clase pudiendo recivir parametros
como entrada y modificar el estado de la instancia,haciendo uso de los decoradores es pocible crear diferentes
tipos de metodos.

*Los metodos de instancia "normales" que ya hemos visto metodo()
*Metodos de clase con el decorador @classmethod
*Metodos estaticos usando el decorador staticmethod

En la siguiente clase tenemos un ejemplo donde definimos los tres tipos de metodos.'''

class Clase:
  def metodo(self):
    return 'Metodo normar',self
  
@classmethod
def metododeclase(cls):
  return 'Metodo de clase',cls
  
@staticmethod
def metodoestatico():
    return 'Metodo estatico'

