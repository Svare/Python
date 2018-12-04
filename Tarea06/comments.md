# Instalacion de tor

	Al momento de intentar instalar tor se encontraron complicaciones
	al intentar ejecutar los comandos:

	# gpg2 --recv A3CAF0...
	# gpg2 --export A3CAF0... | apt-key add -

	El segundo comando no se ejecutaba correctamente asi que se ejecutaron
	los siguientes comandos:

	# sudo apt remove gnupg
	# sudo apt install --reinstall gnupg2
	# sudo apt install dirmngr

	Posteriormente se volvieron a ejecutar los comandos gpg2 pero esta vez
	en una terminal como superusuario y esto soluciono el problema.

	( Tal vez el problema siempre fue que se tenian que ejecutar desde terminal
	  como superusuario )

# Modulos requeridos

	Para que el programa funcione correctamente se deben instalar los modulos requests y pysocks
	
	# pip install requests
	# pip install pysocks
 

	
