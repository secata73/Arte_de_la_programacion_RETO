# Arte_de_la_programacion_RETO
Este es el RETO de la entrega final para la semana TEC el arte de la programación 
feat_add_canon_modded
Velocidad aumentada del proyectil

Antes: el proyectil se lanzaba con una velocidad moderada definida por la división entre 25 en la función tap.

Ahora: se redujo el divisor para que el proyectil tenga más velocidad al dispararse.

Línea modificada:

speed.x = (x +500) / 20
speed.y = (y +500) / 20

🔹 Velocidad aumentada de los balones

Antes: los balones avanzaban hacia la izquierda restando 0.5 a su coordenada x.

Ahora: se aumentó el valor restado, haciendo que los balones se muevan más rápido.

Línea modificada:

target.x -= 2

🔹 Juego infinito (los balones reaparecen)

Antes: cuando un balón salía de la pantalla, el juego terminaba porque la función hacía return.

Ahora: los balones que salen por la izquierda reaparecen por la derecha en su misma posicion vertical evitando que el juego se acabe

Código añadido:

for target in targets:
    if target.x < -200:
        target.x = 200

✅ Resultado final

Con estos cambios:

El proyectil es más rápido.

Los balones se mueven más rápido.
El juego no tiene final
 

## Cambios realizados en el programa `paint.py`

1. **Nuevo color añadido**
   - Se agregó la opción de color **amarillo** al programa.
   - Atajo de teclado: **Y**.
   - Línea añadida:
     ```python
     onkey(lambda: color('yellow'), 'Y')
     ```

2. **Función `circle` completada**
   - Antes: la función `circle` solo tenía `pass`.
   - Ahora: se calcula el radio entre el punto de inicio y el punto final, se posiciona la tortuga y se dibuja un círculo aproximado con segmentos.
   - Permite dibujar un círculo centrado en el punto inicial y con radio definido por el clic final.

3. **Función `rectangle` completada**
   - Antes: solo tenía `pass`.
   - Ahora: se dibuja un rectángulo usando como esquinas opuestas los puntos `start` y `end`.

4. **Función `triangle` completada**
   - Antes: solo tenía `pass`.
   - Ahora: se dibuja un triángulo equilátero usando como base la distancia horizontal entre `start` y `end`.

## Atajos de teclado finales

- **Colores**:
  - `K`: negro  
  - `W`: blanco  
  - `G`: verde  
  - `B`: azul  
  - `R`: rojo  
  - `Y`: amarillo (nuevo)

- **Formas**:
  - `l`: línea  
  - `s`: cuadrado  
  - `c`: círculo (nuevo)  
  - `r`: rectángulo (nuevo)  
  - `t`: triángulo (nuevo)  

- **Otros**:
  - `u`: deshacer

---

Con estos cambios, el programa ahora permite dibujar **líneas, cuadrados, círculos, rectángulos y triángulos** en diferentes colores, incluyendo el nuevo color amarillo.
# Arte_de_la_programacion_RETO
Este es el RETO de la entrega final para la semana TEC el arte de la programación

## Descripción
Este proyecto consiste en la modificación del clásico videojuego Snake, basado en el código de Grant Jenks.  
El reto fue trabajado en equipo, donde cada integrante tuvo que implementar una funcionalidad diferente y colaborar mediante el uso de GitHub con commits, ramas y merges.  

## Cambios realizados
1. **Movimiento de la comida**  
   - Se agregó la función `move_food()` para que la comida se mueva de manera aleatoria un paso a la vez.  
   - La comida puede moverse hacia arriba, abajo, izquierda o derecha.  
   - Se agregó una validación para evitar que la comida se salga de los límites de la ventana.  

2. **Colores aleatorios diferentes**  
   - Se definió una lista con cinco colores permitidos: azul, morado, naranja, amarillo y rosa.  
   - Al iniciar el juego, la víbora y la comida reciben colores diferentes seleccionados de esa lista.  
   - El color rojo quedó reservado únicamente para la pantalla de "Game Over".  

