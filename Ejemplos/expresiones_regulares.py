
from re import search

patron = r"(([a-z]*)([^:]+))(:)"
coincidencia = search(patron, "becario123:qwersdfqwrevd:sdfasfasdf")


print coincidencia.group(0)
print coincidencia.group(1)
print coincidencia.group(2)
print coincidencia.group(3)
print coincidencia.group(4)

''' 4 mayusculas o minusculas, seguidas de 4 digitos'''

	# [a-zA-Z]{4}[0-9]{4}

''' Cualquier caracter excepto '$' una o mas veces, seguido de '$' '''

	# [^$]+\$

''' Los comentarios multilinea en lenguje C '''

	# [/][*][.\n]*[*][/]

''' Un posible nombre de variable en Python '''

	# [a-zA-Z_][a-zA-Z0-9_]*


ipv4 = r'[0]'