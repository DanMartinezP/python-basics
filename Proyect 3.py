print("Ingrese numeros. Para finalizar ingrese OK")

acumulador = 0
counter = 0

while True:
    num = input("Ingrese numero: ")
    if num == "OK":
        break
    elif num.isdigit():
        acumulador = acumulador + int(num)
        counter = counter + 1
    else:
        print("Ingrese un numero o OK para finalizar")

print("Finalizando...")
if counter > 0:
    print("El promedio es: ", acumulador / counter)
else:
    print("No ingresaste ningún número.")