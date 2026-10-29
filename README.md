# Guía rápida · parcial.py (Parcial 3 · Sistemas Operativos)

Programa en Python **sin dependencias** (solo librería estándar). Funciona **sin internet**.

---

## 0. Preparación (una sola vez)

Deja estos archivos en la misma carpeta, por ejemplo `~/Desktop/parcial SO/`:

- `parcial.py`
- `README_Parcial3_SO.md` (el archivo donde busca el buscador)

Abre la terminal en esa carpeta:

```
cd "/home/mateo/Desktop/parcial SO"
python3 --version
```

Si `python3` no responde, prueba con `python` o `py` (Windows) en todos los comandos.

### Regla de oro (lo que más confunde)

| Si quieres... | Dónde lo escribes |
|---------------|-------------------|
| **Buscar** teoría o métodos en el README | `python3 parcial.py buscar README_Parcial3_SO.md` y luego, **dentro** del `pregunta >`, escribes solo palabras clave |
| **Calcular** (`ajuste`, `banquero`, `deteccion`, `pagina`) | El comando completo en la **terminal normal**. NUNCA dentro del `pregunta >` |

Para salir del buscador: Enter con la línea vacía, o Ctrl+C.

### Formato de los datos (igual en todos los comandos)

- **Matrices:** una fila por proceso. `;` separa filas y `,` separa columnas.
  `"0,1,0;2,0,0"` significa P0 = (0,1,0) y P1 = (2,0,0).
- **Hexadecimal:** siempre con `0x` delante (`0x00C00000`).
- **Comillas:** pon cada dato entre comillas dobles `"..."`.
- **Orden de las filas:** P0 es la primera fila, P1 la segunda, etc.

---

## 1. Buscador

```
python3 parcial.py buscar README_Parcial3_SO.md --chars 3000
```

`--chars 3000` evita que los fragmentos salgan cortados. Aparece `pregunta (vacio = salir) >` y escribes **4 a 6 palabras clave**, no el enunciado completo.

Ejemplos de búsquedas (escríbelas dentro del `pregunta >`):

```
banquero necesidad secuencia segura
primer mejor peor ajuste hueco hexadecimal
pagina desplazamiento marco tabla
espera circular semaforos orden wait bloqueo
monitor wait notifyAll while
```

Consejos:
- Revisa **varios resultados**, no solo el primero.
- Si sale flojo, reformula con sinónimos o con el nombre del algoritmo.
- Escribe **una búsqueda por vez**, con Enter entre ellas (si las pegas juntas se funden en una sola palabra).
- Una sola búsqueda sin entrar al modo interactivo:
  ```
  python3 parcial.py buscar README_Parcial3_SO.md -q "banquero necesidad" -n 5 --chars 3000
  ```

El buscador **solo trae texto relacionado**. No resuelve nada.

---

## 2. Memoria continua · `ajuste`

Calcula **primer, mejor y peor ajuste** de una vez.

```
python3 parcial.py ajuste --huecos "base/limite,base/limite,..." --req "tam1,tam2,..."
```

- `--huecos`: cada hueco como `base/limite`, **en el orden del enunciado**.
- `--req`: los tamaños solicitados, en orden.

### Ejemplo (Punto 3 del simulacro)

Huecos: `0x02000000/0x00600000`, `0x03400000/0x00300000`, `0x05000C00/0x00A00000`, `0x08100000/0x00500000`. Solicitudes: 0x00400000, 0x00500000, 0x00200000.

```
python3 parcial.py ajuste --huecos "0x02000000/0x00600000,0x03400000/0x00300000,0x05000C00/0x00A00000,0x08100000/0x00500000" --req "0x00400000,0x00500000,0x00200000"
```

Salida:

