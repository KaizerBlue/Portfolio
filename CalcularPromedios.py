def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

def aprueba_desaprueba(promedio):
    if promedio >= 7:
        return True
    else:
        return False

def main():
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))

    promedio = calcular_promedio(nota1, nota2, nota3)

    if aprueba_desaprueba(promedio):
        print("El alumno aprueba con un promedio de",promedio)
    else:
        print("El alumno desaprueba con un promedio de",promedio)
main()