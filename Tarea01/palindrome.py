
# Jesus Enrique Pacheco Franco
# 27/Nov/2018


def is_palindrome(string):
    '''
        Parametros
            string [str]: Cadena de caracteres a evaluar
            
        Descripcion
            Verifica si la cadena string es un palindromo
            
        Return
            True : Si string es un palindromo
            False : Si string no es un palindromo
    '''
    return string == string[::-1]

def biggest_palindrome(string, palindromes):
    '''
        Parametros
            string [str]: Cadena de caracteres a evaluar
            palindromes [list]: Lista donde se van a almacenar todos los palindromos
                                encontrados, siempre se debe pasar como argumento
                                una lista vacia.
            
        Descripcion
            Encuentra el palindromo mas grande dentro de la cadena string
            
        Return
            str: El palindromo mas grande
    '''
    for i in range(1,len(string)+1):
        if is_palindrome(string[:i]):
            palindromes.append(string[:i])
    
    if len(string) > 1:
        biggest_palindrome(string[1:], palindromes)
    else:
        palindromes.append(string)
    
    sorted_palindromes = sorted(palindromes, key=lambda item: len(item))
    return sorted_palindromes[-1]
        
def main():
    
    string = raw_input("Dame la cadena a evaluar: ")
    print biggest_palindrome(string, [])
    
    
if __name__ == '__main__':
    main()
