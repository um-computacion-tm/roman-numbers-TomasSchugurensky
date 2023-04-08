def decimal_to_roman(decimal):
    equivalentes = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    letras = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    resultado = ""
    i = 0
    while decimal > 0:
        if decimal - equivalentes[i] >= 0:
            resultado += letras[i]
            decimal -= equivalentes [i]
        else:
            i += 1
    return resultado
