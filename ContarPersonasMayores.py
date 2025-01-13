def main():
    total_adultos = 0
    total_menores = 0
    while True:
        try:
            ingresa = int(input("Ingresa la edad de la persona: "))
            edad = ingresa
            if edad >= 18:
                total_adultos += 1
            if edad <= 17:
                total_menores += 1
        except ValueError:
            print("Ingresa un numero valido.")

        print("El total de adultos que ingresaron hoy: ",total_adultos)
        print("El total de menores que ingresaron hoy: ",total_menores)

main()
