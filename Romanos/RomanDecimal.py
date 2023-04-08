def RomanToDecimal (roman):
    diccionario = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    decimal = 0
    numero_previo= 0

    for letter in roman:
        numero = diccionario[letter]
        if numero > numero_previo:
            decimal -= 2 * numero_previo
        decimal += numero
        numero_previo = numero

    return decimal