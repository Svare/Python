
# Jesus Enrique Pacheco Franco
# 27/Nov/2018

def is_prime(number):
    '''
        Parametros
            number [int]: Numero a evaluar
            
        Descripcion
            Verifica si el numero number es primo
            
        Return
            True : Si number es primo
            False : Si number no es primo
    '''
    dividers = 0
    for i in range(1,number+1):
        if number % i == 0:
            dividers+=1
    return dividers==2

def n_first_prime_numbers(how_many, prime_numbers, number):
    '''
        Parametros
            how_many [int]: Cantidad de numeros primos a calcular
            prime_numbers [list]: Lista donde vamos almacenar todos los numeros
                                    primos, se debe proporcionar una lista vacia
            number [int]: Entero que vamos a usar como contador para ir obteniendo
                            numeros primos a travez de validaciones
            
        Descripcion
            Obtiene los primeros how_many numeros primos
            
        Return
            prime_numbers: Lista que contiene los numeros primos calculados
    '''
    if how_many != 0:
        if is_prime(number):
            prime_numbers.append(number)
            n_first_prime_numbers(how_many-1, prime_numbers, number+1)
        else:
            n_first_prime_numbers(how_many, prime_numbers, number+1)
    return prime_numbers
            
def main():
    
    import sys
    sys.setrecursionlimit(10000)
    
    how_many = int(raw_input("Cuantos numeros primos quieres? "))
    prime_numbers = n_first_prime_numbers(how_many, [], 0)
    print prime_numbers

if __name__ == '__main__':
    main()
    
