def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3)/3
    return promedio 
nota1 = float(input("Ingrese la primera nota"))
nota2 = float(input("Ingrese la segunda nota"))
nota3 = float(input("Ingrese la tercera nota"))
promedio = calcular_promedio(nota1, nota2, nota3)
print("El promedio de las tres notas es: ", promedio)