from pickletools import read_string1
import random

def generar_passwrd():
    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simb = ['!', '#', '$', '&', '/', '(', ')']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayus + minus + simb + numeros

    contra = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contra.append(caracter_random)
        
    contra = "".join(contra)    
    return contra
def run():
    contra = generar_passwrd()
    print("Tu nuve contraseña es: " + contra )



if __name__ == '__main__':
    run()