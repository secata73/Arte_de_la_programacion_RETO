# Arte_de_la_programacion_RETO
Este es el RETO de la entrega final para la semana TEC el arte de la programación 
 

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
