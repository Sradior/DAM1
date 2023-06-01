'''
Programa calculadora
Oscar Barea Zahonero 2023

'''

print ("Bienvenido a tu calculadora")
print ("Introduce tu nombre por favor")

nombre = input()

print ("Hola,",nombre,"bienvenido a tu calculadora")
def calculadora ():
    print("Elije la operacion que quieres realizar"+
            "\n1.-Suma"+
            "\n2.-Resta"+
            "\n3.-Multiplicacion"+
            "\n4.-Division"
          )
    operacion = int(input())
    print("La operacion que has elegido es la", operacion)

    print ("Ahora introduce un numero")
    numero1 = int(input())

    print ("Ahora introduce otro numero")
    numero2 = int(input())

    if operacion == 1:
        print("El resultado es:",(numero1+numero2))

    if operacion == 2:
        print("El resultado es:",(numero1-numero2))

    if operacion == 3:
        print("El resultado es:",(numero1*numero2))

    if operacion == 4:
        print("El resultado es:",(numero1/numero2))

    calculadora() #todo esta sangrado con def calculadora, para que todo permanezca dentro de la funcion

calculadora() #al ejecturl doble calculadora () se hará en bucle en shell
