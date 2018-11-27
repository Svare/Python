#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

lista1 = [1,2,3,4,3,4]
print 'lista1 = %s' % lista1
print '_'*50
print 'Operaciones y funciones que no afectan a la lista original\n'
print 'Regresa el valor maximo de la lista'
print 'max(lista1) -> %s\n' % max(lista1)

print 'Regresa el valor minimo de la lista'
print 'min(lista1) -> %s\n' % min(lista1)

print 'Regresa la cantidad de elementos en la lista'
print 'len(lista1) -> %s\n' % len(lista1)

print 'Multiplica una lista n veces'
print 'lista1*2 -> %s\n' % (lista1*2)

print 'Regresa una lista con los elementos de ambas listas'
print 'lista1 + [6,7,8] -> %s\n' % (lista1 + [6,7,8])

print 'Indica cuantas veces aparece cierto elemento'
print 'lista1.count(3) -> %s\n' % lista1.count(3)

print 'Indica el indice de la primer coincidencia de un elemento'
print 'lista1.index(2) -> %s\n' % lista1.index(2)

print '_'*50
print 'Operaciones y funciones que si afectan a la lista original\n'

print 'Agrega un elemento al final de la lista'
lista1.append(10)
print 'lista1.append(10) -> %s\n' % lista1

print 'Inserta un elemento en el indice especificado'
lista1.insert(5,100)
print 'lista1.insert(5,100) -> %s\n' % lista1

print 'Elimina de la lista el elemento del indice especificado'
lista1.pop(4)
print 'lista1.pop(4) -> %s\n' % lista1

print 'Elimina de la lista el elemento especificado'
lista1.remove(4)
print 'lista1.remove(4) -> %s\n' % lista1

print 'Ordena una lista'
lista1.sort()
print 'lista1.sort() -> %s\n' % lista1

print 'Reacomoda una lista en el orden inverso'
lista1.reverse()
print 'lista1.reverse() -> %s\n' % lista1


