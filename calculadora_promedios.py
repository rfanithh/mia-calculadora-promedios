def main():
    # 1. Pedir materias y calificaciones al usuario. 
    materias, calificaciones = ingresar_calificaciones()  #Realizado 20261022_1745

    # 2. Calcular el promedio general
    promedio = calcular_promedio(calificaciones)  #Realizado 20261022_1758

    # 3. Determinar aprobadas y reprobadas
    aprobadas, reprobadas = determinar_estado(materias, calificaciones)  #Realizado 20261022_1837. Y fin de esta seccion. Actualizado 20261028_1557
    
    # 4. Encontrar la mejor y peor calificación
    indice_peor, indice_mejor = encontrar_extremos(calificaciones) #Realizado 20261024_1039


    # 5. Mostrar el resumen final
    if len(materias) > 0:  # Evita que se muestre el resumen si no se ingresaron materias. 
        print("\nResumen final\n")
        print("\nLista de materias y calificaciones:")
        for m, c in zip(materias, calificaciones):  # Usamos zip para recorrer las listas de materias y calificaciones al mismo tiempo. Realizado 20261028_1557
            print( f"  {m}: {c}") 
        print("\nPromedio general:", promedio) 
        print("\nAprobadas:", aprobadas, "Reprobadas:", reprobadas)
        indice_mejor, indice_peor = encontrar_extremos(calificaciones)

        print("\nMejor materia y calificación:", materias[indice_mejor], calificaciones[indice_mejor])
        print("\nPeor materia y calificación:", materias[indice_peor], calificaciones[indice_peor])

    else:
        print("\nNo se ingresaron materias.")
            
# 6. Mensaje de despedida

    print("\nGracias por usar la calculadora de promedios. ¡Hasta luego!\n")

# Inicio de la calculadora de promedios
# 1.  Pedir materias y calificaciones al usuario
def ingresar_calificaciones():
    materias = []    #lista para almacenar las materias
    calificaciones = []   #lista para almacenar las calificaciones
    print("Ingrese las materias y calificaciones del alumno. Escriba 'fin' para terminar.") #Un mensajito para que el usuario sepa que hacer
        
    while True:
        materia = input("Materia: ")   # Solicitamos al usuario que ingrese la materia y almacenamos en la lista materia.
        if materia.lower() == "fin":   # Si materia luego de convertirlo a minuscula es igual a "fin", entonces se rompe el ciclo.
            break
        else:
            if materia == "":   # Si el usuario no ingresa nada, se le indica que ingrese un valor valido.
                print("Materia inválida. Debe ingresar un valor o fin para terminar.")
                continue   # Con continue, hacemos que el ciclo vuelva a empezar, sin ejecutar el resto del codigo.
        while True:
            try: # Agregado 20261028_1617 , para cuando el usuario ingrese un string en vez de un float. 
                calificacion = float(input("Calificacion entre 0 y 10: "))   #Aqui es necesario convertir a float o int, ya que input devuelve un string y necesitamos un num p/ poder hacer operaciones mat.    
                if calificacion < 0 or calificacion > 10:   #Si la calificacion es menor a 0 o mayor a 10, entonces se le indica al usuario que ingrese un valor valido.
                    print("Calificación inválida. Debe estar entre 0 y 10.")
                else:
                    break   #Con continue, hacemos que el ciclo vuelva a empezar, sin ejecutar el resto del codigo.
            except ValueError: # Agregado 20261028_1617
                print("Entrada inválida. Debe ingresar un número entre 0 y 10.")
            
        calificaciones.append(calificacion)   #Con append agregamos la calificacion a la lista calificaciones.
        materias.append(materia)
    return materias, calificaciones  # Para no perder los datos, retornamos la lista de materias y calificaciones.

# 2. Calcular el promedio general

def calcular_promedio(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones.
    Devuelve None si la lista está vacía.
    """
    if len(calificaciones) > 0:
         return (sum(calificaciones)/len(calificaciones))
    else:
        return None

# 3. Determinar aprobadas y reprobadas

def determinar_estado(materia, calificaciones, umbral= 5.0):
    aprobados = []
    reprobados = []
    for i in range(len(calificaciones)):
        if calificaciones[i] >= umbral:
            aprobados.append(materia[i])
        else:
            reprobados.append(materia[i])
    return aprobados, reprobados

# 4. Encontrar la mejor y peor calificación

def encontrar_extremos (calificaciones):
    if len(calificaciones) == 0 :
        return None, None
    indice_mejor = calificaciones.index(max(calificaciones))
    indice_peor = calificaciones.index(min(calificaciones))
    return indice_mejor, indice_peor

"""
CODIGO VIEJO, SE REMPLAZA POR:

El evaluador dice que debe recibir solo las calificaciones y devolver los índices extremos, en lugar de recibir materias y calificaciones y devolver tuplas de nombre+nota.

def encontrar_extremos(materias: list[str], calificaciones: list[float]) -> tuple[tuple[str, float], tuple[str, float]]:  # Usando type hints
    if len(materias) == 0 or len(calificaciones) == 0:
        return (None, None), (None, None)
    
    mejor_calificacion = calificaciones[0]  # Se toma la calificacion en posicion 0 como la mejor calificacion inicial.
    mejor_materia = materias[0] # Se toma la materia en posicion 0 como la mejor materia inicial.
    peor_calificacion = calificaciones[0] # Se toma la calificacion en posicion 0 como la peor calificacion inicial.
    peor_materia = materias[0] # Se toma la materia en posicion 0 como la peor materia inicial.

    for i in range(len(calificaciones)): # En una primera pasada, la primera calificacion es la mejor y la peor, pero en las siguientes pasadas, se comparan las calificaciones con la mejor y peor calificacion actual.
        if calificaciones[i] > mejor_calificacion:
            mejor_calificacion = calificaciones[i]
            mejor_materia = materias[i]
        elif calificaciones[i] < peor_calificacion:
            peor_calificacion = calificaciones[i]
            peor_materia = materias[i]

    mejor_materia_calificacion = (mejor_materia, mejor_calificacion) # Se pasa el resultado como tupla, para que sea mas facil de manejar y mostrar en pantalla.
    peor_materia_calificacion = (peor_materia, peor_calificacion)

    return mejor_materia_calificacion, peor_materia_calificacion
"""

if __name__ == "__main__":  # Esta vaina se me va a olvidar siempre, mejor creo un template que lo tenga siempre.
    main()
