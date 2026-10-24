# Proyectos de Python

Proyectos y algoritmos en Python de mi formación, incluidos proyectos de la certificación **Scientific Computing with Python** de [freeCodeCamp](https://www.freecodecamp.org/).

Cubren programación orientada a objetos, recursión, backtracking y manejo de matrices, sin librerías externas.

| Proyecto | Archivo | Conceptos |
| --- | --- | --- |
| App de presupuesto | [`build-a-budget-app.py`](build-a-budget-app.py) | Clases, listas de diccionarios, formato de texto |
| Calculadora de polígonos | [`build-a-polygon-area-calculator.py`](build-a-polygon-area-calculator.py) | Herencia, sobrescritura de métodos |
| Torres de Hanói | [`Hanoi.py`](Hanoi.py) | Algoritmo iterativo, pilas |
| N-Reinas | [`N_Queens.py`](N_Queens.py) | Recursión, backtracking (DFS) |
| Ganador de Tateti | [`Tic_Tac_Toe.py`](Tic_Tac_Toe.py) | Matrices N×N, recorridos |

## Cómo ejecutarlos

Requisito: Python 3. No hace falta instalar ninguna librería.

```bash
git clone https://github.com/Fercho612/Python-Projects.git
cd Python-Projects
python build-a-budget-app.py
```

Cada archivo trae al final un ejemplo de uso que se ejecuta al correrlo.

## Proyectos

### App de presupuesto

Clase `Category` que lleva el saldo de una categoría de gastos con depósitos, retiros y transferencias, y rechaza movimientos sin fondos suficientes. La función `create_spend_chart` dibuja en texto el porcentaje gastado por categoría:

```
Percentage spent by category
100|
 ...
 50|    o
 40| o  o
 30| o  o
 20| o  o
 10| o  o  o
  0| o  o  o
    ----------
     F  C  A
     o  l  u
     o  o  t
     d  t  o
```

### Calculadora de polígonos

Clases `Rectangle` y `Square` (que hereda de `Rectangle`) para calcular área, perímetro y diagonal, dibujar la figura con asteriscos y contar cuántas veces entra una figura dentro de otra.

### Torres de Hanói

`hanoi_solver(n)` resuelve el problema de forma iterativa y devuelve el estado de las tres torres después de cada movimiento. Usa la cantidad mínima de movimientos: 2ⁿ − 1.

```
[3, 2, 1] [] []
[3, 2] [] [1]
...
[] [] [3, 2, 1]
```

### N-Reinas

`dfs_n_queens(n)` encuentra todas las formas de ubicar n reinas en un tablero de n×n sin que se ataquen, con búsqueda en profundidad y backtracking. Cada solución indica la columna de la reina en cada fila. Para n = 8 encuentra las 92 soluciones.

### Ganador de Tateti

Funciones que detectan si hay un ganador en un tablero cuadrado de cualquier tamaño, revisando filas, columnas y las dos diagonales, e ignorando las casillas vacías.

## Autor

Fernando Pereyra Galetti · [GitHub](https://github.com/Fercho612)
