import calculos as calc
from .mensaje_consola import mensaje_consola

""""
Muestra por consola los inputs que son requeridos para calcular el 
consumo de calorias estando en reposo.
Si se le pasa como el valor 00 como argumento, se ejecuta un test
"""
def consola_calcular_calorias_en_reposo(test=True):
    if test == 911:
        print("\n######################################################")
        print("Test de consumo de calorías en reposo")
        test = calc.calcular_calorias_en_reposo(81, 175, 20, 1)
        test2 = calc.calcular_calorias_en_reposo(58, 169, 21, 0)
        print(f"\nTest calorias en reposo: {test}")##1808.75
        print(f"Test2 calorias en reposo: {test2}")##1370.25
        return "\n[TEST FINALIZADO]"
    respusta = mensaje_consola(2)
    peso = respusta[0]
    altura = respusta[1]
    edad = respusta[3]
    genero = respusta[4]

    resultado = calc.calcular_calorias_en_reposo(peso, altura, edad, genero)

    

    return f"\nTu porcentaje de grasa corporal es: {resultado}."
