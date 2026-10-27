# Actividad — Calculadora de promedios

**Descripción general:**
Desarrollo de una calculadora de promedios escolares en Python utilizando variables, operadores, estructuras de control y funciones básicas.

---

## Instrucciones

Crea un nuevo archivo Python llamado `calculadora_promedios.py` que contendrá todo el código de tu programa.

### 1. Función `ingresar_calificaciones()`

- [x] Hecho. 

Implementa una función llamada `ingresar_calificaciones()` que permita al usuario introducir el nombre de una materia y su calificación correspondiente. Esta función debe:

- Solicitar al usuario que ingrese el nombre de la materia
- Solicitar la calificación (validando que sea un número entre 0 y 10)
- Almacenar ambos datos en dos listas separadas (una para nombres y otra para calificaciones)
- Preguntar si desea continuar ingresando más materias
- Retornar ambas listas cuando el usuario decida terminar

### 2. Función `calcular_promedio(calificaciones)`

Crea una función `calcular_promedio(calificaciones)` que reciba una lista de calificaciones y devuelva el promedio de todas ellas.

### 3. Función `determinar_estado(calificaciones, umbral)`

Desarrolla una función `determinar_estado(calificaciones, umbral)` que reciba la lista de calificaciones y un valor umbral (por defecto `5.0`), y devuelva dos listas: una con los índices de las materias aprobadas y otra con los índices de las reprobadas.

### 4. Función `encontrar_extremos(calificaciones)`

Implementa una función `encontrar_extremos(calificaciones)` que identifique el índice de la calificación más alta y el índice de la más baja en la lista de calificaciones.

### 5. Función principal (`main`)

En la función principal (`main`), llama a la función `ingresar_calificaciones()` para obtener los datos del usuario.

Utiliza las funciones creadas para:
- Calcular el promedio general
- Determinar materias aprobadas/reprobadas
- Encontrar las materias con calificaciones extremas

### 6. Resumen final

Muestra un resumen final que incluya:
- [x] Todas las materias con sus calificaciones.
- [x] El promedio general.
- [x] Las materias aprobadas y reprobadas.
- [x] La materia con mejor calificación y su valor.
- [x] La materia con peor calificación y su valor.

### 7. Casos especiales y cierre

- [x] Asegúrate de manejar casos especiales, como cuando no se ingresa ninguna materia, utilizando estructuras condicionales apropiadas.
- Finaliza el programa con un mensaje de despedida.
- Implementa la estructura `if __name__ == "__main__":` para ejecutar la función principal.

---

## Requisitos funcionales

- [x] Crear un programa que permita al usuario ingresar nombres de materias y sus calificaciones correspondientes (valores entre 0 y 10).
    Realizado en 
        linea 16
        linea 42
- [x] Almacenar las materias y calificaciones en estructuras de datos adecuadas (listas).
- [x] Calcular y mostrar el promedio general de todas las calificaciones ingresadas.
- [x] Determinar qué materias están aprobadas y reprobadas según un umbral definido (`5.0`).
- [ ] Identificar y mostrar la materia con la calificación más alta y la más baja.
- [x] Permitir al usuario agregar tantas materias como desee, con opción para finalizar la entrada de datos.
- [x] Mostrar un resumen final con toda la información procesada de forma clara.

## Restricciones técnicas

- [x] Utilizar exclusivamente programación estructurada (sin clases ni POO).
- Implementar al menos 3 funciones diferentes para organizar el código.
- [x] Incluir validación básica de entradas para evitar errores.
