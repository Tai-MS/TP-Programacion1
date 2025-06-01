"""
Calcula el indice de masa corporal (IMC) con el peso y la altura.
"""
def calcular_IMC(peso: float, altura: float) -> float:
    altura_m = altura / 100
    imc = round(peso / (altura_m * altura_m), 2)

    return imc


"""
Calcula el consumo de calorías en reposo (TMB) con el peso, la altura, la edad y el género.
El género es pasado como 0 para mujer y 1 para hombre, tomando un valor distinto para cada uno.
"""
def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, genero: int):
    if genero == 0:
       valor_genero = -161
    else:
         valor_genero = 5

    tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero
    return tmb


"""
Clasifica el IMC en distintas categorías.
"""
def clasificar_IMC(imc: float) -> str:
    if imc < 16:
        return "Delgadez severa"
    elif 16 <= imc <= 16.99:
        return "Delgadez moderada"
    elif 17 <= imc <= 18.49:
        return "Delgadez aceptable"
    elif 18.5 <= imc <= 24.99:
        return "Peso normal"
    elif 25 <= imc <= 29.99:
        return "Sobrepeso"
    elif 30 <= imc <= 34.99:
        return "Obesidad tipo I"
    elif 35 <= imc <= 39.99:
        return "Obesidad tipo II"
    elif 40 <= imc <= 49.99:
        return "Obesidad tipo III o mórbida"
    else:  # IMC > 50
        return "Obesidad tipo IV o extrema"


"""
Devuelve la grasa recomendada según la edad y el género.
"""
def grasa_recomendada(edad: int, genero: int):
    if genero == 0:
        if 20 <= edad and edad <= 29:
            return "Porcentaje de grasa ideal es entre 11% y 20%"
        elif 30 <= edad and edad <= 39:
            return "Porcentaje de grasa ideal es entre 12% y 21%"
        elif 40 <= edad and edad <= 49:
            return "Porcentaje de grasa ideal es entre 14% y 23%"
        elif 50 <= edad and edad <= 59:
            return "Porcentaje de grasa ideal es entre 15% y 24%"
    else:
        if 20 <= edad and edad <= 29:
            return "Porcentaje de grasa ideal es entre 16% y 28%"
        elif 30 <= edad and edad <= 39:
            return "Porcentaje de grasa ideal es entre 17% y 29%"
        elif 40 <= edad and edad <= 49:
            return "Porcentaje de grasa ideal es entre 18% y 30%"
        elif 50 <= edad and edad <= 59:
            return "Porcentaje de grasa ideal es entre 19% y 31%"


"""
Calcula el porcentaje de grasa corporal utilizando la altura, peso, edad y genero.
El género es pasado como 0 para mujer y 1 para hombre, tomando un valor distinto para cada uno.
"""    
def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, genero:int) -> float:
    imc = calcular_IMC(peso, altura)

    if genero == 0:
       valor_genero = 0
    else:
        valor_genero = 10.8 

    resultado = round(1.2 * imc + 0.23 * edad - 5.4 - valor_genero, 2)
    
    return resultado


"""
Calcula el consumo de calorías en actividad con el peso, la altura, la edad, el género y la actividad.
El género es pasado como 0 para mujer y 1 para hombre, tomando un valor distinto para cada uno.
La actividad es un número entre 1 y 5, donde 1 es poco o ningún ejercicio y 5 es atleta. Dependiendo de la actividad, 
se multiplica el TMB por un valor diferente.
"""
def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero:float, valor_actividad: float) -> float:
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)

    if valor_actividad == 1:
        valor_actividad = 1.2
    elif valor_actividad == 2:
        valor_actividad = 1.375
    elif valor_actividad == 3:
        valor_actividad = 1.55
    elif valor_actividad == 4:
        valor_actividad = 1.725
    elif valor_actividad == 5:
        valor_actividad = 1.9

    tmb_en_actividad = round(tmb * valor_actividad, 2)
    
    return tmb_en_actividad


"""
Calcula el consumo de calorías recomendado para adelgazar con el peso, la altura, la edad y el género.
El género es pasado como 0 para mujer y 1 para hombre, tomando un valor distinto para cada uno.
El resultado que devuelve es un array que representa el rango de calorías recomendadas para adelgazar entre el minimo y el maximo.
"""
def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero:float) -> float:
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    
    resultado1 = round(tmb * 0.8, 2)  
    resultado2 = round(tmb * 0.85, 2)  
    margen = [resultado1, resultado2]
    return margen