```
##### PRIMER AJUSTE #####
req 0x00400000 -> hueco #0 (base proceso 0x02000000, limite hueco 0x600000)
req 0x00500000 -> hueco #2 (base proceso 0x05000C00, limite hueco 0xa00000)
req 0x00200000 -> hueco #0 (base proceso 0x02400000, limite hueco 0x200000)
tabla final: 0x03400000/0x300000 | 0x05500C00/0x500000 | 0x08100000/0x500000

##### MEJOR AJUSTE #####
req 0x00400000 -> hueco #3 (base proceso 0x08100000, limite hueco 0x500000)
req 0x00500000 -> hueco #0 (base proceso 0x02000000, limite hueco 0x600000)
req 0x00200000 -> hueco #1 (base proceso 0x03400000, limite hueco 0x300000)
tabla final: 0x02500000/0x100000 | 0x03600000/0x100000 | 0x05000C00/0xa00000 | 0x08500000/0x100000

##### PEOR AJUSTE #####
req 0x00400000 -> hueco #2 (base proceso 0x05000C00, limite hueco 0xa00000)
req 0x00500000 -> hueco #0 (base proceso 0x02000000, limite hueco 0x600000)
req 0x00200000 -> hueco #2 (base proceso 0x05400C00, limite hueco 0x600000)
tabla final: 0x02500000/0x100000 | 0x03400000/0x300000 | 0x05600C00/0x400000 | 0x08100000/0x500000
```

Cómo leerlo:
- `hueco #N`: número del hueco **en el orden del enunciado** (empieza en 0).
- `base proceso`: dónde queda el proceso (la base del hueco elegido).
- `limite hueco`: tamaño del hueco **antes** de asignar.
- `tabla final`: los huecos que quedan, en el mismo orden. Un hueco que llega a 0 desaparece.
- Empates (mejor/peor ajuste): se toma el **primero** de la lista.
- Si un requisito no cabe, imprime `NO CABE (espera)`.

**No cubre:** terminación de procesos, fusión de huecos ni cola de espera (eso se hace a mano con el método del README §5.3).

---

## 3. Banquero · `banquero`

Calcula Necesidad, dice si el estado es seguro (con secuencia) y evalúa una solicitud.

```
python3 parcial.py banquero --asig "..." --max "..." --disp "..." [--pide "proceso:vector"] [--total "..."]
```

- `--asig`: matriz de Asignación.
- `--max`: matriz de Máximo.
- `--disp`: Disponible dado en el enunciado.
- `--total`: existencias totales. Si lo pasas **sin** `--disp`, calcula el Disponible por ti.
- `--pide "3:1,1,1"`: el proceso **3** solicita (1,1,1).

### Ejemplo (banquero con solicitud)

Existencias (9,6,5). P0..P3. Asignación: (1,1,0) (2,1,1) (1,0,2) (2,1,0). Máximo: (4,3,2) (3,2,2) (3,1,4) (5,2,2). P3 solicita (1,1,1).

```
python3 parcial.py banquero --asig "1,1,0;2,1,1;1,0,2;2,1,0" --max "4,3,2;3,2,2;3,1,4;5,2,2" --total "9,6,5" --pide "3:1,1,1"
```

Salida:

```
Necesidad:
  P0: [3, 2, 2]
  P1: [1, 1, 1]
  P2: [2, 1, 2]
  P3: [3, 1, 2]
  Trabajo = [3, 3, 2]
  P0 (necesita [3, 2, 2]) -> Trabajo = [4, 4, 2]
  P1 (necesita [1, 1, 1]) -> Trabajo = [6, 5, 3]
  P2 (necesita [2, 1, 2]) -> Trabajo = [7, 5, 5]
  P3 (necesita [3, 1, 2]) -> Trabajo = [9, 6, 5]
SEGURO, secuencia: ['P0', 'P1', 'P2', 'P3']

P3 solicita [1, 1, 1]
  Simulado: Disponible = [2, 2, 1]
  Trabajo = [2, 2, 1]
  P1 (necesita [1, 1, 1]) -> Trabajo = [4, 3, 2]
  P0 (necesita [3, 2, 2]) -> Trabajo = [5, 4, 2]
  P2 (necesita [2, 1, 2]) -> Trabajo = [6, 4, 4]
  P3 (necesita [2, 0, 1]) -> Trabajo = [9, 6, 5]
SEGURO -> SE CONCEDE
```

Cómo leerlo:
- El primer `Trabajo` es el **Disponible** (aquí (9,6,5) − suma de asignaciones = (3,3,2)).
- Cada línea `P# (necesita ...)` es un paso de la secuencia segura.
- Si dice `INSEGURO -> NO SE CONCEDE`, la solicitud se rechaza. Si dice `No hay disponible`, el proceso espera. Si dice `ERROR: excede su maximo`, la solicitud supera su Necesidad.

