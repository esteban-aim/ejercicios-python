def main():
    print("inserte un numero")
    numero1 = int(input())
    print("Inserta el segundo numero")
    numero2 = int(input())
    print("inserta el tercer numero")
    numero3 = int(input())
    print("inserta el cuarto numero")
    numero4 = int(input())
    suma = numero1 + numero2 + numero3 + numero4
    print("la suma es: " + str(suma))
    resta = numero1 - numero2 - numero3 - numero4
    print("la resta es: " + str(resta))
    multi = numero1 * numero2 * numero3 * numero4
    print("la multiplicacion es: " + str(multi))
    division = numero1 / numero2 / numero3 / numero4
    print("la division es : " + str(division))
    ensalada = ((numero1 + numero2) - numero3) * numero4
    print("la ensalada es: " + str(ensalada))


if __name__ == '__main__':
    main()
