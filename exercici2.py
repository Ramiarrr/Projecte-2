
num1 = int(input("Introdueix el primer nombre enter: "))
num2 = int(input("Introdueix el segon nombre enter: "))
suma = num1 + num2
resta = num1 - num2
multiplicacio = num1 * num2
print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicacio es:", multiplicacio)
if num2 != 0:
    divisio = num1 / num2
    print("La divisio es:", divisio)
else:
    print("No es pot dividir entre zero.")