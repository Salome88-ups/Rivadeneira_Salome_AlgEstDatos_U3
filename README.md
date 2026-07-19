# Rivadeneira_Salome_AlgEstDatos_U3
# Red de ciudades - Unidad 3 Grafos

## Descripción

Este proyecto implementa una red de ciudades mediante un grafo ponderado utilizando Python.

El programa permite representar ciudades conectadas mediante carreteras y realizar recorridos utilizando algoritmos de grafos.

## Requisitos

- Python 3 instalado.

## Ejecución

Abrir una terminal dentro del proyecto y ejecutar:

python main.py


## Funcionalidades

### R1 - Modelado del grafo

La red se representa mediante un diccionario de Python donde cada ciudad contiene una lista de ciudades vecinas con su distancia en kilómetros.

### R2 - Recorrido BFS

Permite conocer las ciudades alcanzables desde una ciudad inicial y la cantidad de escalas necesarias.

### R3 - Algoritmo Dijkstra

Calcula la distancia mínima desde una ciudad de origen hacia todas las demás ciudades.

### R4 - Comparación

Se compara una ruta con menos escalas obtenida mediante BFS contra una ruta con menor distancia obtenida mediante Dijkstra.
