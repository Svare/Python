
# Jesus Enrique Pacheco Franco
# 27/Nov/2018

from random import choice, random

def password(length, pswd, characters):
    '''
        Parametros
            length [int]: Longitud de la contrasena
            pswd [list]: Lista donde se almacenaran todos los caracteres
                            que conformaran la contrasena
            characters [list]: Lista que contiene los caracteres que se utilizaran para
                                generar la contrasena
            
        Descripcion
            Genera una contrasena de una longitud dada
            
        Return
            str_pass [str]: Contrasena
    '''
    if length != 0:
        pswd.append(choice(characters))
        password(length-1, pswd, characters)
    
    str_pass = ""
    
    for c in pswd:
            str_pass += c
        
    return str_pass

def main():
    
    characters = ['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','#','$','&','@']
    
    #length = int(raw_input("Longitud de contrasena: "))
    print password(15, [], characters)
        
if __name__ == '__main__':
    main()
