# Calculadora de promedios

Primera práctica del Propedéutico Python del MIA (UNIR).

Pide materias y calificaciones, calcula el promedio, muestra aprobadas y reprobadas, y señala la mejor y la peor.

## Correr

    python3 calculadora_promedios.py

## Enunciado

Ver enunciado.md.

## Correcciones v2

Basadas en la evaluación inicial:

- [x] encontrar_extremos recibe materias y calificaciones y devuelve parejas de nombre y nota, en lugar de recibir solo las calificaciones y devolver los índices extremos como se especifica. priority high
- [x] documentar el comportamiento de calcular_promedio cuando la lista está vacía; ahora devuelve implícitamente None. priority medium
- [x] Para que el resumen sea más fácil de leer, podrías mostrar cada materia junto a su calificación en la misma línea, en lugar de imprimir las dos listas por separado. priority low
- [x] En el resumen se muestran los índices de aprobadas y reprobadas, pero no los nombres de esas materias.
- [x] La conversión de la nota con float(input(...)) no captura ValueError; si el usuario introduce texto no numérico, el programa termina con una excepción en vez de volver a solicitar la calificación. priority high