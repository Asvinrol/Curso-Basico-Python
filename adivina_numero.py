import random


def run():
    numero_random = random.randint(1,100) 
    numero_elegido = int(input("Elige un numero del 1 al 100 Perrillo: "))
    while numero_elegido != numero_random:
        if numero_elegido < numero_random:
            print("Busca un número más grande wey")
        else:
            print("Busca un número más pequeño cabron")
        numero_elegido = int(input("Elige otro número: "))
    print("Ganaste Lokho")

if __name__ == '__main__':
    run()