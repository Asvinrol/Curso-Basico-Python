def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    #print(mi_diccionario ['llave1'])
    #print(mi_diccionario ['llave2'])
    #print(mi_diccionario ['llave3'])

    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }

    #for pais in poblacion_paises.keys(): ## .keys muestra el nombre de las llaves
    #    print(pais)

    #for pais in poblacion_paises.values(): ## .Values muestra el valor de las llaves
    #    print(pais)

    for pais, poblacion in poblacion_paises.items():##.items muestra tanto el nombre como el valor de las llaves
        print(pais + "tiene " + str(poblacion) + " habitantes")



if __name__ == '__main__':
    run()