### Verificar si el Disponible del enunciado está mal (trampa de 2018)

Pasa **ambos**: `--disp` (el del enunciado) y `--total`. Imprime `OK` o `<-- NO COINCIDE`.

```
python3 parcial.py banquero --asig "..." --max "..." --disp "7,2,5,5" --total "15,6,9,10"
```

**Lo que debes escribir tú en el examen:** las verificaciones de la solicitud (Solicitud ≤ Necesidad, Solicitud ≤ Disponible). El programa las hace por dentro pero no las imprime.

---

## 4. Detección de bloqueos · `deteccion`

Usa **Solicitud** (no Máximo). Dice qué procesos quedan bloqueados.

```
python3 parcial.py deteccion --asig "..." --sol "..." --disp "..."
```

### Ejemplo (a): hay bloqueo

5 procesos, 3 recursos, Disponible (0,0,0). Asignación: (0,1,0) (2,0,0) (3,0,3) (2,1,1) (0,0,2). Solicitud: (0,0,0) (2,0,2) (0,0,1) (1,0,0) (0,0,2).

```
python3 parcial.py deteccion --asig "0,1,0;2,0,0;3,0,3;2,1,1;0,0,2" --sol "0,0,0;2,0,2;0,0,1;1,0,0;0,0,2" --disp "0,0,0"
```

Salida:

```
Trabajo = [0, 0, 0]; Fin inicial = [False, False, False, False, False]
  P0 (pide [0, 0, 0]) termina -> Trabajo = [0, 1, 0]
BLOQUEADOS: P1, P2, P3, P4
```

### Ejemplo (b): cambias una fila y no hay bloqueo

Igual, pero P2 solicita (0,0,0):

```
python3 parcial.py deteccion --asig "0,1,0;2,0,0;3,0,3;2,1,1;0,0,2" --sol "0,0,0;2,0,2;0,0,0;1,0,0;0,0,2" --disp "0,0,0"
```

Salida:

```
Trabajo = [0, 0, 0]; Fin inicial = [False, False, False, False, False]
  P0 (pide [0, 0, 0]) termina -> Trabajo = [0, 1, 0]
  P2 (pide [0, 0, 0]) termina -> Trabajo = [3, 1, 3]
  P1 (pide [2, 0, 2]) termina -> Trabajo = [5, 1, 3]
  P3 (pide [1, 0, 0]) termina -> Trabajo = [7, 2, 4]
  P4 (pide [0, 0, 2]) termina -> Trabajo = [7, 2, 6]
NO hay bloqueo
```

Cómo leerlo:
- `Fin inicial`: verdadero solo para procesos cuya Asignación es toda ceros.
- Cada línea es un proceso cuya Solicitud cabe en `Trabajo`; al terminar devuelve su Asignación.
- `BLOQUEADOS: ...` son los que nunca lograron terminar.
- Cuando el profe pregunta "¿y si P1 solicita X?", **cambia solo esa fila de `--sol`** y vuelve a correr.

---

## 5. Paginación · `pagina`

Separa página y desplazamiento y traduce direcciones lógicas a físicas.

```
python3 parcial.py pagina --pag TAMAÑO --tabla "marcos" --dir "direcciones" [--bits N] [--proc BYTES]
```

- `--pag`: tamaño de página en **bytes** (potencia de 2: 512, 1024, 4096...).
- `--tabla`: el marco de la página 0, 1, 2, ... en ese orden.
- `--dir`: direcciones lógicas (decimal o `0x...`).
- `--bits`: bits de la dirección (opcional, imprime cuántos son de página y de desplazamiento).
- `--proc`: tamaño del proceso en bytes (opcional, para marcar direcciones fuera del límite).

### Ejemplo A (Punto 4 del simulacro)

Direcciones de 20 bits, páginas de 512 B. Tabla: pág.0→marco 6, 1→2, 2→9, 3→4.

```
python3 parcial.py pagina --pag 512 --tabla "6,2,9,4" --dir "0x005FF,0x00400,0x00600,0x007FF" --bits 20
```

Salida:

