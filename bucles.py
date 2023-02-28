#contador = 0
#print("2 elevado a " + str(contador) + " Es igual a: " + str(2**contador))

#contador = 1
#print("2 elevado a " + str(contador) + " Es igual a: " + str(2**contador))

from re import L
from sqlite3 import complete_statement


def run():
    LIMITE = 1000000

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print("2 elevado a " + str(contador) + " Es igual a: " + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador


if __name__ == '__main__':
    run( )