#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

aprobados = []

def aprueba_becario(nombre_completo):
    nombre_separado = nombre_completo.lower()
    nombre_separado = nombre_completo.split()
    
    for n in nombre_separado:
        if n in ['manuel', 'valeria', 'alejandro', 'luis', 'enrique','omar','abraham','oscar']:
            return False
    aprobados.append(nombre_completo.upper())
    aprobados.sort()
    return True

def borrarBecario(nombre_completo):
    if aprobados.remove(nombre_completo.upper()):
        print 'True'
    else:
        print 'False'

becarios = ['Cervantes Varela JUAN MaNuEl',
            'Leal González IgnaciO',
            'Ortiz Velarde valeria',
            'Martínez Salazar LUIS ANTONIO',
            'Rodríguez Gallardo pedro alejandro',
            'Tadeo Guillén DiAnA GuAdAlUpE',
            'Ferrusca Ortiz jorge luis',
            'Juárez Méndez JeSiKa',
            'Pacheco Franco jesus ENRIQUE',
            'Vallejo Fernández RAFAEL alejanDrO',
            'López Fernández serVANDO MIGuel',
            'Hernández González ricaRDO OMAr',
            'Acevedo Gómez LAura patrICIA',
            'Manzano Cruz isaías AbrahaM',
            'Espinosa Curiel OscaR']
for b in becarios:
    if aprueba_becario(b):
        print 'APROBADOO: ' + b
    else:
        print 'REPROBADO: ' + b
        
print aprobados

borrarBecario("Acevedo Gómez LAura patrICIA")

print aprobados

#print becarios
