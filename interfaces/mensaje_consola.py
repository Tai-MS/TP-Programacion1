"""
FUNCIONA ENCARGADA DE MOSTRAR LOS MENSAJES EN CONSOLA PARA LOS INPUTS NECESARIOS
PARA CADA CALCULO
"""
def mensaje_consola(opcion: int):
    actividad = 0
    edad = 0
    genero = 0
    print("######################################################")
    peso = float(input("\nIngresa el peso en kilogramos (ejemplo: 70.75): "))
    print("######################################################")

    altura = float(input("\nIngresa tu altura en centimetros (ejemplo: 172): "))
    print("######################################################")
    if opcion == 2 or opcion == 3 or opcion == 4:
        edad = int(input("\nIngresa tu edad: "))
        print("######################################################")

        genero = int(input("\nIngresa tu genero ([1] para hombre, [0] para mujer): "))
        print("######################################################")
        
    
    if opcion == 3:
        print("Para calcular las calorías en actividad, se necesita el valor de tu actividad.")
        print("\nOpciones de actividad:")
        print("[1] poco o ningún ejercicio")
        print("[2] ejercicio ligero (1 a 3 días a la semana)")
        print("[3] ejercicio moderado (3 a 5 días a la semana)")
        print("[4] deportista (6 -7 días a la semana)")
        print("[5] atleta (entrenamientos mañana y tarde)")
        actividad = float(input("\nIngresa tu actividad: "))
        print("######################################################")
    return peso, altura, actividad, edad, genero
