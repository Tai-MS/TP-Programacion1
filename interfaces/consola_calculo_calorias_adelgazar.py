import calculos as calc
from .mensaje_consola import mensaje_consola

""""
Muestra por consola los inputs que son requeridos para calcular el rango de 
calorias que hay que consumir para adelgazar.
Si se le pasa como el valor 00 como argumento, se ejecuta un test
"""
def consola_consumo_calorias_recomendado_para_adelgazar(test=True):
    if test== 911:
        print("\n######################################################")
        print("Test de consumo de calorías recomendado para adelgazar")
        test = calc.consumo_calorias_recomendado_para_adelgazar(81, 175, 20, 1)
        test2 = calc.consumo_calorias_recomendado_para_adelgazar(58, 169, 21, 0)
        print(f"\nTest calorias para adelgazar: {test}")
        print(f"Test2 calorias para adelgazar: {test2}")
        return "\n[TEST FINALIZADO]"
    respusta = mensaje_consola(2)
    peso = respusta[0]
    altura = respusta[1]
    edad = respusta[3]
    genero = respusta[4]
    
    resultado = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, genero)

    return f"\nTu consumo de calorías recomendado para adelgazar es: entre {resultado[0]} calorias y {resultado[1]} calorias."