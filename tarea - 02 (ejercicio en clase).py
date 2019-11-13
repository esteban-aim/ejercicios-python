def main():
    print("cual es tu nombre")
    nombre1 = input()
    print("cual es tu segundo nombre")
    nombre2 = input()
    print("cual es tu primer apellido")
    apellido1 = input()
    print("cual es tu segundo apellido")
    apellido2 = input()
    print("buenos dias: " + nombre1 + " " + nombre2 + " " + apellido1 + " " + apellido2)
    print("buenos días: %s %s %s %s" % (nombre1, nombre2, apellido1, apellido2))


if __name__ == '__main__':
    main()
