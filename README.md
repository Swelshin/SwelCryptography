# SwelCryptography
**SwelCryptography** es una recopilación de los metodos criptográficos que diseñe en su momento.

## Tms
**Tms** es un cifrado simétrico que trata de reducir la longitud de la contraseña manteniendo una seguridad y dificultar un analisis criptográfico, no esta completo pues tiene una parte, la que cifra por sustitución sumando en forma de matriz
aunque esa es la parte principal, **Tms** deberia de tener un capa de trasposición antes de iniciar y revertirse al final (dando lo que seria una contraseña matriz totalmente desordenada, volviendo imposible realizar un analisis criptográfico).

**Tms** tiene una forma peculiar de calcular longitudes que es la raíz cuadrada de la longitud del texto por 2.

 $$
 \sqrt{longitud} \times 2
 $$

para 36 números las combinaciones ascienden 2 billones si las contraseñas estan formadas por números del 0 al 9.

**Tms** tiene 2 modos
- contraseña generada, este permite mayor facilidad, pero no se recomienda pues reduce las combinaciones a **36 000 000**.
- contraseña creada manualmente este es el recomendado cuando se necesita la máxima seguridad pues permite infinitas combinaciones.

Aparte de los modos anteriores se puede usar **Tms** para cifrar de 2 formas
- Cifrado de texto, este modo puede dar problemas cuando las contraseñas son grandes, pues convierte las letras a número y luego convierte el texto cifrado en letras de nuevo.
- Cifrado de Números, este modo no da problemas, solo lo hice por eso

### Ejemplo de uso 
```python
import tms.normal_tms as tms #importando tms normal, contraseña elegida por el usuario, es una función

contraseñas = [[5, 2, 4, 2, 24, 3, 9, 10], [7, 4, 3, 6, 23, 5, 9, 30]] # definimos las contraseñas
datos = [] #no se que poner, rellenalo tú vago
datos_cifrados = tms(datos, contraseñas, "enrypt")
print("Datos Cifrados: " + str(datos_cifrados))
datos_descifrados = tms(datos_cifrados, contraseñas, "decrypt")
print("Datos Descifrados: " + str(datos_descifrados))
```
## Leira v4 (las demás versiones no estan disponibles)
**Leira v4** es un cifrado asimétrico.

*Proximamente*