## Instrucciones de uso
1. Ejecutar el archivo `snake.py` en Python 3.  
2. Controlar la víbora con las teclas:  
   - Flecha derecha → mover a la derecha  
   - Flecha izquierda → mover a la izquierda  
   - Flecha arriba → mover hacia arriba  
   - Flecha abajo → mover hacia abajo  
3. El objetivo es comer la comida que aparece en pantalla, la cual también se mueve de manera aleatoria.  
4. El juego termina cuando la víbora choca contra los bordes de la ventana o contra sí misma.  

## Requisitos
- Python 3  
- Librería `turtle`  
- Librería `freegames` (instalar con `pip install freegames`)  

## Autores
- [Tu nombre]  
- [Nombre de tu compañero/a]  

## Historia de commits esperada
- `Initial commit: Add original Snake game code`  
- `Docs: Add Instituto standard documentation`  
- `Feat: Add random movement for food`  
- `Feat: Snake and food get random colors (except red)`  
- `Fix: Prevent food from leaving the window`  
- `Docs: Update README and final documentation`  
# Arte\_de\_la\_programacion\_RETO

Este es el RETO de la entrega final para la semana TEC *El arte de la programación*.

## Descripción

Este proyecto consiste en la modificación del clásico videojuego **Memory**, basado en el código de Grant Jenks.
El reto fue trabajado en equipo, donde cada integrante tuvo que implementar una funcionalidad diferente y colaborar mediante el uso de GitHub con commits, ramas y merges.

## Cambios realizados

1. **Contador de taps (clics del usuario)**

   * Se agregó un contador que registra cuántas veces el jugador ha hecho clic.
   * El valor se muestra en la parte superior izquierda de la pantalla durante toda la partida.

2. **Detección de juego completado**

   * Se agregó una validación que detecta cuando todas las fichas han sido destapadas.
   * Al finalizar, se despliega un mensaje de felicitación en la pantalla.

3. **Centrado de los valores en cada cuadro**

   * Los símbolos ahora aparecen centrados dentro de cada ficha, mejorando la estética y la legibilidad.

4. **Innovación: uso de emojis en lugar de números**

   * Para mejorar la jugabilidad y estimular la memoria visual, los números fueron reemplazados por **emojis de frutas, verduras y alimentos**.
   * Esto hace el juego más intuitivo, colorido y atractivo para los usuarios.

## Instrucciones de uso

1. Ejecutar el archivo `memory.py` en Python 3.
2. El objetivo es encontrar todos los pares de fichas iguales haciendo clic en ellas.
3. El juego termina cuando se destapan todos los pares, mostrando un mensaje de felicitación.

## Requisitos

* Python 3
* Librería `turtle`
* Librería `freegames` (instalar con `pip install freegames`)

## Autor

* \[Sebastián Camacho]

## Historia de commits esperada

* `Initial commit: Add original Memory game code`
* `Feat: Add tap counter`
* `Feat: Detect game completion`
* `Fix: Center symbols inside tiles`
* `Feat: Replace numbers with emojis for better memory aid`
* `Docs: Update code comments and README`
*  main

"""
==========================================================
REPORTE DE ACTIVIDAD 3: Juego del Pacman (Gpo 101)
Por Pedro Escobedo - A01787721
==========================================================

Propósito:
Modificar y documentar el videojuego Pacman con nuevas 
funcionalidades, trabajando en colaboración y siguiendo 
los estándares del Instituto.

Cambios implementados:
1. Tablero cambiado (tiles modificados).
2. Número de fantasmas parametrizable (GHOST_STARTS).
3. Posición inicial de Pacman cambiada (vector(-160, 160)).
4. Velocidad de fantasmas ajustable (GHOST_SPEED y TIMER_MS).
5. Fantasmas más listos (IA greedy con aleatoriedad 20%).

Documentación:
- Se añadieron docstrings a las funciones principales.
- Se comentaron las secciones de configuración, tablero 
  e inteligencia de los fantasmas.

🎯 Conclusión:
El proyecto Pacman fue modificado exitosamente para cumplir 
con las funcionalidades solicitadas. Se documentó el código, 
se gestionó con commits en GitHub y se prepararon los archivos 
para la entrega.
==========================================================
"""
