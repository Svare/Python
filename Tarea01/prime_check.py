
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

def main():
    number = int(raw_input("Numero a verificar: "))
    print is_prime(number)

if __name__ == '__main__':
    main()
