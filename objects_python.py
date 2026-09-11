'''La progamacion  orientada a objetos es un metodo que nos permite organiza el codigo de una manera
que se asemeje bastante a como pensamos en la vida real utlizando las famosas < clases >.

Estas nos permiten agrupar un conjunto de variables y funciones, cosas de lo mas cotidianas y simples
pueden  ser representadas mediante diferentes caracteristicas como en el caso de un perro su nombre,
edad,raza estas caracteristicas seran llamados < atributos >.

Por otro lado las clases tienen un conjunto de funcionalidades o cosas quue pueden hacer, en el caso
de un perro podria ser andar o ladrar, llamaremos a estas  funcionalidades < metodos >.

La programacion orientada a objetos esta basada en seis principios o pilares basicos
*Herencia
*Coesion
*Abstraccion
*Poliformismo
*Abstraccion
*Encapsulamiento

Este metono surgio debido a la creciente complejidad a la que los programadores se iban enfrentando,
uno delos primeros mecanismos que se crearon fueron las funciones que permiten arupar bleques de codigo
que relizan una tarea especifica bajo un nombre algo muy util ya que permite reutilizar modulos o funciones
sin tener que copiar todo el codigo.'''

#------------------------------DEFINIENDO CLASES-----------------------------#

#Lo primero es crear una clase utilizaremos como ejemplo un perro
class Perro:
    pass

'''Este ejemplo se trata de una clase vacia y sin mucha utilidad practica pero es la base minima de una clase,
en este ejemplo el uso de < pass > se utiliza debido a que en el caso de no contener nada en nuestra clase
enviara un error en su implementacion.
Ahora que temos una clase podemos crear un objeto,podemos hacerlo como si de una variable normal tratara.
Nombre de la variable es igual a la clase agrenado () dentro de los cuales iran los parametros de entrada
en el caso necesario '''

#Creamos un obejeto de la clase perro
mi_perro = perro()

#-------------------------------DEFIENIENDO ATRIBUTOS----------------------------#

'''Existen dos tipos de otributo.
*Atributos de instancia: Son atributos particulares de cada objeto en este caso nuestro perro.
*Atributos de clase: Se trata de atributos que pertenecen a la clase, por lo tanto seran comunes para
todos los obbjetos.
Eempecemos creando atributos de instancia para nuestro perro pueden ser el nombre y la raza. para eyo creamos
un metodo __init__ que sera llamado automaticamente cuando creemos un objeto. Se trata de el constructor.'''

class Perro:
    #El metodo __init__ es llamado al crear el objeto
    def __init__(self,nombre,raza):
       print(f'Creando perro {nombre,raza}')

       #Atributos de instancia 
       self. nombre =  nombre
       self. raza  = raza

'''Ahora que hemos definido el metodo __init__ con dos parametros de entrada podemos crear el objeto pasando
el valor de los atributos, usando < type() > podemos ver que el objeto es d la clase < Perro >.'''

mi_perro = Perro('Toby','Bulldog')
print(type(mi_perro))
#Creando perro,toby,bulldog
#< class__main__ .Perro >

'''Seguramente te ayas fijado que el < self > se pasa como parametro de entrada del metodo. Es una variable
que representa la instancia de la clase y debera estar siempre hay.
El uso de __init__ y el doble < __ > no es una coinsidencia, cunado veas un metodo con esa forama significa
qu esta reservado par aun uso especial en el lenguaje es enste caso seria el constructor.
Por ultimo podemos accder a los atributos utilizando el objeto y < . >'''

print (mi_perro.nombre) #Toby
print (mi_perro.raza) #Bulldog

'''Hasta ahora hemos definido atributos de insatancia ya que los atributos perenecen a cada perro en concreto.
Ahora vamos a definir un atributo clase, que sera comun para todos los perros por ejemplo la especie.'''

class Perro:
    #Atributo clase
    especie = 'Mamifero'

    #El metodo __init__ es llamado alcrear el objeto
    def __init__(self,nombre,raza):
       print(f'Creando perro {nombre} , {raza}')
       #Atributos de instancia
       self.nombre = nombre
       self.raza = raza

'''Dado que es un atributo de clase, no es necesario crear un objeto para acceder a los atributos, podemos hacer lo
siguiente.'''

print(Perro.especie)
#'Mamifero'

'''Tambien se puede acceder al atributo de la clase desde el objeto'''

mi_perro = Perro('Toby','Bulldog')
mi_perro.especie
#'Mamifero'

