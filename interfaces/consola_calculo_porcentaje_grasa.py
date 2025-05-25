import calculos as calc
from .mensaje_consola import mensaje_consola

""""
Muestra por consola los inputs que son requeridos para calcular el porcentaje de 
grasa corporal.
Si se le pasa como el valor 00 como argumento, se ejecuta un test.
"""
def consola_calcular_porcentaje_grasa(test=True) -> float:
    if test == 00:
        print("\n######################################################")
        print("Test de consumo de porcentaje de grasa")
        test = calc.calcular_porcentaje_grasa(81, 175, 20, 1) 
        test2 = calc.calcular_porcentaje_grasa(58, 169, 21, 0) 
        print(f"\nTest porcentaje de grasa: {test}")##20.14
        print(f"Test2 porcentaje de grasa: {test2}")##23.8
        return "\n[TEST FINALIZADO]"
    respusta = mensaje_consola(2)
    peso = respusta[0]
    altura = respusta[1]
    edad = respusta[3]
    genero = respusta[4]

    resultado = calc.calcular_porcentaje_grasa(peso, altura, edad, genero)
    grasa_recomendada = calc.grasa_recomendada(edad, genero)
    return f"\nTu porcentaje de grasa corporal es: {resultado}. {grasa_recomendada}"

