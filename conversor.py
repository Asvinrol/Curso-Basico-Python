def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos " + tipo_pesos  +" tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) 
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares perrillo")
menu = """
Bienvenido al conversor de moendas mi loco 💸

1 - Pesos Colombianos Parce Gonorrea
2 - Pesos Argentinos Che Boludo
3 - Pesos Mexicanos Fierro Pariente

Eleige una opcion mi Loco: """

opcion = int(input(menu))

if opcion == 1:
    conversor("Colombianos", 4413.33)
elif opcion ==2:
    conversor("Argentinos", 138.57)
elif opcion ==3:
    conversor("Mexicanos", 20.18)
else:
    print("Ingresa una opcion correcta porfavor")


