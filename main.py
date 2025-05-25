import interfaces

"""
También se puede pasar el argumento 911, utilizado para ejecutar los test de
cada calculo de forma rapida. No es presentado al usuario dado que no es relevante para él.
"""
def iniciar_programa():
    while True:
        print("######################################################")
        print("\nOpciones:")
        print("1. Calcular tu IMC")
        print("2. Calcular tu porcentaje de grasa")
        print("3. Calcular tu consumo de calorías en reposo")
        print("4. Calcular tu consumo de calorías en actividad")
        print("5. Calcular las calorías recomendadas para adelgazar")
        print("######################################################")

        try:
            opcion = int(input("¿Qué opción querés elegir? Ingresá el número correspondiente: "))
            if opcion in [1, 2, 3, 4, 5, 911]:
                return opcion
            else:
                print("Opcion invalida. Elegi un numero entre 1 y 5.")
        except ValueError:
            print("Error. Ingresá un número válido.")

elegir = iniciar_programa()

if elegir == 1:
    print(interfaces.consola_calcular_IMC())
elif elegir == 2:
    print(interfaces.consola_calcular_porcentaje_grasa())
elif elegir == 3:
    print(interfaces.consola_calcular_calorias_en_reposo())
elif elegir == 4:
    print(interfaces.consola_calcular_calorias_en_actividad())
elif elegir == 5:
    print(interfaces.consola_consumo_calorias_recomendado_para_adelgazar())
elif elegir == 911:
    print(interfaces.consola_calcular_IMC(911))
    print(interfaces.consola_calcular_porcentaje_grasa(911))
    print(interfaces.consola_calcular_calorias_en_reposo(911))
    print(interfaces.consola_calcular_calorias_en_actividad(911))
    print(interfaces.consola_consumo_calorias_recomendado_para_adelgazar(911))


