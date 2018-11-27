#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

#TUPLAS
print '_'*40 + '\nTUPLAS\n' + '_'*40

tupla1 = 1,2,3,4,5
print '\ntupla1' 
print tupla1

tupla2 = (6,7,8,9)
print '\ntupla2'
print tupla2

print '\ntupla1[0]' 
print tupla1[0]

print '\ntupla1[2:]'
print tupla1[2:]

print '\nmax(tupla1)' 
print max(tupla1)

print '\nmin(tupla2)' 
print min(tupla2)

print '\nlen(tupla1+tupla2)' 
print len(tupla1+tupla2)

print '\nlist(tupla1)'
print list(tupla1)
#tupla1.append(100) #ERROR
#tupla2.remove(9)   #ERROR


#Conjuntos
print '_'*40 + '\nCONJUNTOS\n' + '_'*40

set1 = {1,2,3,4,5,6}
print '\nset1' 
print set1

set2 = {4,5,6,7,8,9}
print '\nset2'
print set2

print '\nlen(set1)' 
print len(set1)

print '\nset1|set2'
print set1|set2

print '\nset1-set2' 
print set1-set2

print '\nset1&set2' 
print set1&set2

print '\nset1^set2' 
print set1^set2

print '\nset1.add(100)'
set1.add(100)
print set1

print '\nset1.update([100,200,300])'
set1.update([100,200,300])
print set1

print '\nset1.remove(100)'
#Genera un error si no tiene al elemento que intenta quitar
set1.remove(100)
print set1

print '\nset1.discard(200)'
#NO genera errores si no tiene al elemento que intenta quitar
set1.discard(200)
print set1

#Diccionarios
print '_'*40 + '\nDiccionarios\n' + '_'*40

dic1 = {'Pedro':10,'Juan':9,'Diego':5}
print '\ndic1' 
print dic1

dic2 = {'Leticia':9,'Lorena':7,'Mariela':10}
print '\ndic2'
print dic2

print '\nlen(dic1)' 
print len(dic1)

print '\ndic1.update(dic2)'
dic1.update(dic2)
print dic1

print '\ndic1[\'Carlos\'] = 0'
dic1['Carlos'] = 0
print dic1

print '\ndic1[\'Carlos\'] = 6'
dic1['Carlos'] = 6
print dic1

print '\ndic1[\'Juan\']'
print dic1['Juan']

print '\ndic1.keys()'
print dic1.keys()

print '\ndic1.values()'
print dic1.values()

print '\ndic1.pop(\'Carlos\')'
dic1.pop('Carlos')
print dic1
