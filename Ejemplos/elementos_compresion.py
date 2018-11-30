
# Listas por compresion

l1 = [n**3 for n in range(1,31,2)]
print l1


l2 = ['hola','como','estas']
l2 = [(s.upper(),s.lower(),len(s)) for s in l2]
print l2

from random import randint

l3 = ['jesus','servando','rafa']

l3 = {s:randint(0,10) for s in l3}
print l3

# Diccionario con los primeros 50 numeros odiosos

dictionary = {num:(bin(num), hex(num)) for num in range(51) if bin(num).count('1') % 2 != 0}
print dictionary



