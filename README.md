# Arte_de_la_programacion_RETO
Este es el RETO de la entrega final para la semana TEC el arte de la programación 
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