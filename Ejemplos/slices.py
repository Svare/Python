#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

lista1 = ['Juan','Pedro','Jose','Fernando','Diego']
print '_'*50
print 'lista1 = %s' % lista1
print 'lista1[inicio:final:salto]'

print '_'*50
print '\nAcceder a un unico valor\n'
print 'lista1[0] -> %s' % lista1[0]
print 'lista1[1] -> %s' % lista1[1]
print 'lista1[2] -> %s' % lista1[2]
print 'lista1[-1] -> %s' % lista1[-1]
print 'lista1[-2] -> %s' % lista1[-2]

print '_'*50
print '\nAcceder a un rango de valores\n'
print 'lista1[0:2] -> %s' % lista1[0:2]
print 'lista1[:2] -> %s' % lista1[:2]
print 'lista1[2:] -> %s' % lista1[2:]
print 'lista1[1:2] -> %s' % lista1[1:2]
print 'lista1[1:3] -> %s' % lista1[1:3]
print 'lista1[:-2] -> %s' % lista1[:-2]
print 'lista1[:] -> %s' % lista1[:]

print '_'*50
print '\nAcceder a un rango de valores usando saltos\n'
print 'lista1[::1] -> %s' % lista1[::1]
print 'lista1[::2] -> %s' % lista1[::2]
print 'lista1[:4:2] -> %s' % lista1[:4:2]
print 'lista1[1::2] -> %s' % lista1[1::2]
print 'lista1[4:0:-1] -> %s' % lista1[4:0:-1]
print 'lista1[::-1] -> %s' % lista1[::-1]

print '_'*50
print '\nSlices en cadenas\n'
cadena1 = 'Becarios UNAM-CERT'
print 'cadena1 = "%s"\n' % cadena1
print 'cadena1[-1] -> %s' % cadena1[-1]
print 'cadena1[:5] -> %s' % cadena1[:5]
print 'cadena1[::3] -> %s' % cadena1[::3]
