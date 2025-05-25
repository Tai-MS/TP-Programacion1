import calculos as calc
from .mensaje_consola import mensaje_consola


""""
Muestra por consola los inputs que son requeridos para calcular el
consumo de calorias estando en actividad.
Si se le pasa como el valor 00 como argumento, se ejecuta un test
"""
def consola_calcular_calorias_en_actividad(test=True):
    if test == 00:
        print("\n######################################################")
        print("Test de consumo de calorías en actividad")
        test = calc.calcular_calorias_en_actividad(81, 175, 20, 1, 3)##2803.56
        test2 = calc.calcular_calorias_en_actividad(58, 169, 21, 0, 4)##2363.68
        print(f"\nTest calorias en actividad: {test}")
        print(f"Test2 calorias en actividad: {test2}")
        return "\n[TEST FINALIZADO]"
    respusta = mensaje_consola(3)
    peso = respusta[0]
    altura = respusta[1]
    edad = respusta[3]
    genero = respusta[4]
    actividad = respusta[2]
    
    resultado = calc.calcular_calorias_en_actividad(peso, altura, edad, genero, actividad)  



    return f"\nTu consumo de calorías en actividad es: {resultado}."
