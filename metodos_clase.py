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

#------------------------------------METODOS DE INSATNCIA----------------------------#

'''Los metodos de insatancia son los metodos normales de toda la vida que hemos visto toda la vida,
rciben como parametro la entrada < self > que hace referencia a la instancia que llama al metodo.
Tambien otros argumentos como entrada'''

class Clase:
  def metodo(self,arg1,arg2):
    return 'Metodo normal',self

'Y como sabemos una vez creado un objeto puede ser llamado'
mi_clase = Clase()
mi_clase.metodo('a','b')
#('Metodo normal',<__main__.Clase atx43s2>)

'''En vista a esto los metodos de instancia pueden:

*Acceder y modificar los atributos del objeto.
*Pueden accder a otros metodos.
*Dado que desde el objeto < self > se puede accder a la clase con 'slef.clas' tambien se puede modificar el
estado de la clase.'''

#-------------------------------------METODOS DE CLASE-------------------------------#
'''A diferencia de los metodos de instancia, los metodos de clase reciben como argumento < cls >, que hace
referencia  la clase, por lo tanto pueden acceder a la clase pero no a la instancia'''

class Clase:
  @classmethod
  def metodoclase(cls):
    return 'Metodo de clase',cls
  
#Se pueden llamar sobre la clase
Clase.metodoclase()
#('Metodo de clase',__main__.Clase)

'''Por lo tanto los metodos de clase:
*No pueden acceder a los atributos de la instancia.
*Pero si pueden modificar los atributos de la clase.'''