```
Pagina 512 B -> 9 bits de desplazamiento, 11 bits de pagina (2048 entradas)
0x5ff (1535): pagina 2, desp 0x1ff, marco 9 -> fisica 0x13ff (5119)
0x400 (1024): pagina 2, desp 0x0, marco 9 -> fisica 0x1200 (4608)
0x600 (1536): pagina 3, desp 0x0, marco 4 -> fisica 0x800 (2048)
0x7ff (2047): pagina 3, desp 0x1ff, marco 4 -> fisica 0x9ff (2559)
```

### Ejemplo B (página inválida)

Direcciones de 16 bits, páginas de 1 KB. Tabla: 7,2,5,0,9,1 (6 páginas).

```
python3 parcial.py pagina --pag 1024 --tabla "7,2,5,0,9,1" --dir "0x0C35,0x1400,0x17FF,0x0041,0x2000" --bits 16
```

Salida:

```
Pagina 1024 B -> 10 bits de desplazamiento, 6 bits de pagina (64 entradas)
0xc35 (3125): pagina 3, desp 0x35, marco 0 -> fisica 0x35 (53)
0x1400 (5120): pagina 5, desp 0x0, marco 1 -> fisica 0x400 (1024)
0x17ff (6143): pagina 5, desp 0x3ff, marco 1 -> fisica 0x7ff (2047)
0x41 (65): pagina 0, desp 0x41, marco 7 -> fisica 0x1c41 (7233)
0x2000 (8192): pagina 8, desp 0 -> PAGINA INVALIDA / fuera del limite
```

Cómo leerlo:
- Fórmula que usa: `fisica = marco * P + (D mod P)`, con `pagina = D // P`.
- `PAGINA INVALIDA` significa que la página no existe en la tabla (trap en el examen).

**No cubre:** asignación de marcos con eventos (procesos que llegan/terminan), fragmentación interna, TLB ni tiempo efectivo de acceso. Eso se hace a mano con las fórmulas del README §6.

---

## 6. Qué NO resuelve el programa (hazlo a mano con el README)

| Tipo de ejercicio | Dónde está la plantilla en `README_Parcial3_SO.md` |
|-------------------|----------------------------------------------------|
| Grafo de asignación (evitar bloqueos) | §4.3-A |
| Código con monitor o semáforos | §3.3 y §3.4 |
| Memoria continua con eventos, fusión y cola de espera | §5.3 y H-M3 |
| Paginación con eventos (marcos libres) | §6.3 |
| Contadores de semáforos | §3.2 |
| Teoría (condiciones de bloqueo, TLB, etc.) | usa el buscador |

---

## 7. Problemas comunes

| Síntoma | Causa y solución |
|---------|------------------|
| El comando devuelve fragmentos del README en vez de calcular | Lo pegaste dentro del `pregunta >`. Sal con Enter vacío y pégalo en la terminal normal. |
| `python3: command not found` | Prueba `python` o `py`. |
| `No such file or directory` | No estás en la carpeta correcta: `cd "/home/mateo/Desktop/parcial SO"`. |
| Error de argumentos / `unrecognized arguments` | Falta una comilla o hay un espacio dentro de una matriz. No pongas espacios en `"0,1,0;2,0,0"`. |
| `invalid literal for int()` | Un número está mal escrito o falta el `0x` en un hexadecimal. |
| Dos búsquedas salen mezcladas | Las pegaste en la misma línea. Una búsqueda por Enter. |
| Resultados raros en el buscador | Usa menos palabras, más específicas, y revisa los 5 primeros resultados. |

---

## 8. Checklist para el examen

- [ ] Confirmar con el profe que el programa propio está permitido (el buscador es la parte dudosa).
- [ ] Tener `parcial.py` y `README_Parcial3_SO.md` en la misma carpeta, y probar un comando de cada tipo antes de empezar.
- [ ] Copiar los números del enunciado con cuidado (una cifra mal en un hex arrastra todo).
- [ ] Copiar la salida a la hoja **con los pasos** (`Trabajo = ...`): el profe pide justificación.
- [ ] Revisar si algún dato del enunciado puede estar mal a propósito (Disponible).
- [ ] Declarar los supuestos (por ejemplo "primer ajuste desde la primera posición").