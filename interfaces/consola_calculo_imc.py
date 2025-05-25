import calculos as calc
from .mensaje_consola import mensaje_consola

""""
Muestra por consola los inputs que son requeridos para calcular el IMC.
Si se le pasa como el valor 00 como argumento, se ejecuta un test
"""
def consola_calcular_IMC(test=True):
    if test == 911:
        print("\n######################################################")
        print("Test de calculo de IMC")
        test = calc.calcular_IMC(81, 175)
        test2 = calc.calcular_IMC(58, 169)
        print(f"\nTest IMC: {test}") ##26.45
        print(f"Test2 IMC: {test2}") ##20.31
        return "\n[TEST FINALIZADO]"
    respusta = mensaje_consola(1)
    peso = respusta[0]
    altura = respusta[1]

    resultado_IMC = calc.calcular_IMC(peso, altura)
    resultado_clasif = calc.clasificar_IMC(resultado_IMC)
    return f"\nTu IMC es: {resultado_IMC}. Tu clasificación es: {resultado_clasif}."

