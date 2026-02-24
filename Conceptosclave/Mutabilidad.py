

#////////////////////////////////Mutuables//////////////////////////////////////////////////////////////////////////////////

#La mutabilidad es la capacidad de un objeto para cambiar su contenido sin cambiar su identidad.
#Para verificar que un objeto tiene la capasidad de cambiar su contenido lo aremos observando las ID de estos 
#Las ID son unicas y existen mientras el objeto este creado.

#Mutuables
x = 5 #ID 140726664250408
print("ID de x=5: ", id(x))
x = 8 #ID 140726664250504
print("ID de x=8: ", id(x))
#En este caso tenemos dos ID que son diferentes ya que estas variables apuntan o contienen valores diferentes

lista1 = [1, 2, 3, 4]
lista2 = lista1 

print("ID de lista 1: ",id(lista1), "\n" "ID de lista 2: ", id(lista2))

#En este caso las ID son iguales ya que las dos variables apuntan al mismo valor. 
#OJOOO: las listas cambian de ID cada que el codigo se ejecuta por que se libera la memoria.

#Lista              0             1          2          3          Total de 4 elemntos en la lista 
listaDeFrutas = ["Manzana ", "Mandarina", "Mango", "mazadinango"]

print(listaDeFrutas, "ID de la lista de frutas: ", id(listaDeFrutas))

listaDeFrutas.append("chayote")

print(listaDeFrutas, "ID de lista frutas mudificada: ", id(listaDeFrutas))


#Como podemos observar los objetos son los mismos y tienen la capacidad de cambiar


#///////////////////////////////////////////Inmutuables///////////////////////////////////////////////////////////////////////


#las tuplas son imutuables es decir no se puden cambiar, borrar o agregar valores 


tupla1 = (1, 2, 3)


print(type(tupla1))
print(tupla1)

#tupla1.append NO existe pero hay una forma de agregar o modificar cosas de una lista 

tupla2 = ("cocodrilo", "jaguar", "jaguardrilo")
print(tupla2, type(tupla2))

listaDetupla = list(tupla2)
print(listaDetupla, type(listaDetupla))


listaDetupla.append("michi")
print(listaDetupla)

tupla2 = tuple(listaDetupla)
print(tupla2, type(tupla2))


#y tambien se pueden sumar tuplas.

tupla3 = tupla1 + tupla2
print(tupla3, type(tupla3))

