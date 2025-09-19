# Arte_de_la_programacion_RETO
Este es el RETO de la entrega final para la semana TEC el arte de la programación 
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
