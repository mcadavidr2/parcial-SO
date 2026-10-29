# README · Preparación Parcial 3 · ST0257 Sistemas Operativos

**Profesor:** Juan Francisco Cardona McCormick · **Material base:** transcripciones de clase, Capítulo 3 (PDF), parciales 2013‑2025, taller previo al parcial 3.

> **Cómo usar este documento.** Léelo en este orden: §1 (qué dijo el profe) → §2 (cómo pregunta) → §3 a §6 (un tema por sección: teoría mínima + método paso a paso + ejercicios reales + ejercicios hipotéticos con solución) → §7 (simulacro) → §8 (checklist de última hora).
>
> **Etiquetas.** `[REAL]` = ejercicio que el profesor ya puso en un parcial (enunciado resumido y solución). `[HIP]` = ejercicio hipotético que inventé imitando su estilo. Todas las cuentas de los `[HIP]` y las que resolví de los `[REAL]` están **verificadas con código** (Python y Java); los programas de concurrencia se compilaron y se ejecutaron.

---

## Índice

1. [Qué dijo el profesor y qué esperar](#1-qué-dijo-el-profesor-y-qué-esperar)
2. [Cómo formula las preguntas el profesor](#2-cómo-formula-las-preguntas-el-profesor)
3. [Tema 1 · Concurrencia](#3-tema-1--concurrencia)
4. [Tema 2 · Bloqueos (interbloqueos)](#4-tema-2--bloqueos-interbloqueos)
5. [Tema 3 · Memoria continua](#5-tema-3--memoria-continua)
6. [Tema 4 · Memoria paginada (y lo que la rodea)](#6-tema-4--memoria-paginada-y-lo-que-la-rodea)
7. [Simulacro de parcial](#7-simulacro-de-parcial)
8. [Errores típicos y checklist de última hora](#8-errores-típicos-y-checklist-de-última-hora)
9. [Fuentes y límites de este documento](#9-fuentes-y-límites-de-este-documento)

---

## 1. Qué dijo el profesor y qué esperar

### 1.1 Los temas (transcripción "Taller antes del parcial 3")

Cuando un estudiante le preguntó qué temas caían, el profesor respondió textualmente en este orden:

| # | Tema | Cómo lo describió |
|---|------|-------------------|
| 1 | **Concurrencia** | Es el cierre del capítulo de procesos; explicó que los mecanismos de concurrencia no se habían evaluado de forma extensiva antes, por eso entran ahora. |
| 2 | **Bloqueos** | "Cómo evitar, cómo detectar y cómo manejar" los bloqueos. |
| 3 | **Memoria continua** | Es uno de los dos temas de memoria vistos hasta el momento. |
| 4 | **Memoria paginada** | El otro tema de memoria visto. |

Además dijo, durante el taller:

* Los 3 ejercicios que resolvió **son ejemplos de tipos de ejercicio**, no los que saldrán: "yo siempre trato de hacer un parcial distinto… para que no tengamos el mismo ejercicio repetido 200 veces", pero "no digo que se vayan a salir de esos 3, son parte de los temas".
* Los ejercicios que resolvió en el taller fueron: (a) **3 procesos con 3 variables compartidas y semáforos** (concurrencia que además es de bloqueos), (b) **3 procesos y 6 recursos A–F con grafo de asignación** (mostrar el bloqueo y evitarlo cambiando el orden de los `get`) y (c) **memoria continua con primer/mejor/peor ajuste** en hexadecimal.
* **Conceptos de parciales anteriores** (por ejemplo microkernel) no los evalúa directamente, pero los da por sabidos si aparecen dentro de un ejercicio.
* Revisen las **soluciones de los parciales anteriores** (hay versiones con solución) y practiquen; mencionó la página 352 del libro (un ejercicio de asignación de recursos).
* **Reglas del examen:** pueden llevar libros, manuales y calculadora (modo *programador* para hexadecimal). Puedes usar un programa propio o una hoja de Excel para calcular. **No** se permite inteligencia artificial, compañeros ni consultar por WhatsApp.
* En el parcial de memoria te pedirá **llenar la tabla de segmentos libres** y puede pedir además "cómo queda la tabla de procesos / el BCP / la MMU de cada uno".
* Si el enunciado **no dice dónde empieza** el primer ajuste, asume **la primera posición**. Si el round robin **no dice el quantum**, asume **1** (esto último lo dijo en la sesión de preguntas y respuestas).

### 1.2 Estructura probable del examen

El parcial 3 de las últimas ediciones **siempre tiene 4 ejercicios largos** (25 % a 40 % cada uno). Estos son los más recientes:

| Fecha | Ejercicios |
|-------|-----------|
| **30‑oct‑2025** (el más reciente) | (25 %) Código concurrente con **semáforos** (control modular por turnos) · (25 %) **Grafo de asignación**, evitar bloqueos · (25 %) **Detección de bloqueos** (algoritmo con matrices) · (25 %) **Memoria continua** hex, primer/mejor/peor ajuste |
| 7‑may‑2020 (dos versiones) | (30 %) Código concurrente con **monitores** (cerrojo con llaves / fábrica de aviones) · (25 %) **Grafo**, evitar bloqueos · (20 %) **Detección** de bloqueos (versión A) o **Banquero** (versión B) · (25 %) **Memoria continua** hex (A) o contabilidad de memoria (B) |
| 31‑oct‑2019 | (35 %) Detección de bloqueos · (30 %) Memoria continua · (35 %) Banquero |
| 9/10/17‑may‑2019 | (40 %) **Banquero concurrente** (monitor sobre una clase) · (30 %) Memoria continua hex · (30 %) Banquero |
| 2018 | Preguntas de memoria (nº de páginas, traducción MMU, tiempo efectivo de acceso) · Banquero (30 %) · Memoria virtual con segmentación y paginación + reemplazo (40‑50 %) |
| 2016‑2017 | Monitor manejador de recursos (30 %) · Memoria dinámica *mejor ajuste con eventos* (35 %) · **Paginación con eventos** (35 %) · Banquero (30‑40 %) · Segmentación + paginación (60 %) |
| 2013‑2015 | 10 preguntas de selección múltiple (3‑4 % c/u) sobre monitores, bloqueos, fallos de página, ajuste en particiones, paginación + 3 ejercicios largos (reemplazo de páginas, mejor ajuste, código de la MMU) |

**Lectura práctica:** en 2025 y 2020 el parcial 3 fue **concurrencia + grafo + algoritmo de matrices + memoria continua**. La **paginación** fue el ejercicio largo en 2014, 2016 y 2018 y además aparece como pregunta corta. Estudia los cuatro temas completos, pero ensaya primero estos cuatro tipos de ejercicio.

### 1.3 Prioridades

| Prioridad | Qué | Por qué |
|-----------|-----|---------|
| 🔴 Máxima | Memoria continua (3 ajustes), grafo de asignación (evitar), detección de bloqueos, banquero, código con monitor/semáforos | Aparecen casi siempre y son los que el profe resolvió en el taller |
| 🟠 Alta | Paginación: traducción de direcciones, tamaños, asignación de marcos con eventos, fórmula $F=\text{marco}(D/P)\cdot P + D \bmod P$ | Tema declarado; sale como ejercicio largo o como 3‑4 preguntas cortas |
| 🟡 Media | Teoría de monitores / semáforos (selección múltiple), prevención y recuperación de bloqueos, TLB y tiempo efectivo de acceso | Preguntas cortas |
| ⚪ Baja pero cubierta | Reemplazo de páginas (FIFO/LRU/óptimo), segmentación, memoria virtual | Salen en parciales viejos, pero **el profe dijo que solo se vio memoria continua y paginada**. Está en §6.6 por si acaso |

---

## 2. Cómo formula las preguntas el profesor

Estos son los **patrones de enunciado** que se repiten. Reconocerlos te dice qué algoritmo aplicar sin pensar.

| # | Frase típica (resumida) | Qué te está pidiendo |
|---|------------------------|----------------------|
| 1 | "La figura muestra el grafo de asignación de recursos… a partir de $t_i$ ocurren los siguientes eventos: $t_i$: P0 solicita a R0, $t_{i+1}$: P1 solicita a R1… Muestre el estado del sistema en $t_{i+5}$: ¿qué procesos están bloqueados? ¿qué recursos están asignados? ¿cuáles sin asignar?" | Método del **grafo con aristas de reclamo** (§4.3‑A). Evento por evento: ¿el recurso está libre? ¿al asignarlo se forma un ciclo? |
| 2 | "Aplique el algoritmo de detección de bloqueos a los siguientes datos y muestre los resultados… Si el sistema no está bloqueado, ¿qué pasa si P1 solicita dos ejemplares más de R0?" | **Detección multi‑instancia** con `Trabajo`/`Fin` y matriz **Solicitud** (§4.3‑C). Luego cambias una fila y repites |
| 3 | "Dado el siguiente estado… a) ¿Cuál es el contenido de la matriz Necesidad? b) ¿Se encuentra en un estado seguro? c) Si P1 solicita (1,0,2), ¿puede concederse inmediatamente? d) Si luego P3 solicita (0,0,0,1), ¿seguro o inseguro?" | **Algoritmo del banquero** completo (§4.3‑B). A veces pide "verifique que el arreglo de Disponibilidad está bien calculado" (¡puede estar mal a propósito!) |
| 4 | "Considere un sistema de memoria continua con los siguientes huecos en el orden de la memoria… ¿Cuáles huecos son tomados con la secuencia de requisitos…? Muestre cómo queda la lista de segmentos libres con a) primer ajuste b) mejor ajuste c) peor ajuste." | §5.2. Aritmética en **hexadecimal** (base + tamaño) |
| 5 | "Implemente las clases `X` y `Y` para que se comporten de forma concurrente y acorde a la descripción…" + historia larga con chistes + figura UML | Un **monitor** (Java `synchronized`/`wait`/`notifyAll`) o **semáforos**. Ignora el relato y extrae las reglas (§3.7) |
| 6 | "Con el método del mejor ajuste, muestre en cada evento cómo queda la memoria ocupada, las particiones libres y los procesos que se quedan esperando por memoria." | Memoria dinámica con **llegadas, terminaciones, fusión de huecos y cola de espera** (§5.3) |
| 7 | "La memoria funciona con paginación con marcos de 1K… muestre en cada evento cómo queda la tabla de páginas de los procesos activos, los marcos libres y los procesos en estado *nuevo*." | Paginación con **lista de marcos libres** y cola de espera (§6.3) |
| 8 | "Complete el código que falta en el constructor y en `fromLogicToPhysic()`." | Código de la **MMU**: `tabla[dir / tamPag] * tamPag + dir % tamPag` (§6.5) |
| 9 | "Llene la siguiente tabla: pasó/falló, cuánta memoria libre queda, qué módulo falló, cuánta memoria hizo falta." | **Contabilidad de memoria** (§5.4) |
| 10 | Selección múltiple (3‑4 % c/u): "¿Cuántos procesos pueden estar esperando en un monitor…?", "¿Qué significa retener y esperar?", "Cuando una página es traída de disco el proceso queda en estado…", "valor de los contadores de los semáforos". | Teoría con clave: ver §3.5, §4.1 y §6.4 |

**Rasgos de estilo que conviene conocer**

1. **Ejercicios con trampa.** El de los 3 procesos y 3 semáforos "funciona el 99,9 % de las veces", pero si los pides en distinto orden hay bloqueo. Él mismo dice: "aunque es un ejercicio de concurrencia, es también un ejercicio de bloqueos".
2. **Datos que pueden estar mal a propósito:** en el banquero de 2018 el vector `Disponible` del enunciado estaba mal y el inciso (a) era detectarlo. En la clase también dijo "creo que hay un error" en un enunciado. Si algo no cuadra, recalcula y avisa.
3. **Tablas de justificación.** "Cada paso debe estar justificado", "utilice un grafo de asignación de recursos para justificar su respuesta". Escribe la secuencia de `Trabajo` y las comparaciones, no solo el resultado.
4. **Cálculos largos:** dijo que "esto es larguito, hay que echar mucha calculadora". Usa la calculadora en modo programador y verifica sumas hexadecimales dos veces.
5. **Humor y relatos largos** en los enunciados (con notas al pie). Léelos una vez, luego extrae: *recursos, reglas, qué métodos hay que escribir*.
6. **Variantes por grupo/fecha:** el mismo ejercicio con otros números (en 2019 hubo tres versiones con idéntica estructura). Practicar con números distintos es lo que sirve.
7. **Casi nunca piden demostraciones**, piden **simular y mostrar el estado final**.
---

## 3. Tema 1 · Concurrencia

### 3.1 Teoría mínima (todo lo que está en el Capítulo 3)

**Condición de carrera.** Dos o más procesos (o hilos) leen/escriben datos compartidos y el resultado final depende de *quién* ejecuta y *exactamente cuándo*. Ejemplo del capítulo: `contador++` (productor) y `contador--` (consumidor) se descomponen en `registro = contador; registro = registro ± 1; contador = registro`. Intercalados mal, con `contador = 5` el resultado puede ser **4 o 6** en vez de 5.

**Sección crítica.** Segmento de código donde se tocan variables compartidas. Estructura de un proceso: `sección de ingreso → sección crítica → sección de egreso → sección restante`. Los **6 requisitos** de una solución:

1. **Exclusión mutua**: solo un proceso a la vez en la sección crítica del mismo recurso.
2. Un proceso que se interrumpe fuera/dentro de su sección crítica **no debe interferir** con los otros.
3. **Sin bloqueo ni inanición**: nadie espera indefinidamente.
4. **Progreso**: si nadie está en su sección crítica, quien quiera entrar **entra sin dilación**.
5. **No se asumen velocidades** relativas ni número de procesadores.
6. Un proceso permanece en su sección crítica un **tiempo finito**.

**Soluciones por software (2 procesos $i$, $j$).**

| Algoritmo | Idea | Resultado |
|-----------|------|-----------|
| 1 · turno | `while (turno != i); SC; turno = j;` | Exclusión mutua ✔, pero **obliga a alternar**: viola *progreso* (requisito 4). |
| 2 · banderas | `indicador[i]=true; while(indicador[j]); SC; indicador[i]=false;` | Exclusión mutua ✔, pero si ambos ponen su bandera a la vez, **ambos esperan para siempre** (bloqueo). |
| 3 · Peterson | `indicador[i]=true; turno=j; while(indicador[j] && turno==j); SC; indicador[i]=false;` | Cumple los requisitos para 2 procesos. |
| Panadero (n procesos) | Cada uno toma un número = máx+1; entra el menor (desempata por id) | Funciona para $n$ procesos; usa `escogiendo[]` y `numero[]`. |

**Soluciones por hardware.**

* `Evaluar‑y‑Asignar(&cerradura)` (*test‑and‑set*, atómica): devuelve el valor viejo y deja `true`. Uso: `while (Evaluar‑y‑Asignar(&cerradura)) ; SC; cerradura=false;`
* `Intercambiar(&a,&b)` (*swap*, atómica): `llave=true; do Intercambiar(&cerradura,&llave); while(llave); SC; cerradura=false;`
* Para $n$ procesos con **espera acotada** se añade `esperando[n]` y al salir se entrega la cerradura al siguiente que espera.
* Defecto común: **espera activa** (consume CPU). Inhibir interrupciones solo sirve con un procesador.

**Semáforos.** Variable entera con dos operaciones **atómicas**: `espera(S)` (wait, P) y `señal(S)` (signal, V).

```
espera(S):  S.valor = S.valor - 1;  si S.valor < 0  -> poner el proceso en S.L y bloquearlo
señal(S):   S.valor = S.valor + 1;  si S.valor <= 0 -> sacar un proceso de S.L y despertarlo
```

* Valor **negativo = |valor| procesos bloqueados** en la cola del semáforo.
* **El semáforo vive en el kernel** (contador + cola de procesos). No se guarda en el BCP ni en el espacio del usuario: el proceso solo tiene una **manija**, como un descriptor de fichero. (Pregunta de parcial con clave: "ninguna de las anteriores".)
* Versión simple con espera activa: `while (S <= 0) nada; S--`. El kernel la evita bloqueando en una cola.
* **Semáforo binario**: valor 0/1. Se puede construir un semáforo de conteo con dos binarios y un entero (diapositivas).
* Patrones de inicialización:

| Uso | Valor inicial | Código |
|-----|--------------|--------|
| Exclusión mutua | **1** | `espera(mutex); SC; señal(mutex);` |
| Sincronización / orden ("B espera a A") | **0** | A: `...; señal(sinc);` · B: `espera(sinc); ...` |
| Recurso con $k$ instancias | **k** | `espera(rec); usar; señal(rec);` |

* **Peligro:** el **orden** de los `wait`. P0: `espera(S); espera(Q);` y P1: `espera(Q); espera(S);` pueden quedar cada uno con un semáforo y esperando el otro → **bloqueo mutuo**. Regla: **todos adquieren en el mismo orden**.

**Problemas clásicos (con las inicializaciones que el profe espera).**

| Problema | Semáforos | Nota |
|----------|-----------|------|
| Buffer limitado | `vacíos = n`, `llenos = 0`, `mutex = 1` | Productor: `wait(vacíos); wait(mutex); …; signal(mutex); signal(llenos)`. Consumidor: `wait(llenos); wait(mutex); …; signal(mutex); signal(vacíos)`. Si inviertes `wait(mutex)` y `wait(vacíos)` hay bloqueo. |
| Lectores‑escritores (prioridad a lectores) | `mutex=1`, `escr=1`, `cuentalect=0` | El **primer** lector toma `escr`, el **último** lo libera. Los escritores pueden sufrir inanición. |
| Lectores‑escritores (prioridad a escritores) | 5 semáforos (`mutexlect, mutexescr, mutex, sescr, slect`) | Un escritor que espera bloquea a los lectores nuevos con `slect`. |
| Filósofos | ver §3.4 | La versión ingenua (cada uno toma el tenedor izquierdo y luego el derecho) **se bloquea**. |
| Fumadores | un semáforo por fumador + `SYNC` | ver §3.6‑R7 |
| Jardín ornamental | `mutex` sobre el contador de visitantes; si hay máximo `m`, un semáforo de conteo inicializado en `m` | Dos torniquetes = dos hilos que hacen `contador++` |

**Regiones críticas.** `region v when B do S;` ejecuta `S` en exclusión mutua sobre `v` cuando se cumple la condición `B`. Buffer: productor `region buffer when cuenta < n`, consumidor `region buffer when cuenta > 0`.

**Monitores.** Módulo/objeto donde **solo un proceso a la vez** ejecuta cualquier procedimiento `entry`. La sincronización condicional se hace con **variables de condición** `x` y dos operaciones:

* `x.wait()` suspende al proceso **y libera el monitor** hasta que otro haga `x.signal()` sobre la **misma** condición.
* `x.signal()` despierta a un proceso que espere en `x`. **Si nadie espera, la señal se pierde** (a diferencia del semáforo, el monitor no recuerda).
* Un monitor se parece a **un objeto** (datos privados + métodos que acceden a ellos). Tiene **1 cola de entrada** y una cola de espera por cada variable de condición.

**Sincronización en Java (monitores de Java).**

| Elemento | Qué recordar |
|----------|--------------|
| `synchronized` (método o bloque) | Adquiere el cerrojo del objeto (`this`); se libera al salir, incluso con excepción. Los cerrojos son **por hilo**, no por invocación. |
| Campos `static` | Se protegen con `synchronized (C.class)` o métodos `synchronized static`; bloquear el objeto **no** protege los campos estáticos. (`getClass()` en subclases es incorrecto.) |
| `wait()`, `notify()`, `notifyAll()` | Solo dentro de `synchronized`. Cada objeto tiene **una** cola de espera (una "variable de condición" implícita). |
| Patrón correcto | `while (!condición) wait();` — **siempre `while`**, porque al despertar la condición puede haber cambiado. |
| Qué notificar | Si dudas, **`notifyAll()`**: cada hilo vuelve a comprobar su condición. |
| `Thread` | `start()` ejecuta `run()` como actividad independiente; no se puede reiniciar; `join()` espera la terminación; `sleep`, `yield`, `interrupt`; prioridad 1‑10 (defecto 5, hereda del creador). |
| Objetos "completamente sincronizados" | Todos los métodos `synchronized`, sin campos públicos, métodos finitos, estado consistente al entrar y salir. |

> **Nota sobre las diapositivas.** El buffer limitado en Java de las diapositivas hace `cantidad++` *antes* del `while`; eso es incorrecto. Usa la versión de §3.4.

### 3.2 Método: "¿cuál es el valor de los contadores de los semáforos?"

Pregunta muy frecuente de selección múltiple. Te dan el código de varios procesos, los valores iniciales y **en qué línea va cada proceso** ("han terminado de ejecutar la instrucción *k*").

1. Para cada proceso, cuenta las operaciones `wait`/`signal` en las líneas **≤ k**.
2. **Cuenta el `wait` aunque el proceso se haya quedado bloqueado en él**: el contador ya se decrementó (por eso aparecen valores negativos).
3. $\text{valor final} = \text{inicial} - (\#\text{wait}) + (\#\text{signal})$ por cada semáforo.
4. Un valor negativo $-m$ ⇒ hay $m$ procesos bloqueados en ese semáforo.

Ejemplo `[REAL]` (2013). Semáforos `sem1=1, sem2=0`. Código:

```
P1H1: 2 wait(sem1)  3 //crítica  4 signal(sem1)        P1H2: 2 signal(sem2)
P2H1: 2 wait(sem2)                                       P2H2: 2 wait(sem1)  3 //crítica  4 signal(sem1)
```

* Estado "3 3 3 2" (P1H1 en 3, P1H2 en 3, P2H1 en 3, P2H2 en 2): `sem1 = 1 − wait(P1H1) − wait(P2H2) = −1`; `sem2 = 0 + signal(P1H2) − wait(P2H1) = 0`. **Respuesta: sem1 = −1, sem2 = 0.**
* Estado "2 3 1 5": P1H1 hizo `wait(sem1)` (−1); P1H2 hizo `signal(sem2)` (+1 a sem2); P2H1 aún no hizo nada; P2H2 hizo `wait` y `signal` de `sem1` (neto 0). `sem1 = 1 − 1 = 0`; `sem2 = 0 + 1 = 1`. **Respuesta: sem1 = 0, sem2 = 1.**

Ejemplo `[REAL]` (2014). `sem1=1, sem2=0`; P1 y P4: `wait(sem1) … signal(sem1)`; P2: `signal(sem2)`; P3: `wait(sem2)`. Estado "5 3 3 5": P1 y P4 hicieron wait+signal (neto 0), P2 hizo `signal(sem2)` y P3 `wait(sem2)` ⇒ **sem1 = 1, sem2 = 0**.

### 3.3 Plantillas listas para copiar

**A) Receta para un ejercicio "implemente la clase…" con monitor**

1. Escribe el **estado compartido** (contadores, banderas, orientación…).
2. Para cada método, escribe su **guarda** (la condición para poder continuar).
3. Estructura: `while (!guarda) wait();` → actualizar estado → `notifyAll();` si el cambio puede habilitar a otros.
4. Revisa: ¿alguien puede quedarse dormido para siempre? ¿hay un caso en que nadie llame `notifyAll()`?
5. Si piden "con semáforos": un semáforo por **evento** (inicial 0) o por **recurso** (inicial = nº de instancias), más `mutex` (inicial 1) si hay estado compartido.

**B) Monitor estilo Java**

```java
public class MiMonitor {
    private int estado;                          // 1. estado compartido

    public synchronized void accionA() throws InterruptedException {
        while (!(/* guarda de A */)) wait();     // 2‑3. esperar la condición
        /* actualizar estado */
        notifyAll();                             // 4. despertar a los que puedan avanzar
    }
    public synchronized void accionB() {
        /* actualizar estado */
        notifyAll();
    }
}
```

**C) Monitor en pseudocódigo (estilo Pascal del profe)**

```
monitor BufferLimitado
  var contador, n, entra, sale: integer; buffer: array of Elemento;
      lleno, vacio: condicion;
  procedure entry Poner(e)
    begin
      while contador = n do lleno.wait;
      buffer[entra] := e; entra := (entra+1) mod n; contador := contador+1;
      vacio.signal;
    end
  procedure entry Obtener(var e)
    begin
      while contador = 0 do vacio.wait;
      e := buffer[sale]; sale := (sale+1) mod n; contador := contador-1;
      lleno.signal;
    end
```

> Con señales tipo Hoare basta `if`; con Java/Mesa **usa `while`**. En el examen, `while` nunca está mal.

### 3.4 Código de los problemas clásicos (probado)

**Buffer limitado (monitor Java)**

```java
class BufferLimitado {
    private final Object[] buf; private int entra = 0, sale = 0, cantidad = 0;
    BufferLimitado(int n) { buf = new Object[n]; }
    public synchronized void poner(Object o) throws InterruptedException {
        while (cantidad == buf.length) wait();           // lleno
        buf[entra] = o; entra = (entra + 1) % buf.length; cantidad++;
        notifyAll();
    }
    public synchronized Object obtener() throws InterruptedException {
        while (cantidad == 0) wait();                    // vacío
        Object o = buf[sale]; sale = (sale + 1) % buf.length; cantidad--;
        notifyAll();
        return o;
    }
}
```

**Lectores‑escritores, prioridad a lectores (semáforos)**

```java
Semaphore mutex = new Semaphore(1), escr = new Semaphore(1);  int cuentaLect = 0;
void iniciarLectura()  { mutex.acquire(); if (++cuentaLect == 1) escr.acquire(); mutex.release(); }
void terminarLectura() { mutex.acquire(); if (--cuentaLect == 0) escr.release(); mutex.release(); }
void iniciarEscritura(){ escr.acquire(); }
void terminarEscritura(){ escr.release(); }
```

**Filósofos sin bloqueo (orden jerárquico de tenedores)** — rompe la *espera circular*:

```java
void tomar(int i) { int a = Math.min(i, (i+1)%n), b = Math.max(i, (i+1)%n);
                    tenedor[a].acquire(); tenedor[b].acquire(); }   // siempre el de menor índice primero
void soltar(int i){ int a = Math.min(i, (i+1)%n), b = Math.max(i, (i+1)%n);
                    tenedor[b].release(); tenedor[a].release(); }
```

**Filósofos con estados (solución del capítulo)**: `estado[i] ∈ {PENSANDO, HAMBRE, COMIENDO}`, `mutex=1`, `s[i]=0`.

```
tomar(i):  wait(mutex); estado[i]=HAMBRE; probar(i); signal(mutex); wait(s[i]);
dejar(i):  wait(mutex); estado[i]=PENSANDO; probar(IZQ); probar(DER); signal(mutex);
probar(i): si estado[i]==HAMBRE y estado[IZQ]!=COMIENDO y estado[DER]!=COMIENDO:
              estado[i]=COMIENDO; signal(s[i]);
```

### 3.5 Teoría de selección múltiple (con clave)

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué es una condición de carrera? | Varios procesos leen/escriben datos compartidos y el resultado depende de quién ejecuta y exactamente cuándo. |
| ¿Qué es la exclusión mutua? | La forma clásica de **evitar las condiciones de carrera**. |
| Dos formas de comunicación entre procesos | Compartir variables y enviar eventos (mensajes). |
| Inicialización correcta del productor‑consumidor | `vacíos = n`, `llenos = 0`, `mutex = 1`. |
| ¿Dónde se guarda el contador de un semáforo? | En el **kernel** (estructura del semáforo: contador + cola). No en el BCP. |
| ¿Qué pasa cuando un proceso dentro de un monitor hace `wait` en una condición? | Se **suspende hasta que otro ejecute `signal` en la misma condición**. |
| ¿Qué estructura de datos se parece más a un monitor? | **Un objeto.** |
| Con un proceso ejecutando un método del monitor, ¿cuántos *otros* pueden estar ejecutándose dentro? | **0**. |
| Con $m$ procesos en el sistema y un monitor con $n$ variables de condición, ¿cuántos pueden estar esperando? | **$m-1$** (uno está dentro; los demás esperan en la cola de entrada o en las de condición). |
| ¿Cuántas colas tiene un monitor con $n$ variables de condición? | **1 cola de entrada + $n$ colas de condición** (la clave no aparece en el PDF; es la respuesta estándar). |
| ¿Cuántas variables de condición da `synchronized` en Java? | **Una** (la cola implícita del objeto; la clave no aparece en el PDF). Con `Lock` se pueden crear varias `Condition`. |
| Rango de valores de `sum` si un proceso usa mutex y el otro no (cada uno suma 1, 50 veces) | **mínimo 2, máximo 100** (razonamiento de pérdida de actualizaciones). |

### 3.6 Ejercicios `[REAL]` resueltos

#### R1 · Tres procesos, tres variables, semáforos (taller de esta semana)

> $P_0$ usa $B_0$ y $B_1$ a la vez; $P_1$ usa $B_1$ y $B_2$; $P_2$ usa $B_2$ y $B_0$. Corren concurrentes. Escriba el código con semáforos para coordinar el acceso exclusivo.

Un semáforo **por variable** (`sB0, sB1, sB2`, todos en 1). **La trampa:** si cada proceso pide "primero la suya, luego la siguiente" ($P_2$: `B2` y luego `B0`) puede darse $P_0$ con $B_0$ esperando $B_1$, $P_1$ con $B_1$ esperando $B_2$, $P_2$ con $B_2$ esperando $B_0$ ⇒ **bloqueo circular**. Solución: **siempre en orden de variable**.

```
P0: wait(sB0); wait(sB1);  usar B0,B1;  signal(sB1); signal(sB0);
P1: wait(sB1); wait(sB2);  usar B1,B2;  signal(sB2); signal(sB1);
P2: wait(sB0); wait(sB2);  usar B0,B2;  signal(sB2); signal(sB0);   // B0 ANTES que B2
```

Alternativa que mencionó: un semáforo por *región crítica* (si el ejercicio dibuja varias regiones). Regla que repitió: adquirir **siempre en orden**, primero los recursos de más bajo nivel y luego los de más alto nivel.

#### R2 · Control modular por turnos (2025, semáforos)

> Un control activa $m$ hilos `ControlTask` por turnos rotatorios $0…m-1…0$. En cada `activateTurn()` reactiva la tarea del turno y espera a que ella señale que terminó. Implemente `run()` de `ControlTaskImpl`, `activateTurn()` y el constructor de `ControlImpl`.

Dos semáforos por tarea: `act[i]` (inicial **0**: "es tu turno") y `done[i]` (inicial **0**: "terminé").

```java
public class ControlImpl {
    private int turn = 0;
    private final Semaphore[] act, done;
    public ControlImpl(List<ControlTask> tasks) {
        int m = tasks.size();
        act = new Semaphore[m]; done = new Semaphore[m];
        for (int i = 0; i < m; i++) {
            act[i]  = new Semaphore(0);
            done[i] = new Semaphore(0);
            tasks.get(i).accept(act[i], done[i]);      // le entrega sus dos semáforos
        }
    }
    public void activateTurn() throws InterruptedException {
        act[turn].release();                           // signal: activa la tarea
        done[turn].acquire();                          // wait: espera a que termine
        turn = (turn + 1) % act.length;
    }
}
public class ControlTaskImpl implements ControlTask {
    private Semaphore semActivate, semDone;
    public void accept(Semaphore activate, Semaphore done) { semActivate = activate; semDone = done; }
    public void run() {
        try { while (true) { semActivate.acquire(); /* hacer algo */ semDone.release(); } }
        catch (InterruptedException e) { }
    }
}
```

*Verificado:* con 4 tareas y 10 activaciones el orden de ejecución fue `0,1,2,3,0,1,2,3,0,1`. La solución publicada inicializa `waitTasks[i] = new Semaphore(1)` y no crea los arreglos; con `1` el control **no esperaría** a que la tarea termine. Debe ser `0`.

#### R3 · Fábrica de aviones OMG (2020, monitor)

> Llegan alas izquierdas y derechas en orden aleatorio. Cuando el sistema completa **una derecha y una izquierda** (en cualquier orden) procede a la siguiente etapa. Implemente el monitor de recepción.

Idea: cada ala que llega **empareja** con una del lado contrario que esté esperando (la libera y ambas continúan); si no hay pareja, **espera**.

```java
class RecepcionAlas {
    private int izqEsperando = 0, derEsperando = 0;      // alas sin pareja
    private int izqLiberadas = 0, derLiberadas = 0;      // permisos ya concedidos a las que esperan
    public synchronized void llegaIzquierda() throws InterruptedException {
        if (derEsperando > 0) { derEsperando--; derLiberadas++; notifyAll(); }   // forma par y libera la derecha
        else { izqEsperando++; while (izqLiberadas == 0) wait(); izqLiberadas--; }
    }
    public synchronized void llegaDerecha() throws InterruptedException {
        if (izqEsperando > 0) { izqEsperando--; izqLiberadas++; notifyAll(); }
        else { derEsperando++; while (derLiberadas == 0) wait(); derLiberadas--; }
    }
}
```

*Verificado* con 133 izquierdas y 67 derechas: se formaron 67 pares; al llegar las 66 derechas que faltaban se completaron los 133 y ningún hilo quedó bloqueado.

#### R4 · Cerrojo con llaves (2020, monitor)

> Un cerrojo gira en sentido horario Norte→Este→Sur→Oeste. Está orientado al Este y solo admite llaves orientadas al Este. Si una llave coincide, entra y el cerrojo avanza a la siguiente posición; si no, espera. El administrador puede girar el cerrojo una posición.

```java
class Cerrojo {
    private int actual = 1;                    // 0=Norte, 1=Este, 2=Sur, 3=Oeste
    public synchronized void usar(int llave) throws InterruptedException {
        while (actual != llave) wait();        // espera a que el cerrojo coincida
        actual = (actual + 1) % 4;             // gira a la siguiente posición
        notifyAll();                           // alguna llave pudo quedar habilitada
    }
    public synchronized void girar() { actual = (actual + 1) % 4; notifyAll(); }   // administrador
}
```

*Verificado:* 4 llaves (una por orientación) usando el cerrojo 3 veces entran en el orden `E,S,O,N,E,S,O,N,E,S,O,N` y ninguna queda bloqueada; una llave `OESTE` sola entra después de que el administrador gira dos veces.

#### R5 · Banquero concurrente (2019, monitor)

> `ControlBanquero.solicitarRecursos(vector)` devuelve `true` si asignó (el estado queda seguro) o `false` si no; `liberarRecursos(vector)` libera. Escriba `ControlConcurrenteBanquero` con monitores: si la solicitud no se puede conceder, el hilo duerme hasta que ocurra una liberación y reintenta.

```java
public class ControlConcurrenteBanquero {
    private final ControlBanquero banquero;
    public ControlConcurrenteBanquero(ControlBanquero b) { this.banquero = b; }
    public synchronized void solicitarRecursos(int[] solicitud) throws InterruptedException {
        while (!banquero.solicitarRecursos(solicitud)) wait();   // reintenta tras cada liberación
    }
    public synchronized void liberarRecursos(int[] liberacion) {
        banquero.liberarRecursos(liberacion);
        notifyAll();                                             // todos reintentan
    }
}
```

La versión Pascal publicada tiene la condición invertida (`== True`); la correcta es esperar **mientras la solicitud NO se conceda**. El mismo patrón sirve para el **monitor de memoria** (`ControlConcurrenteMemoria`): `while ((ma = manejador.solicitarMemoria(c)) == null) wait(); return ma;` y al liberar `manejador.liberar(ma); notifyAll();`.

#### R6 · Monitor `Resource` y "retener y esperar" (2015)

El monitor original: `getResource()` hace `if (!assigned) { assigned = true; owner = pid }` y **si está ocupado no hace nada** (no espera). Corrección (versión del profe, con variable de condición `waitRsrc`): si está asignado, `waitRsrc.wait`; al liberar `waitRsrc.signal`. Versión robusta en Java:

```java
class Resource {
    private boolean assigned = false; private long owner;
    public synchronized void getResource() throws InterruptedException {
        while (assigned) wait();
        assigned = true; owner = Thread.currentThread().getId();
    }
    public synchronized void freeResource() {
        if (assigned && owner == Thread.currentThread().getId()) { assigned = false; notify(); }
    }
}
```

Parte (b): con cuatro procesos `f: r1,r2,r4 · g: r1,r3 · h: r2,r3 · i: r3,r4`, **no puede haber bloqueo** porque todos piden los recursos en un orden global creciente (`r1<r2<r3<r4`) y los liberan en orden inverso ⇒ se elimina la **espera circular**. (El profe pedía modelar un escenario con bloqueo y otro sin; la respuesta esperada es que con este orden el escenario con bloqueo **no existe**.)

#### R7 · Fumadores (2015, semáforos)

```
enum SEM = { NOTABACO, NOPAPEL, NOCERILLAS, SYNC };   sem sems[4] = {0,0,0,0};

agente():  for(;;){ v = Random(3);        // el agente escoge qué ingrediente falta
                    signal(sems[v]);       // despierta al fumador que tiene lo que falta
                    wait(sems[SYNC]); }    // espera a que el fumador termine
fumador(propio, agente): for(;;){ wait(propio); fumar(); signal(agente); }
main: lanzar 3 fumadores (sems[NOTABACO], sems[NOPAPEL], sems[NOCERILLAS]) con SYNC y el agente
```

#### R8 · Contadores de semáforos y otras `[REAL]`

Ver §3.2 (ejemplos 2013 y 2014) y la tabla de §3.5.

### 3.7 Cómo atacar un enunciado largo de concurrencia

1. Subraya **los métodos que debes escribir** y **las clases/figura** que te dan.
2. Lista las **reglas** del relato como frases de una línea ("la llave espera hasta que coincida la orientación", "el par se forma con una izquierda y una derecha").
3. Decide **qué estado** necesitas (contadores / banderas / orientación) y **quién lo cambia**.
4. Escribe la guarda de cada método y el `notifyAll()`.
5. Prueba mentalmente tres casos: *llega primero uno*, *llegan dos opuestos*, *llegan muchos del mismo tipo*.

### 3.8 Ejercicios `[HIP]` con solución

#### H‑C1 · Contadores de semáforos (estilo parcial)

```
sem_t a = 1, b = 0, c = 0;
P1: 1 //antes  2 wait(&a)  3 //crítica  4 signal(&b)  5 //resto
P2: 1 //antes  2 wait(&b)  3 //crítica  4 signal(&c)  5 //resto
P3: 1 //antes  2 wait(&c)  3 //crítica  4 signal(&a)  5 //resto
```

¿Valor de `a, b, c` si (i) P1=4, P2=3, P3=2? (ii) P1=5, P2=4, P3=2? (iii) P1=2, P2=2, P3=2?

* (i) `a = 1−1 = 0` (P1 hizo wait(a)); `b = 0+1−1 = 0` (signal de P1, wait de P2); `c = 0−1 = −1` (P3 hizo `wait(c)` y P2 aún no señala) ⇒ **a=0, b=0, c=−1** (P3 bloqueado).
* (ii) `a = 1−1 = 0`; `b = 0+1−1 = 0`; `c = 0+1−1 = 0` (P2 señaló c y P3 lo consumió) ⇒ **a=0, b=0, c=0**.
* (iii) `a = 0` (P1 pasó); `b = −1` (P2 bloqueado); `c = −1` (P3 bloqueado) ⇒ **a=0, b=−1, c=−1**.

Variante con la figura 2014 (`sem1=1, sem2=0`; P1,P4: `wait(sem1)…signal(sem1)`; P2: `signal(sem2)`; P3: `wait(sem2)`) en el estado "2 2 2 2": `sem1 = 1−1−1 = −1`, `sem2 = 0+1−1 = 0` ⇒ **sem1=−1, sem2=0**.

#### H‑C2 · Puente de un solo carril (monitor)

> Un puente admite hasta 3 carros a la vez, **todos del mismo sentido**. Nunca cruzan carros de sentidos opuestos. Implemente `entrar(sentido)` y `salir()`.

```java
class Puente {
    private int enPuente = 0, sentido = -1;      // -1: libre, 0: norte→sur, 1: sur→norte
    private final int MAX;
    Puente(int max) { MAX = max; }
    public synchronized void entrar(int s) throws InterruptedException {
        while (!(sentido == -1 || sentido == s) || enPuente >= MAX) wait();
        sentido = s; enPuente++;
    }
    public synchronized void salir() {
        enPuente--;
        if (enPuente == 0) sentido = -1;          // queda libre: puede entrar cualquier sentido
        notifyAll();
    }
}
```

*Verificado* con 60 hilos (30 por sentido): 0 violaciones de exclusión por sentido ni de capacidad, ningún bloqueo. Observación para el examen: esta solución puede causar **inanición** de un sentido; si el enunciado pide equidad, añade un contador de turnos o una cola FIFO.

#### H‑C3 · Barrera reutilizable (monitor)

> $n$ hilos deben esperarse unos a otros al final de cada fase antes de empezar la siguiente.

```java
class Barrera {
    private final int n; private int llegados = 0, generacion = 0;
    Barrera(int n) { this.n = n; }
    public synchronized void esperar() throws InterruptedException {
        int miGen = generacion;
        if (++llegados == n) { llegados = 0; generacion++; notifyAll(); }
        else while (miGen == generacion) wait();   // la "generación" evita despertares espurios
    }
}
```

*Verificado* con 5 hilos y 20 fases: ningún hilo avanzó antes de que todos terminaran la fase.

#### H‑C4 · Tres hilos imprimen A B C en orden (semáforos)

```java
Semaphore a = new Semaphore(1), b = new Semaphore(0), c = new Semaphore(0);
// A: repetir { a.acquire(); print("A"); b.release(); }
// B: repetir { b.acquire(); print("B"); c.release(); }
// C: repetir { c.acquire(); print("C"); a.release(); }
```

Cada semáforo significa "es el turno de…". Solo `a` empieza en 1. Es el mismo patrón de `ControlImpl` (R2).

#### H‑C5 · ¿Qué pasa si inicializo mal el productor‑consumidor?

| Inicialización | Consecuencia |
|---------------|--------------|
| `vacíos=n, llenos=0, mutex=1` | Correcta |
| `mutex = 0` | Nadie pasa `wait(mutex)`: **bloqueo total** |
| `vacíos = 0` | El productor nunca produce; el consumidor espera en `llenos=0`: **bloqueo total** |
| `vacíos=0, llenos=n, mutex=0` (la figura del parcial 2014) | Incorrecta: `mutex=0` bloquea a todos |
| Productor con `wait(mutex)` **antes** de `wait(vacíos)` | Con el buffer lleno el productor retiene `mutex` esperando `vacíos` y el consumidor no puede entrar para liberar: **bloqueo** |
| Sin `mutex` y 2 productores | Condición de carrera sobre `entra`/`contador` |

#### H‑C6 · Diez preguntas de selección múltiple (con respuesta)

1. Un semáforo vale −3. → **Hay 3 procesos bloqueados en su cola.**
2. Valor inicial de un semáforo de exclusión mutua. → **1.**
3. Para que B ejecute solo *después* de que A termine su tarea, el semáforo de sincronización se inicia en → **0.**
4. ¿Dónde está el contador de un semáforo? → **En el kernel, no en el BCP.**
5. ¿Por qué la señal de un monitor "se pierde" y la de un semáforo no? → **El monitor no tiene memoria; el semáforo sí (acumula en el contador).**
6. ¿Por qué `while (!cond) wait();` y no `if`? → **Porque al despertar la condición pudo cambiar (varios despertados, semántica de Java).**
7. ¿Cuántos procesos pueden ejecutar código dentro de un monitor a la vez? → **Uno.**
8. ¿Cómo proteges un campo `static` en Java? → **`synchronized (Clase.class)` o método `synchronized static`.**
9. ¿Qué requisito viola el algoritmo de turno estricto? → **El de progreso: si nadie está en la sección crítica, quien quiera entrar debe poder hacerlo sin dilación.**
10. ¿Qué es espera activa y cómo la evita el kernel en los semáforos? → **Es repetir una comprobación consumiendo CPU; el kernel bloquea al proceso en la cola del semáforo.**
---

## 4. Tema 2 · Bloqueos (interbloqueos)

### 4.1 Teoría mínima

**Modelo del sistema.** Hay tipos de recursos con varias instancias idénticas. Un proceso usa un recurso en tres pasos: **Solicitar → Usar → Liberar**. Si no se puede satisfacer la solicitud, el proceso **espera**. (Pregunta con clave: la operación **bloqueante** es **Solicitar**; usar y liberar no.)

**Bloqueo mutuo.** Conjunto de procesos donde cada uno espera un recurso que tiene otro del conjunto (ejemplo del capítulo: dos trenes en un cruce).

**Las 4 condiciones necesarias (deben darse las cuatro a la vez):**

| Condición | Significado |
|-----------|------------|
| **Exclusión mutua** | Al menos un recurso no es compartible: solo un proceso a la vez lo usa. |
| **Retener y esperar** | Un proceso *conserva* los recursos que ya tiene mientras espera otros que están asignados a otros procesos. (Clave del parcial: "la llamada para solicitar un recurso no libera los recursos actuales del proceso, pero si el solicitado está asignado a otro, este tiene que esperar a que sea liberado".) |
| **No expropiación** | Los recursos no se pueden quitar: se liberan voluntariamente. |
| **Espera circular** | $P_0$ espera a $P_1$, $P_1$ a $P_2$, …, $P_{n-1}$ a $P_0$. |

**Grafo de asignación de recursos.** Nodos: procesos $P_i$ y tipos de recurso $R_j$ (las instancias se dibujan como puntos). Arista $P_i \to R_j$ = **solicitud** (el proceso espera); arista $R_j \to P_i$ = **asignación**.

* Sin ciclos ⇒ no hay bloqueo.
* Con **una sola instancia por recurso**, ciclo ⇒ **bloqueo**.
* Con **varias instancias**, el ciclo es condición *necesaria pero no suficiente* (el capítulo muestra un grafo con ciclo y sin bloqueo).

**Tres formas de manejar el problema:** (1) **prevenir/evitar** con un protocolo; (2) **permitir** el bloqueo, **detectarlo** y **recuperarse**; (3) **ignorarlo** (política del avestruz).

**Prevención: negar una de las cuatro condiciones**

| Condición | Cómo se niega | Inconveniente |
|-----------|---------------|--------------|
| Exclusión mutua | Hacer compartibles los recursos que se pueda (p. ej. archivos de solo lectura) | Casi nunca se puede: algunos recursos son intrínsecamente no compartibles |
| Retener y esperar | Pedir **todos los recursos a la vez**, o pedirlos de uno en uno **liberando** los que se tienen antes de pedir más | Baja utilización de recursos; posible inanición |
| No expropiación | Si pides un recurso ocupado se te **quitan** los que tienes; o solo se quita lo que otro proceso solicite | Hay que poder guardar/restaurar el estado del recurso |
| Espera circular | Numerar los recursos con $F:R\to\mathbb{N}$ y **solo pedir en orden creciente** (o liberar los de $F\ge F(R_j)$ antes de pedir $R_j$); varias instancias del mismo tipo se piden en **una sola** solicitud | Obliga a un orden global |

**Evitar (con información adicional).** Cada proceso declara su **máximo**. Un **estado es seguro** si existe una **secuencia segura** $\langle P_1,\dots,P_n\rangle$: para cada $P_i$ lo que aún puede pedir se satisface con lo disponible más lo que tienen los $P_j$ con $j<i$. Si no existe, es **inseguro** (puede llevar al bloqueo; no siempre lo hace). Un sistema puede pasar de seguro a inseguro por una asignación.

Ejemplo del capítulo (12 cintas): $P_0$ máx 10 tiene 5; $P_1$ máx 4 tiene 2; $P_2$ máx 9 tiene 2. Disponibles 3. Seguro con $\langle P_1,P_0,P_2\rangle$. Si $P_2$ pide 1 más, disponible 2, $P_1$ termina (→4) pero $P_0$ necesita 5 y $P_2$ 6 ⇒ **inseguro**.

* **Una instancia por recurso:** *algoritmo del grafo con aristas de reclamo* (§4.3‑A).
* **Varias instancias:** **algoritmo del banquero** (§4.3‑B).

**Detección.** Se deja que ocurra y se verifica periódicamente.

* **Una instancia por recurso:** *grafo de espera* ($P_i\to P_j$ si $P_i$ espera un recurso de $P_j$). Hay bloqueo ⇔ hay ciclo.
* **Varias instancias:** algoritmo con `Disponible`, `Asignación`, `Solicitud` (§4.3‑C). Cuesta del orden de $m\times n^2$ operaciones.
* **¿Cuándo invocarlo?** Depende de (1) con qué frecuencia es probable un bloqueo y (2) a cuántos procesos afectaría.

**Recuperación.**

| Estrategia | Detalle |
|-----------|---------|
| Terminar procesos | **Todos** los bloqueados, o **uno por uno** hasta romper el ciclo. Factores para elegir: prioridad; tiempo ejecutado y que le falta; recursos usados y de qué tipo; recursos adicionales que necesita; cuántos procesos habría que abortar; interactivo o por lotes. |
| Expropiar recursos | **Selección de la víctima** (minimizar costo), **retroceso** (devolver el proceso a un estado seguro y reiniciarlo desde allí) y evitar **inanición** (que siempre sea la misma víctima). Se combinan las estrategias. |

**Relación con la concurrencia.** Dos semáforos pedidos en distinto orden por dos procesos producen las cuatro condiciones (el semáforo es exclusión mutua; cada proceso retiene uno y espera el otro; no hay expropiación; la espera es circular). **Solución universal: orden global de adquisición.**

### 4.2 ¿Qué algoritmo uso?

| Si el enunciado dice… | Algoritmo | Matrices |
|-----------------------|-----------|----------|
| "Muestre el estado en $t_{i+5}$… grafo… solicitudes en $t_i$, $t_{i+1}$…" | Grafo con aristas de reclamo (evitar) | Un dibujo |
| "Matriz Necesidad", "¿estado seguro?", "¿puede concederse la solicitud?" | **Banquero** | `Disponible`, `Max`, `Asignación`, `Necesidad = Max − Asignación` |
| "Aplique el algoritmo de detección", "¿qué procesos están bloqueados?" | **Detección** | `Disponible`, `Asignación`, `Solicitud` (no hay `Max`) |
| "Menor valor de $x$ para que el estado sea seguro" | Banquero con $x$ desconocida | Pruebas $x=0,1,2,…$ |

**Diferencias que más se confunden:**

| | Banquero (seguridad) | Detección |
|--|---------------------|-----------|
| Compara con | `Necesidad` (lo que *podría* pedir) | `Solicitud` (lo que *está pidiendo ahora*) |
| `Fin[i]` inicial | falso para todos | verdadero si `Asignación[i]` es todo ceros |
| Pregunta | ¿Puedo garantizar que todos terminen? | ¿Quién está bloqueado ahora? |

### 4.3 Procedimientos paso a paso

#### A) Grafo con aristas de reclamo ("muestre el estado en $t_{i+k}$")

El grafo trae, además de nodos, **aristas punteadas** $P\dashrightarrow R$ = "este proceso podrá pedir ese recurso". Para **cada evento** "$P$ solicita $R$":

1. Si $R$ está **ocupado** → $P$ **espera** (arista de solicitud $P\to R$). Queda bloqueado.
2. Si $R$ está **libre**: *simula* la asignación (convierte la arista $P\to R$ en $R\to P$) y busca **ciclos** considerando las aristas punteadas.
   * **Sin ciclo** → estado seguro → **se asigna**.
   * **Con ciclo** → estado inseguro → **no se asigna** y $P$ queda **bloqueado** (aunque $R$ esté libre).
3. Al terminar los eventos, responde las tres preguntas: *procesos bloqueados*, *recursos asignados*, *recursos sin asignar*.

Escribe en el examen cuál es el ciclo que encontraste (p. ej. $R_0\to P_0\to R_2\to P_1\to R_0$).

#### B) Banquero

*Datos:* `n` procesos, `m` tipos. $\text{Necesidad}[i,j]=\text{Max}[i,j]-\text{Asignación}[i,j]$. Total de cada recurso = suma de lo asignado + disponible (así se *verifica* un `Disponible`).

*Algoritmo de seguridad:*

1. `Trabajo = Disponible`, `Fin[i] = falso` para todo $i$.
2. Busca $i$ con `Fin[i]=falso` **y** `Necesidad[i] ≤ Trabajo`. Si no existe, ve al paso 4.
3. `Trabajo = Trabajo + Asignación[i]`, `Fin[i] = verdadero`; vuelve al paso 2.
4. Si `Fin[i]` es verdadero para todos → **estado seguro** (la secuencia en que fuiste marcando es una *secuencia segura*; puede haber varias distintas, todas válidas).

*Algoritmo de solicitud ($P_i$ pide `Solicitud`):*

1. Si `Solicitud ≤ Necesidad[i]` sigue; si no → **error** (excede su máximo).
2. Si `Solicitud ≤ Disponible` sigue; si no → $P_i$ **espera** (no hay recursos).
3. Simula: `Disponible −= Solicitud`; `Asignación[i] += Solicitud`; `Necesidad[i] −= Solicitud`. Ejecuta el algoritmo de seguridad: **seguro → se concede; inseguro → no se concede** y se restaura el estado.

*Presentación sugerida:* escribe la tabla de `Necesidad`, luego las líneas `Trabajo = …` con el proceso elegido en cada paso.

#### C) Detección con varias instancias

1. `Trabajo = Disponible`. `Fin[i] = verdadero` si `Asignación[i]` es todo ceros; si no, `falso`.
2. Busca $i$ con `Fin[i]=falso` y `Solicitud[i] ≤ Trabajo`. Si no hay, ve al paso 4.
3. `Trabajo += Asignación[i]`; `Fin[i]=verdadero`; repite desde 2.
4. Todo `Fin[i]` en `falso` al final ⇒ **ese proceso está en bloqueo**. Si todos son verdaderos, **no hay bloqueo**.

#### D) "Menor valor de $x$"

Prueba $x=0,1,2…$ en `Disponible`/`Asignación` y aplica seguridad; el primero que da seguro es la respuesta (en el parcial 2015 el profe lo hizo así: resultó **$x=1$**).

### 4.4 Ejercicios `[REAL]` resueltos

#### D‑R1 · Tres procesos, seis recursos (taller de esta semana)

Reconstruido de la grabación del taller (la figura/código está en el parcial original):
$P_0$: `get A, get B, get C` · $P_1$: `get D, get E, get B` · $P_2$: `get C, get F, get D`.

* **Mostrar el bloqueo (grafo de asignación).** Se intercala así: $P_0$ obtiene A y B; $P_1$ obtiene D y E; $P_2$ obtiene C y F. Ahora $P_0$ pide C (lo tiene $P_2$), $P_2$ pide D (lo tiene $P_1$) y $P_1$ pide B (lo tiene $P_0$) ⇒ **ciclo** $P_0\to C\to P_2\to D\to P_1\to B\to P_0$ ⇒ bloqueo mutuo. El profe insistió: *para que haya bloqueo los procesos deben ejecutarse "a trozos" en órdenes distintos*; no hace falta que un proceso termine antes que otro.
* **Prevenir cambiando solo el orden de los `get`** (sin mover pedidos entre procesos): impone el orden global $A<B<C<D<E<F$ → $P_0$: A,B,C (ya está) · $P_1$: **B, D, E** · $P_2$: **C, D, F**. Con eso ningún ciclo es posible.
* **Segunda solución** que mencionó: pedir **todos los recursos de un proceso en una sola operación** (niega *retener y esperar*): quien lo pida primero se queda con todo y el otro espera.

#### D‑R2 · Evitar con el grafo (30‑oct‑2025)

Eventos: $t_i$: P0→R0 · $t_{i+1}$: P2→R1 · $t_{i+2}$: P3→R3 · $t_{i+3}$: P3→R4 · $t_{i+4}$: P1→R2. Solución oficial: las cuatro primeras asignaciones **no forman ciclo** y se aceptan. En $t_{i+4}$, asignar R2 a P1 produce **dos ciclos** ($R_0\to P_0\to R_2\to P_1\to R_0$ y $R_2\to P_1\to R_3\to P_3\to R_2$) ⇒ estado **inseguro** ⇒ **no se asigna y se bloquea a P1**.

| Pregunta | Respuesta |
|----------|-----------|
| ¿Seguro? | Con las 5 asignaciones, **no**. |
| ¿Qué debería pasar? | No conceder R2 a P1 (queda bloqueado). |
| Recursos asignados | R0→P0, R1→P2, R3→P3, R4→P3 |
| Sin asignar | R2 |

(En 2020 hubo dos versiones con eventos como "P0→R0, P1→R0, P2→R2, P2→R1, P3→R4"; el patrón de resolución es el mismo: un recurso ocupado deja al solicitante esperando, y una asignación que cierra un ciclo con las aristas punteadas se rechaza.)

#### D‑R3 · Detección (7‑may‑2020 y 30‑oct‑2025)

Recursos R0‑R3. `Disponible = (2,1,0,0)`.

$$\text{Solicitud}=\begin{pmatrix}2&0&0&1\\1&0&1&0\\2&1&0&0\end{pmatrix},\qquad \text{Asignación}=\begin{pmatrix}0&0&1&0\\2&0&0&1\\0&1&2&0\end{pmatrix}$$

* **Caso base.** `Trabajo=(2,1,0,0)`. P2 pide (2,1,0,0) ≤ Trabajo ⇒ termina: `Trabajo = (2,1,0,0)+(0,1,2,0) = (2,2,2,0)`. P0 pide (2,0,0,1): no hay R3 ⇒ aún no. P1 pide (1,0,1,0) ≤ (2,2,2,0) ⇒ termina: `Trabajo = (2,2,2,0)+(2,0,0,1) = (4,2,2,1)`. Ahora P0 pide (2,0,0,1) ≤ (4,2,2,1) ⇒ termina: `Trabajo=(4,2,3,1)`. Secuencia **⟨P2,P1,P0⟩** ⇒ **no hay bloqueo.** (La solución publicada escribe ⟨P2,P0,P1⟩, pero sus números —`Trabajo=(4,2,2,1)`— corresponden a sumar la asignación de P1; P0 solo puede ir después de P1 porque necesita R3.)
* **Variante:** P1 pide **dos ejemplares más de R0** ⇒ `Solicitud[1]=(3,0,1,0)`. `Trabajo=(2,1,0,0)` → P2 termina → `(2,2,2,0)`. P0 necesita R3 (0 disponibles) y P1 necesita 3 de R0 (hay 2) ⇒ ninguno avanza ⇒ **P0 y P1 están en bloqueo mutuo.**

#### D‑R4 · Banquero con 4 tipos de recursos (7‑may‑2020)

`Disponible=(2,1,0,0)`.

| | Max | Asignación | **Necesidad = Max − Asig** |
|--|-----|-----------|------------------------|
| P0 | 0 0 1 2 | 0 0 1 2 | **0 0 0 0** |
| P1 | 2 7 5 0 | 2 0 0 0 | **0 7 5 0** |
| P2 | 6 6 5 6 | 0 0 3 4 | **6 6 2 2** |
| P3 | 4 3 5 5 | 2 3 5 4 | **2 0 0 1** |
| P4 | 0 6 5 2 | 0 3 3 2 | **0 3 2 0** |

* **¿Seguro?** `Trabajo=(2,1,0,0)` → P0 (necesita 0): `(2,1,1,2)` → P3 (2,0,0,1): `(4,4,6,6)` → P4 (0,3,2,0): `(4,7,9,8)` → P1 (0,7,5,0): `(6,7,9,8)` → P2 (6,6,2,2): `(6,7,12,12)`. **Seguro**, secuencia ⟨P0,P3,P4,P1,P2⟩.
* **Solicitud de P2 = (0,1,0,0).** (0,1,0,0) ≤ Necesidad ✔; ≤ Disponible ✔. Simulación: `Disponible=(2,0,0,0)`, `Asig[P2]=(0,1,3,4)`, `Nec[P2]=(6,5,2,2)`. Seguridad: P0 → `(2,0,1,2)`; P3 → `(4,3,6,6)`; P4 → `(4,6,9,8)`; P1 necesita 7 de R1 (hay 6) ✗; P2 necesita 6 de R0 (hay 4) ✗. **Inseguro ⇒ no se concede.**

#### D‑R5 · Banquero con 6 procesos y `Disponible` mal calculado (10‑may‑2018)

Recursos totales A=15, B=6, C=9, D=10. Asignado:
P0 (2,0,2,1) · P1 (0,1,1,1) · P2 (4,1,0,2) · P3 (1,0,0,1) · P4 (1,1,0,0) · P5 (1,0,0,1). Máximo:
P0 (8,5,5,5) · P1 (2,2,3,3) · P2 (7,5,4,4) · P3 (3,3,3,2) · P4 (5,2,2,1) · P5 (4,4,3,4). El enunciado daba `Disponible = (7,2,5,5)`.

* **a) Verificar `Disponible`:** suma de lo asignado = (9,3,3,6). Disponible real = (15,6,9,10) − (9,3,3,6) = **(6,3,6,4)**. **El del enunciado estaba mal.**
* **b) Necesidad:** P0 (6,5,3,4) · P1 (2,1,2,2) · P2 (3,4,4,2) · P3 (2,3,3,1) · P4 (4,1,2,1) · P5 (3,4,3,3).
* **c) Seguro:** `(6,3,6,4)` → P1 → `(6,4,7,5)` → P2 → `(10,5,7,7)` → P3 → `(11,5,7,8)` → P4 → `(12,6,7,8)` → P5 → `(13,6,7,9)` → P0 → `(15,6,9,10)`. Secuencia P1,P2,P3,P4,P5,P0 (la oficial). El orden que obtiene un algoritmo que siempre toma "el primer índice disponible" es P1,P2,P0,P3,P4,P5; **ambas son válidas**.
* **d) Solicitud (3,3,3,3) de P5:** ≤ Necesidad (3,4,3,3) ✔ y ≤ Disponible ✔; tras simular, `Disponible=(3,0,3,1)` y **ningún** proceso puede completarse ⇒ **inseguro, no se concede.**

#### D‑R6 · Banquero con un solo recurso (25‑oct‑2018)

150 unidades de memoria; proceso 1 (máx 70, tiene 45), 2 (60, 40), 3 (60, 15). Disponible = 150 − 100 = 50.

* **a)** Llega un 4.º con máx 60 y necesidad inicial 25 ⇒ disponible 25; necesidades: P1 25, P2 20, P3 45, P4 35. P1 (25 ≤ 25) → 25+45=70 → P2 → … **Seguro.**
* **b)** 4.º con máx 60 y necesidad inicial 35 ⇒ disponible 15; necesidades: P1 25, P2 20, P3 45, P4 25 → ninguno ≤ 15 ⇒ **inseguro, no se admite.**

#### D‑R7 · Menor $x$ que hace seguro el estado (14‑may‑2015)

5 tipos de recursos, `Disponible = (0,0,x,1,2)`. Asignación/Máximo: A (1,0,2,1,1)/(1,1,2,1,3) · B (2,0,1,1,0)/(2,2,2,1,0) · C (1,1,0,1,0)/(2,1,3,1,0) · D (1,1,1,1,0)/(1,1,2,2,1). Necesidades: A (0,1,0,0,2), B (0,2,1,0,0), C (1,0,3,0,0), D (0,0,1,1,1). Con $x=0$ nadie puede avanzar (D necesita 1 de R2) ⇒ inseguro. Con **$x=1$**: D termina → `(1,1,2,2,2)` → A → `(2,1,4,3,3)` → C → `(3,2,4,4,3)` → B. **Respuesta: $x=1$.** (Verificado también por fuerza bruta. La solución publicada lista D, A, B, C, pero B necesita 2 de R1 y en ese punto solo hay 1; el orden válido es D, A, C, B. La respuesta $x=1$ no cambia.)

#### D‑R8 · Ejemplo del capítulo (banquero de 5 procesos y 3 recursos)

A=10, B=5, C=7. Asignado: P0 (0,1,0), P1 (2,0,0), P2 (3,0,2), P3 (2,1,1), P4 (0,0,2). Max: P0 (7,5,3), P1 (3,2,2), P2 (9,0,2), P3 (2,2,2), P4 (4,3,3). `Disponible=(3,3,2)`. Necesidad: P0 (7,4,3), P1 (1,2,2), P2 (6,0,0), P3 (0,1,1), P4 (4,3,1). Seguro (p. ej. ⟨P1,P3,P4,P2,P0⟩).

* P1 pide (1,0,2): se concede (estado sigue seguro, ⟨P1,P3,P4,P0,P2⟩).
* Luego P4 pide (3,3,0): **no hay disponible suficiente** (espera).
* Luego P0 pide (0,2,0): hay disponible, pero el estado resultante es **inseguro** ⇒ **no se concede.**

#### D‑R9 · Preguntas cortas con clave

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué significa "retener y esperar"? | No liberar los recursos actuales al pedir uno nuevo que está ocupado; el proceso espera con lo que tiene. |
| De solicitar/utilizar/liberar, ¿cuál es bloqueante? | **Solicitar.** |
| En el monitor `Resource` con 4 procesos que piden en orden `r1<r2<r3<r4` y liberan al revés, ¿puede haber bloqueo? | **No**: se elimina la espera circular. |

### 4.5 Ejercicios `[HIP]` con solución

#### H‑D1 · Banquero completo (estilo 2018/2020)

Sistema con 5 procesos y 3 tipos de recursos: **A=10, B=7, C=8**.

| | Asignado (A B C) | Máximo (A B C) |
|--|--|--|
| P0 | 1 1 2 | 5 3 4 |
| P1 | 2 1 1 | 4 2 2 |
| P2 | 2 0 2 | 6 1 3 |
| P3 | 1 2 1 | 3 4 2 |
| P4 | 0 1 1 | 2 3 3 |

a) Calcule `Disponible`. b) Calcule `Necesidad`. c) ¿Es seguro? d) P1 solicita (1,0,1): ¿se concede? e) Con el estado original, P0 solicita (3,0,0): ¿se concede? f) P2 solicita (0,1,2). g) P4 solicita (1,0,1).

**Solución.**

* a) Asignado total = (6,5,7); **Disponible = (10,7,8) − (6,5,7) = (4,2,1).**
* b) **Necesidad:** P0 (4,2,2) · P1 (2,1,1) · P2 (4,1,1) · P3 (2,2,1) · P4 (2,2,2).
* c) `Trabajo=(4,2,1)` → P1 (2,1,1)✔ → (6,3,2) → P0 (4,2,2)✔ → (7,4,4) → P2 (4,1,1)✔ → (9,4,6) → P3 (2,2,1)✔ → (10,6,7) → P4 (2,2,2)✔ → (10,7,8). **Seguro: ⟨P1,P0,P2,P3,P4⟩.**
* d) (1,0,1) ≤ Necesidad (2,1,1) ✔ ≤ Disponible ✔. Simulado: Disponible (3,2,0), Nec[P1]=(1,1,0). P1 (1,1,0)✔ → (6,3,2) → … el resto sigue pasando. **Seguro ⇒ se concede.**
* e) (3,0,0) ≤ Necesidad ✔ ≤ Disponible ✔. Simulado: Disponible (1,2,1). Nadie puede continuar (P1 necesita 2 de A, P0 necesita 2 de C, …). **Inseguro ⇒ P0 espera.**
* f) (0,1,2): pide 2 de C pero su necesidad de C es 1 ⇒ **error: excede su máximo.**
* g) (1,0,1) ≤ Necesidad (2,2,2) ✔ ≤ Disponible ✔. Simulado: Disponible (3,2,0): nadie puede completarse (todos necesitan al menos 1 de C). **Inseguro ⇒ P4 espera.**

#### H‑D2 · Detección (dos versiones)

4 procesos, 3 recursos de una instancia cada uno. `Disponible=(0,0,0)`.

$$\text{Asignación}=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\\0&0&0\end{pmatrix},\quad \text{Solicitud}=\begin{pmatrix}0&1&0\\1&0&0\\0&0&0\\0&0&1\end{pmatrix}$$

a) ¿Hay bloqueo? b) ¿Y si P1 solicitara (0,0,1) en vez de (1,0,0)?

**Solución.**

* a) `Trabajo=(0,0,0)`. `Fin` inicial: P3 = **verdadero** (no tiene nada asignado), los demás falso. P2 pide (0,0,0) ≤ Trabajo ⇒ termina, `Trabajo=(0,0,1)`. P0 pide (0,1,0) ✗; P1 pide (1,0,0) ✗ ⇒ **P0 y P1 están en bloqueo** (esperan R1 y R0 respectivamente: ciclo $P_0\to R_1\to P_1\to R_0\to P_0$).
* b) Con `Solicitud[P1]=(0,0,1)`: P2 termina → `Trabajo=(0,0,1)`; P1 (0,0,1) ✔ → `(0,1,1)`; P0 (0,1,0) ✔ → `(1,1,1)`. **No hay bloqueo**, secuencia ⟨P2,P1,P0⟩.

#### H‑D3 · Evitar con el grafo (eventos con aristas de reclamo)

4 procesos y 4 recursos de una instancia. Aristas punteadas (lo que cada proceso *podrá* pedir): P0: {R0, R1} · P1: {R1, R2} · P2: {R2, R0} · P3: {R3, R1}. No hay asignaciones iniciales. Eventos: $t_0$: P0→R0 · $t_1$: P1→R1 · $t_2$: P2→R2 · $t_3$: P3→R3 · $t_4$: P0→R1 · $t_5$: P1→R2. Muestre el estado en $t_5$.

**Solución (revisando el ciclo en cada evento).**

| Evento | Razonamiento | Resultado |
|--------|-------------|-----------|
| $t_0$: P0→R0 | R0 libre; sin ciclo | **R0→P0** |
| $t_1$: P1→R1 | R1 libre; P1 aún podrá pedir R2, pero R2 no tiene dueño; sin ciclo | **R1→P1** |
| $t_2$: P2→R2 | Si se asigna: $R_0\to P_0 \dashrightarrow R_1\to P_1\dashrightarrow R_2\to P_2\dashrightarrow R_0$ = **ciclo** | **Inseguro: P2 se bloquea** (aunque R2 está libre) |
| $t_3$: P3→R3 | Libre; P3 podrá pedir R1 (de P1) pero P1 no espera nada de P3; sin ciclo | **R3→P3** |
| $t_4$: P0→R1 | R1 ocupado por P1 | **P0 espera a P1** |
| $t_5$: P1→R2 | R2 libre; P1 ya tendría R1 y R2 y ya no espera nada; sin ciclo | **R2→P1** |

**Estado en $t_5$:** asignados R0→P0, R1→P1, R2→P1, R3→P3; sin asignar: ninguno; **bloqueados: P0** (espera R1) **y P2** (se le negó R2 por seguridad). Cuando P1 termine y libere R1 y R2, P0 y P2 podrán avanzar.

#### H‑D4 · Prevención: ¿qué condición niega cada medida?

| Medida | Condición negada |
|--------|-----------------|
| Cada proceso pide todo lo que necesita antes de empezar | Retener y esperar |
| Numerar los recursos y exigir pedirlos en orden ascendente | Espera circular |
| Si el proceso pide algo ocupado, el sistema le quita lo que ya tiene | No expropiación |
| Convertir un archivo en "solo lectura compartido" | Exclusión mutua |
| El banquero | **No es prevención**: es *evitar* (usa información de máximos y comprueba si el estado es seguro) |

#### H‑D5 · Recuperación

Tres procesos bloqueados: P1 (prioridad alta, 90 % del trabajo hecho), P2 (prioridad baja, 5 %), P3 (prioridad media, 40 %). Se decide terminar **uno a uno**. ¿Por cuál empezar y qué factores justifica? → Por **P2**: menor prioridad, menos trabajo perdido, y tras cada terminación se vuelve a ejecutar la detección (puede que un solo aborto rompa el ciclo). Factores a citar: prioridad, tiempo ya trabajado y restante, cantidad y tipo de recursos que posee (¿expropiables?), recursos adicionales que le faltan, cuántos procesos habría que abortar, interactivo o por lotes. Si se prefiere **expropiar**, hay que elegir víctima, definir el retroceso y evitar que siempre pague el mismo (inanición).

#### H‑D6 · Encuentre el bloqueo con semáforos

```
sem S = 1, Q = 1
P0: wait(S); wait(Q); … ; signal(Q); signal(S);
P1: wait(Q); wait(S); … ; signal(S); signal(Q);
```

Traza: P0 `wait(S)` (S=0) → P1 `wait(Q)` (Q=0) → P0 `wait(Q)` bloquea (Q=−1) → P1 `wait(S)` bloquea (S=−1). **Bloqueo**: cumple exclusión mutua, retener y esperar, no expropiación y espera circular. **Arreglo:** que ambos pidan `S` antes que `Q`.

#### H‑D7 · Estado seguro rápido (una sola clase de recurso)

10 impresoras. P0: máx 8, tiene 3 · P1: máx 5, tiene 2 · P2: máx 7, tiene 3. ¿Seguro? Necesidades 5, 3, 4; disponibles 10−8=2; nadie ≤ 2 ⇒ **inseguro**. Si hubiera 11 impresoras (disponibles 3): P1 termina → 5 → P0 termina → 8 → P2 termina ⇒ **seguro ⟨P1,P0,P2⟩.**
---

## 5. Tema 3 · Memoria continua

### 5.1 Teoría mínima

* **Imagen del proceso** = lo que realmente se coloca en memoria (mucho más que el ejecutable `.exe`). En asignación continua la imagen debe quedar **completa y contigua**.
* El compilador genera código **relocalizable**: asume que el proceso es el único y empieza en la dirección 0. La **MMU** (Memory Management Unit, extensión de la CPU) traduce con **dos registros**:
  * **Registro base**: dirección física donde empieza el proceso.
  * **Registro límite**: tamaño del proceso.
  * $\text{física}=\text{base}+\text{lógica}$ **si** $\text{lógica}<\text{límite}$; si no, **excepción** (protección de memoria).
* En cada conmutación de proceso el kernel **guarda y restaura** estos registros en el BCP (parte "información del procesador/MMU"; es la única parte del BCP que depende de la arquitectura).
* **Particiones dinámicas:** la memoria libre se lleva como una **lista de huecos** `(base, límite)`.
* **Fragmentación externa:** hay espacio libre *total* suficiente, pero repartido en huecos que no alcanzan. **Interna:** sobra espacio *dentro* de lo asignado. La **compactación** mueve procesos para juntar huecos (es posible porque la MMU permite reubicar cambiando la base).
* **Algoritmos de ubicación** (para cada solicitud de tamaño $s$):

| Algoritmo | Qué hueco elige | Nota |
|-----------|----------------|------|
| **Primer ajuste** | El **primer** hueco, recorriendo desde el inicio de la lista, con tamaño ≥ $s$ | Si el enunciado no dice dónde empieza, **desde la primera posición**. |
| Siguiente ajuste ("la mejora") | Como el anterior, pero **empieza donde se hizo la última asignación** | Solo si el enunciado lo dice. |
| **Mejor ajuste** | El hueco **más pequeño** con tamaño ≥ $s$ | Deja huecos diminutos. Empate → el primero de la lista. |
| **Peor ajuste** | El hueco **más grande** | Destroza los huecos grandes. Empate → el primero de la lista. |

* **Regla de actualización** (así lo hace la solución oficial): se asigna al **inicio del hueco**. Nuevo hueco: $\text{base}'=\text{base}+s$, $\text{límite}'=\text{límite}-s$. Si el límite llega a 0 el hueco **desaparece**. La lista queda **en el mismo orden de memoria** del enunciado (no se reordena por tamaño).
* Al **terminar** un proceso su memoria vuelve a la lista de huecos y se **fusiona** con los huecos adyacentes (cuando $\text{base}_1+\text{límite}_1=\text{base}_2$).
* Si no cabe, el proceso queda **esperando** (estado *nuevo*) y se atiende cuando se libere memoria.

### 5.2 Método paso a paso (el ejercicio "hexadecimal" de 2019, 2020 y 2025)

1. Numera los huecos $0,1,2,\dots$ **en el orden del enunciado**.
2. Convierte los tamaños a decimal *solo para comparar* (o compara dígito a dígito en hex).
3. Para cada requisito y para cada algoritmo: elige el hueco, escribe **"hueco elegido, base asignada al proceso = base del hueco"** y el **hueco restante** (`base + s`, `límite − s`).
4. Aplica el requisito siguiente sobre la **tabla ya actualizada**.
5. Entrega: (a) **qué huecos son tomados** por cada solicitud y (b) la **tabla final de segmentos libres** por algoritmo.

> Usa la calculadora en modo programador y verifica cada suma hex. Un error de un dígito en una base arrastra todo lo que sigue.

### 5.3 Ejercicio `[REAL]` resuelto: 30‑oct‑2025 (también 7‑may‑2020, versión A)

Huecos en el orden de la memoria:

| # | Base | Límite |
|--:|------|--------|
| 0 | 0x06D01000 | 0x00500000 |
| 1 | 0x06100C00 | 0x00C00000 |
| 2 | 0x05200400 | 0x00F00000 |
| 3 | 0x04800000 | 0x00A00000 |
| 4 | 0x01E00000 | 0x00400000 |
| 5 | 0x02500000 | 0x01400000 |
| 6 | 0x07201800 | 0x01200000 |
| 7 | 0x08402C00 | 0x00700000 |

Requisitos: **0x00C00000, 0x00A00000, 0x00B00000**.

**a) Primer ajuste**

* 0x00C00000 → hueco **1** (justo, 0xC00000): base del proceso 0x06100C00; el hueco desaparece.
* 0x00A00000 → hueco **2** (el 0 es muy chico): base 0x05200400; resto `0x05200400+0xA00000 = 0x05C00400`, límite `0xF00000−0xA00000 = 0x500000`.
* 0x00B00000 → recorre desde el principio: 0 (0x5), 2' (0x5), 3 (0xA), 4 (0x4) no caben; **hueco 5** (0x1400000): base 0x02500000; resto `0x03000000 / 0x00900000`.

Tabla final: `0x06D01000/0x500000 · 0x05C00400/0x500000 · 0x04800000/0xA00000 · 0x01E00000/0x400000 · 0x03000000/0x900000 · 0x07201800/0x1200000 · 0x08402C00/0x700000`.

**b) Mejor ajuste**

* 0xC00000 → hueco 1 (justo). Base 0x06100C00; desaparece.
* 0xA00000 → el más pequeño ≥ 0xA00000 es el **3** (justo, 0xA00000): base 0x04800000; desaparece.
* 0xB00000 → candidatos: 2 (0xF00000), 5 (0x1400000), 6 (0x1200000) → el menor es el **2**: base 0x05200400; resto `0x05D00400 / 0x400000`.

Tabla final: `0x06D01000/0x500000 · 0x05D00400/0x400000 · 0x01E00000/0x400000 · 0x02500000/0x1400000 · 0x07201800/0x1200000 · 0x08402C00/0x700000`.

**c) Peor ajuste**

* 0xC00000 → el mayor es el **5** (0x1400000): base 0x02500000; resto `0x03100000 / 0x800000`.
* 0xA00000 → el mayor ahora es el **6** (0x1200000): base 0x07201800; resto `0x07C01800 / 0x800000`.
* 0xB00000 → el mayor ahora es el **2** (0xF00000): base 0x05200400; resto `0x05D00400 / 0x400000`.

Tabla final: `0x06D01000/0x500000 · 0x06100C00/0xC00000 · 0x05D00400/0x400000 · 0x04800000/0xA00000 · 0x01E00000/0x400000 · 0x03100000/0x800000 · 0x07C01800/0x800000 · 0x08402C00/0x700000`.

*(Resultados reproducidos con un programa y coinciden con la solución oficial.)*

### 5.4 Otras variantes `[REAL]`

**(a) Eventos con mejor ajuste dinámico, fusión y cola de espera (2‑nov‑2016, 35 %).** Memoria de 0x10000: SO en 0x0000‑0x7FFF; procesos P0 (0x8000, 0xC00), P2 (0xA000, 0x800), P4 (0xC000, 0x800), P7 (0xCC00, 0x400), P9 (0xE800, 0x1400). Huecos: `0xD000/0x1800, 0xA800/0x1800, 0xC800/0x400, 0x8C00/0x1400, 0xFC00/0x400`. Eventos: $t_{i+1}$ llega P10 (3K) · $t_{i+2}$ llegan P11 y P12 (6K c/u) · $t_{i+3}$ termina P7, llega P13 (4K) · $t_{i+4}$ termina P2, llega P14 (4K). (1K = 0x400.)

| Evento | Qué pasa |
|-------|----------|
| $t_{i+1}$ | P10 (0xC00): el hueco más ajustado es `0x8C00/0x1400` → P10 en 0x8C00; resto `0x9800/0x800`. |
| $t_{i+2}$ | P11 (0x1800) → `0xD000/0x1800` (justo). P12 (0x1800) → `0xA800/0x1800` (justo). |
| $t_{i+3}$ | Termina P7 (0xCC00/0x400): se **fusiona** con `0xC800/0x400` → `0xC800/0x800`. P13 (0x1000) **no cabe** (huecos 0x800, 0x800, 0x400) → **espera**. |
| $t_{i+4}$ | Termina P2 (0xA000/0x800): se fusiona con `0x9800/0x800` → `0x9800/0x1000`. Se atiende a P13 (esperaba) → 0x9800, **justo**. P14 (0x1000) no cabe → espera. |

Libres finales: `0xC800/0x800` y `0xFC00/0x400`. En espera: P14.

**(b) Procesos con segmentos lógicos (2014 y 2016, "completar #rl y #rb").** El tamaño del proceso es la **suma de sus segmentos**; el límite $\#rl$ = ese tamaño y la base $\#rb$ = base del hueco elegido (mejor ajuste). Hay que ir actualizando la lista de huecos después de cada proceso. *Ojo:* en la solución publicada de 2016 aparece la base 0x674B para P0, pero el hueco era `0x67AB` (0x67AB + 0x67C = 0x6E27, que es el hueco restante que usa la propia solución).

**(c) Partición fija / particiones en KB (23‑oct‑2013, preguntas de 4 %).** Particiones libres: 100, 500, 200, 300 KB; procesos: 80, 120, 280, 250, 190 KB. Resultado (tamaño que le queda a cada partición, de la 0 a la 3):

| Algoritmo | Partición 0 | 1 | 2 | 3 |
|-----------|--:|--:|--:|--:|
| Primer ajuste | 20 | 100 | 10 | 50 |
| Mejor ajuste | 20 | 60 | 80 | 20 |
| Peor ajuste | 100 | 20 | 10 | 50 |

(Primer ajuste: P0→0, P1→1, P2→1, P3→3, P4→2. Mejor: P0→0, P1→2, P2→3, P3→1, P4→1. Peor: P0→1, P1→1, P2→1, P3→3, P4→2.)

**(d) Contabilidad de memoria "GO‑NEAS" (7‑may‑2020, versión B).** Módulos estáticos siempre cargados: Main 50 + MaMa 80 + Parser 10 = **140 MB**; matrices: 4 cargadas + `tmp` + `res` = 6 × 10 = **60 MB**. Base = **200 MB**. Modelos: LBN 220 → libres **20**; NC 240 → **40**; YOLO 230 → **30**. Módulos dinámicos: SumarM 20, RestarM 20, MultM 30, DivM 40. Pruebas: P1L1 `m1+m2+m3+m4` (Sumar) · P1L2 `m1−m2−m3−m4` (Restar) · P2L1 `m1*m1*m2*m3*m4` (Mult) · P2L2 `m1−m2*m3/m4` (primero Mult, luego Div, luego Restar: precedencia y, a igual precedencia, de izquierda a derecha).
*Supuesto A (los módulos se quedan cargados durante la línea):*

| Modelo | P1L1 | P1L2 | P2L1 | P2L2 |
|--------|------|------|------|------|
| LBN (20) | pasa, libre 0 | pasa, libre 0 | **falla** en MultM, faltan 10 | **falla** en MultM, faltan 10 |
| NC (40) | pasa, libre 20 | pasa, libre 20 | pasa, libre 10 | **falla** en DivM, faltan 30 |
| YOLO (30) | pasa, libre 10 | pasa, libre 10 | pasa, libre 0 | **falla** en DivM, faltan 40 |

*Supuesto B (cada módulo se descarga al terminar su operación):* solo cambia P2L2 → LBN falla en MultM (faltan 10); NC pasa (necesita 40 como máximo, libre 0); YOLO falla en DivM (faltan 10). **Declara tu supuesto en el examen.**

### 5.5 Ejercicios `[HIP]` con solución

#### H‑M1 · Tres algoritmos con tamaños en MB

Huecos en el orden de la memoria: **A=8, B=15, C=5, D=22, E=11, F=6, G=17, H=9** (MB). Requisitos: **10, 14, 7, 9** MB. ¿Qué huecos se toman y cómo queda la lista con primer, mejor y peor ajuste?

| Algoritmo | 10 MB | 14 MB | 7 MB | 9 MB | Lista final (MB) |
|-----------|-------|-------|------|------|------------------|
| **Primer** | B (15→5) | D (22→8) | A (8→1) | E (11→2) | A1, B5, C5, D8, E2, F6, G17, H9 |
| **Mejor** | E (11→1) | B (15→1) | A (8→1) | H (9→0, desaparece) | A1, B1, C5, D22, E1, F6, G17 |
| **Peor** | D (22→12) | G (17→3) | B (15→8) | D (12→3) | A8, B8, C5, D3, E11, F6, G3, H9 |

Observación: tras el mejor ajuste queda un hueco grande (D=22, G=17) para procesos futuros; el peor ajuste los destroza. El total libre es el mismo (porque se asignó lo mismo), pero la **distribución** cambia.

#### H‑M2 · Versión hexadecimal (estilo 2019‑2025)

| # | Base | Límite |
|--:|------|--------|
| 0 | 0x03000000 | 0x00800000 |
| 1 | 0x01A00400 | 0x00300000 |
| 2 | 0x07800000 | 0x01000000 |
| 3 | 0x05100800 | 0x00C00000 |
| 4 | 0x09000000 | 0x00500000 |
| 5 | 0x0B400C00 | 0x00E00000 |

Requisitos: **0x00A00000, 0x00400000, 0x00D00000, 0x00200000**.

**Primer ajuste.** 0xA00000 → #2 (base 0x07800000; resto `0x08200000/0x600000`) · 0x400000 → #0 (base 0x03000000; resto `0x03400000/0x400000`) · 0xD00000 → #5 (base 0x0B400C00; resto `0x0C100C00/0x100000`) · 0x200000 → #0 (base 0x03400000; resto `0x03600000/0x200000`).
Final: `0x03600000/0x200000 · 0x01A00400/0x300000 · 0x08200000/0x600000 · 0x05100800/0xC00000 · 0x09000000/0x500000 · 0x0C100C00/0x100000`.

**Mejor ajuste.** 0xA00000 → #3 (0xC00000 es el menor ≥; base 0x05100800; resto `0x05B00800/0x200000`) · 0x400000 → #4 (0x500000; base 0x09000000; resto `0x09400000/0x100000`) · 0xD00000 → #5 (0xE00000 < 0x1000000; base 0x0B400C00; resto `0x0C100C00/0x100000`) · 0x200000 → el hueco `0x05B00800` (justo; desaparece).
Final: `0x03000000/0x800000 · 0x01A00400/0x300000 · 0x07800000/0x1000000 · 0x09400000/0x100000 · 0x0C100C00/0x100000`.

**Peor ajuste.** 0xA00000 → #2 (base 0x07800000; resto `0x08200000/0x600000`) · 0x400000 → #5 (el mayor, 0xE00000; base 0x0B400C00; resto `0x0B800C00/0xA00000`) · 0xD00000 → el mayor ahora es #3 con 0xC00000 < 0xD00000 ⇒ **no cabe: queda esperando** (ojo: hay 44 MB libres pero fragmentados) · 0x200000 → #3 (base 0x05100800; resto `0x05300800/0xA00000`).
Final: `0x03000000/0x800000 · 0x01A00400/0x300000 · 0x08200000/0x600000 · 0x05300800/0xA00000 · 0x09000000/0x500000 · 0x0B800C00/0xA00000`.

*(Ver el caso del peor ajuste: es un ejemplo de fragmentación externa: lo que no cabió con peor ajuste sí cabía con mejor ajuste.)*

#### H‑M3 · Eventos con mejor ajuste, fusión y cola de espera

Memoria de usuario 0x4000‑0xFFFF. Procesos: P0 (0x4000, 0x1000), P1 (0x6000, 0x800), P2 (0x7800, 0x1800), P3 (0xC000, 0x2000). Huecos: `0x5000/0x1000`, `0x6800/0x1000`, `0x9000/0x3000`, `0xE000/0x2000`.
Eventos: $t+1$ llega P4 (0xC00) · $t+2$ llegan P5 (0x1800) y P6 (0x800) · $t+3$ termina P1 y llega P7 (0x1C00) · $t+4$ termina P3 y llega P8 (0x6000).

| Evento | Resultado |
|--------|-----------|
| $t+1$ | Dos huecos de 0x1000 empatan; mejor ajuste con empate → el primero (`0x5000`). P4 en 0x5000; resto `0x5C00/0x400`. |
| $t+2$ | P5 (0x1800) → el menor ≥ es `0xE000/0x2000`: P5 en 0xE000, resto `0xF800/0x800`. P6 (0x800) → ajuste exacto en `0xF800` (desaparece). |
| $t+3$ | Termina P1 (0x6000/0x800) y se fusiona con `0x5C00/0x400` y con `0x6800/0x1000` ⇒ `0x5C00/0x1C00`. P7 (0x1C00) cabe **justo** en 0x5C00. |
| $t+4$ | Termina P3 (0xC000/0x2000) y se fusiona con `0x9000/0x3000` ⇒ `0x9000/0x5000`. P8 (0x6000) **no cabe** (el hueco es 0x5000) ⇒ **espera**. |

Libres finales: `0x9000/0x5000`. En espera: P8.

#### H‑M4 · Registros base y límite

P_a tiene base 0x4000 y límite 0x1800. Traduzca las direcciones lógicas 0x0123, 0x17FF, 0x1800 y 0x2000.
→ 0x0123 → **0x4123** · 0x17FF → **0x57FF** · 0x1800 → **excepción** (lógica ≥ límite) · 0x2000 → **excepción**.
Al cambiar de proceso el kernel guarda (0x4000, 0x1800) en el BCP de P_a y carga en la MMU los valores del siguiente.

#### H‑M5 · Teoría rápida

* Huecos libres de 6, 5 y 4 MB (15 MB en total); llega un proceso de 8 MB. → **No cabe por fragmentación externa**; con **compactación** (mover procesos y actualizar sus registros base) cabría, pero es costosa.
* ¿Qué desarrollo de hardware resolvió la fragmentación externa? → **La MMU con tabla de páginas** (paginación).
* ¿Por qué el código debe ser relocalizable? → Porque el compilador asume que el proceso empieza en 0; la base de la MMU lo ubica donde haya hueco.

---

## 6. Tema 4 · Memoria paginada (y lo que la rodea)

### 6.1 Teoría mínima (Sesiones 1 y 2 del profe)

* **Idea.** La memoria física se divide en bloques de tamaño fijo llamados **marcos**; la imagen del proceso se divide en **páginas** del mismo tamaño. Ya **no hace falta que el proceso sea contiguo**.
* **Tamaño de página:** potencia de 2 (de 512 B a 16 MB según arquitectura; típicos 1 KB, 2‑8 KB, 4 KB).
* **Dirección lógica** de $M$ bits con páginas de $2^n$ bytes: los **$M-n$ bits altos** son el **número de página $p$** y los **$n$ bits bajos** el **desplazamiento $d$**.
* **Tabla de páginas:** el índice $p$ devuelve el **número de marco $f$**. Dirección física $=f\cdot 2^n+d$. En fórmula (pregunta de selección múltiple repetida en 2013, 2014 y 2016):

$$F=\text{MARCO}\!\left(\left\lfloor \tfrac{D}{P}\right\rfloor\right)\cdot P+(D \bmod P)$$

* **Tamaño de la tabla de páginas** = $2^{M-n}$ entradas. 32 bits y 4 KB → $2^{20}=1\,048\,576$; 64 bits y 4 KB → $2^{52}$ (imposible de guardar en la MMU, por eso la tabla va a memoria).
* **Tabla por proceso** guardada en el BCP; al despachar un proceso, el despachador carga su tabla en la MMU.
* Si la tabla es grande se guarda **en memoria principal** y la MMU solo tiene el **PTBR** (*page table base register*). Costo: **dos accesos a memoria** por referencia (uno a la tabla, otro al dato).
* **TLB** (buffer de traducción lateral / **registros asociativos**): memoria rápida que busca **en paralelo** por número de página y devuelve el marco; guarda pocas entradas (a lo sumo del orden de 32). *Acierto* ⇒ un solo acceso a memoria; *fallo de TLB* ⇒ se consulta la tabla (doble acceso) y se actualiza la TLB con un reemplazo (p. ej. el menos usado). Funciona por el **principio de localidad** (temporal y espacial).
* **Página inválida:** el número de página supera el límite (tamaño del programa) ⇒ trap.
* **Tabla de marcos del SO:** marcos libres/ocupados. Cuando llega un proceso de $k$ páginas, se le asignan los **primeros $k$ marcos libres**; si no alcanzan, queda en estado **nuevo**/espera.
* **Fragmentación:** la paginación **elimina la externa** y produce **interna** (la última página queda parcialmente vacía; en promedio, media página por proceso). *(En clase comentó que si faltan marcos libres un programa grande no puede ejecutarse; eso es falta de memoria, no fragmentación externa.)*
* **Paginación por demanda / memoria virtual.** No se cargan todas las páginas: se traen cuando se usan. Referencia a una página no presente ⇒ **fallo de página** ⇒ trap ⇒ el SO la trae de disco (mientras tanto el proceso está **bloqueado**) ⇒ al terminar, el proceso pasa a **Listo** (clave de varios parciales). Si no hay marcos libres se aplica un **algoritmo de reemplazo**. Demasiados fallos = **hiperpaginación (thrashing)**. *Memoria virtual* es la técnica genérica que permite asignación no contigua, resuelve la discontinuidad del espacio de direcciones y ofrece más memoria que la física.
* **Tiempo efectivo de acceso** (fórmula del profe): $t_p=t_m+t_d\,(1-p)$, con $t_m$ acceso a memoria, $t_d$ acceso a disco y $p$ la probabilidad de que el dato **esté en memoria**.

### 6.2 Cómo separar página y desplazamiento (los 3 métodos de la clase)

Dirección $D$ y página de $P=2^n$ bytes.

1. **Aritmética decimal:** convierte $D$ a base 10; $p=D\div P$ (división **entera**), $d=D\bmod P$.
2. **Desplazamiento y máscara:** $p = D \gg n$; $d = D \,\&\, \text{máscara}$, con $\text{máscara}=2^n-1$ ($n$ unos). Para construirla: `~(~0 << n)` (ojo: `>>` aritmético con negativos mete unos por la izquierda; por eso se prefiere `<<`).
3. **Leer los bits:** convierte a binario y corta: los $M-n$ de la izquierda son $p$, los $n$ de la derecha son $d$. Si $P$ es potencia de 16 (256 = 0x100, 4096 = 0x1000) basta cortar dígitos hexadecimales.

Ejemplo de la clase: $D=\texttt{0x6ABC405B}$, $P=512$ ($n=9$). $D=1\,790\,722\,139$ ⇒ $p=1\,790\,722\,139\div512=3\,497\,504$ (**0x355E20**), $d=1\,790\,722\,139\bmod512=\mathbf{91}$ (**0x5B**). En una arquitectura de 64 bits con $n=9$ los $64-9=55$ bits altos son la página.

### 6.3 Paginación con eventos (el ejercicio largo de 2016)

**Reglas (así lo resuelve el profe):**

1. La lista de marcos libres es una **cola**: se toman los marcos **en el orden dado** (de arriba hacia abajo).
2. Un proceso de $M$ KB necesita $\lceil M/\text{tamaño de marco}\rceil$ marcos. Si no hay suficientes, **no se le asigna nada** y queda esperando (*nuevo*).
3. Al terminar un proceso, sus marcos se **agregan al final** de la lista de libres.
4. Después de cada terminación se atiende primero a los procesos que **ya esperaban** (en orden de llegada) y luego a los que llegan en ese instante.
5. Para cada evento se muestra: tabla de páginas de los procesos activos, marcos libres y procesos en estado nuevo.

**Ejemplo `[REAL]` (2‑nov‑2016, marcos de 1K).** Tablas: P1 `32,33,34,35,36,37` · P3 `40,41,42,43,44,45,46` · P5 `51,38,39,52,55,54` · P8 `56,57,58,59,60`. Marcos libres: `63,47,48,62,49,50,61,53`.

| Evento | Resultado |
|--------|-----------|
| $t_{i+1}$ llega P9 (3K) | P9 = `63,47,48`. Libres: `62,49,50,61,53` |
| $t_{i+2}$ llegan P10 (2K) y P11 (4K) | P10 = `62,49`. P11 necesita 4 y solo quedan `50,61,53` ⇒ **P11 espera**. Libres: `50,61,53` |
| $t_{i+3}$ termina P8, llega P12 (4K) | Se liberan `56,57,58,59,60` ⇒ libres `50,61,53,56,57,58,59,60`. Primero P11 = `50,61,53,56`; luego P12 = `57,58,59,60`. Libres: ninguno |
| $t_{i+4}$ termina P1, llega P13 (10K) | Se liberan `32…37` (6 marcos). P13 necesita 10 ⇒ **espera**. Libres: `32,33,34,35,36,37` |

*(Reproducido por programa; coincide con la solución oficial.)*

### 6.4 Preguntas cortas `[REAL]` con clave

| Pregunta | Respuesta |
|----------|-----------|
| Fórmula física $F$ desde $D$ y tamaño $P$ | $F=\text{MARCO}(D/P)\cdot P + D\bmod P$ |
| Direcciones de 32 bits, páginas de 4 KB: ¿nº de páginas? | $2^{20}=1\,048\,576$ |
| Direcciones de 16 bits, páginas de 256 B, MMU: pág.0→marco 4, 1→3, 2→2, 3→0, 4→1. ¿Dirección virtual 0x0302? | 8 bits de desplazamiento ⇒ página 0x03, desplazamiento 0x02. Página 3 → marco 0 ⇒ **0x0002** |
| Espacio virtual de 20 bits y páginas de 1024 B: ¿entradas de la tabla? | $2^{20-10}=1024$ |
| Direcciones de 22 bits y páginas de 1024 B: ¿entradas máximas? | $2^{22-10}=2^{12}$ |
| Tiempo máximo de acceso promedio 10 000 ns, $t_m=1$ ns, $t_d=1$ ms (= 10⁶ ns): ¿probabilidad $p$ de que el dato esté en memoria? | $10\,000 = 1 + 10^6(1-p)$ ⇒ $p=0{,}990001$ (≈ **0,99**) |
| Una página es traída de disco por un fallo de página: ¿en qué estado queda el proceso? | **Listo** |
| ¿Qué desarrollo de hardware resolvió la fragmentación externa? | **MMU / tabla de páginas** |
| ¿Cómo sabe el SO qué proceso necesita una página en paginación por demanda? | Quien la solicita es **el proceso que tiene asignada la CPU** |
| Técnica que permite asignación no contigua y resuelve la discontinuidad del espacio de direcciones | **Memoria virtual** |
| Arreglo `X[64][64]` de enteros, marcos de 128 palabras, 4 marcos (1 fijo para el programa), almacenado por filas. ¿Qué recorrido genera menos fallos? | Recorrer **por filas** (`i` externo, `j` interno): 32 cambios de página (**29** si descuentas los 3 primeros marcos libres). Por columnas: 64×32 = 2048 cambios (**2045**). |

### 6.5 Código de la MMU (se pide completar constructor y `fromLogicToPhysic`)

Versión depurada de la solución de 2014/2016 (compilada y probada):

```java
class MMU {
    private final int[] pageTable;          // tabla de páginas del proceso (índice = página, valor = marco)
    private final int pageSize, memorySize, processSize;

    MMU(int pageSize, int memorySize, int[] pageTable, int processSize) throws MemoryException {
        if (pageSize <= 0 || (pageSize & (pageSize - 1)) != 0)      throw new MemoryException(); // potencia de 2
        if (processSize > pageTable.length * pageSize)              throw new MemoryException(); // la tabla debe cubrir el proceso
        if ((long) pageTable.length * pageSize > memorySize)        throw new MemoryException(); // no más que la memoria
        this.pageSize = pageSize; this.memorySize = memorySize; this.processSize = processSize;
        this.pageTable = pageTable.clone();                          // copia, no alias
    }
    int fromLogicToPhysic(int logical) throws MemoryException {
        if (logical < 0 || logical >= processSize) throw new MemoryException();   // página inválida / fuera del límite
        return pageTable[logical / pageSize] * pageSize + logical % pageSize;      // marco·P + desplazamiento
    }
}
```

Con desplazamientos: `(pageTable[logical >>> n] << n) | (logical & ((1 << n) - 1))`.

### 6.6 Temas vecinos (aparecen en parciales viejos; el profe dijo que solo vio continua y paginada)

**Reemplazo de páginas.** Dada una cadena de referencias y $k$ marcos, simula y cuenta fallos.

* **FIFO:** sale la página que lleva **más tiempo cargada** (no actualiza en un acierto).
* **LRU:** sale la **menos recientemente usada** (un acierto la rejuvenece).
* **Óptimo:** sale la que se usará **más tarde en el futuro** (es la cota inferior; no realizable).
* **Anomalía de Belady:** con FIFO, más marcos pueden dar **más** fallos.
* Conteo: el profe separa los fallos **sin reemplazo** (los primeros, mientras se llenan los marcos) de los **con reemplazo**; lee el enunciado para saber cuál pide. `[REAL]` 2014/2016, $R=3,4,3,4,2,2,2,3,4,5,6,7,6$: FIFO con 4 marcos ⇒ 6 fallos totales (**2** con reemplazo); LRU con 3 marcos ⇒ 6 fallos totales (**3** con reemplazo). `[REAL]` 2018, traza de 33 referencias con 4 marcos: FIFO 17, LRU 17, óptimo 12.

**Segmentación.** Un programa se divide en segmentos (texto, datos, pila, heap) con nombre y tamaño; una **violación de segmento** (*segmentation fault*) es acceder fuera de su límite. Con **segmentación + paginación** la dirección es $(s,p,d)$: `s = dir >> (bits_p + bits_d)`, `p = (dir >> bits_d) & mask(bits_p)`, `d = dir & mask(bits_d)`; luego `tablaSegmentos[s].tablaPaginas[p]` da el marco y `físico = (marco << bits_d) | d`. Ejemplo 2015: direcciones de 20 bits con hasta 16 segmentos ⇒ `nseg = (l >> 16) & 0xF`, `desp = l & 0xFFFF`.

### 6.7 Ejercicios `[HIP]` con solución

#### H‑P1 · Traducción de direcciones

Direcciones de 16 bits; páginas de **1 KB**. Tabla del proceso: pág.0→marco 7, 1→2, 2→5, 3→0, 4→9, 5→1 (tamaño del proceso: 6 páginas). Traduzca 0x0C35, 0x1400, 0x17FF, 0x0041 y 0x2000.

* $n=10$ ⇒ $d$ = 10 bits bajos, $p$ = 6 bits altos (la tabla tiene hasta $2^6=64$ entradas).
* 0x0C35: $p=3$, $d=0x035$ → marco 0 ⇒ **0x0035**
* 0x1400: $p=5$, $d=0$ → marco 1 ⇒ **0x0400**
* 0x17FF: $p=5$, $d=0x3FF$ → marco 1 ⇒ **0x07FF**
* 0x0041: $p=0$, $d=0x41$ → marco 7 ⇒ **0x1C41**
* 0x2000: $p=8$ ⇒ **página inválida** (el proceso solo tiene 6 páginas) ⇒ trap.

(Por el método decimal: 0x1400 = 5120; 5120 ÷ 1024 = 5; 5120 mod 1024 = 0.)

#### H‑P2 · Tamaños

a) 24 bits y páginas de 2 KB: entradas $=2^{24-11}=2^{13}=8192$. b) 32 bits y páginas de 1 MB ($n=20$): $2^{12}=4096$ entradas. c) Con 16 GB de memoria física y marcos de 4 KB: $2^{34}/2^{12}=2^{22}=4\,194\,304$ marcos. d) 64 bits y páginas de 512 B: 55 bits de página y 9 de desplazamiento. e) Si cada entrada de tabla ocupa 4 B: la tabla de 32 bits/4 KB pesa $2^{20}\times4=4$ MB **por proceso**.

#### H‑P3 · Marcos libres y eventos

Marcos de **2K**. Tablas: A `5,6,8,10` · B `12,13,15` · C `1,4,16,17,19`. Libres, en este orden: `20,7,14,3,9,11,2,30,18,25`. Eventos: $t_1$ llega D (9K) · $t_2$ llegan E (4K) y F (8K) · $t_3$ termina B y llega G (3K) · $t_4$ termina A y llega H (12K). (Marcos por proceso: D=5, E=2, F=4, G=2, H=6.)

| Evento | Tablas nuevas / cambios | Libres | Nuevo (esperando) |
|--------|------------------------|--------|-------------------|
| $t_1$ | D = `20,7,14,3,9` | `11,2,30,18,25` | — |
| $t_2$ | E = `11,2`; F necesita 4 y solo hay 3 | `30,18,25` | F |
| $t_3$ | Termina B (libera `12,13,15`) ⇒ libres `30,18,25,12,13,15`. Primero F = `30,18,25,12`; luego G = `13,15` | — | — |
| $t_4$ | Termina A (libera `5,6,8,10`); H necesita 6 y hay 4 | `5,6,8,10` | H |

Fragmentación interna: D usa 5 marcos (10K) para 9K ⇒ 1K perdido; G usa 4K para 3K ⇒ 1K perdido.

#### H‑P4 · Tiempo efectivo de acceso

a) $t_m=100$ ns, tabla en memoria, sin TLB ⇒ $2t_m=\mathbf{200}$ ns. b) Con TLB de 10 ns y 90 % de aciertos: $0{,}9(10+100)+0{,}1(10+200)=\mathbf{120}$ ns; con 98 %: **112** ns. c) Memoria virtual con $t_m=100$ ns y $t_d=8$ ms (8 000 000 ns); se quiere $t_p\le200$ ns: $200=100+8\,000\,000(1-p)$ ⇒ $1-p=1{,}25\times10^{-5}$ ⇒ $p\ge\mathbf{0{,}9999875}$.

#### H‑P5 · Reemplazo de páginas

Cadena $R=2,3,2,1,5,2,4,5,3,2,5,2$ con **3 marcos** (`*` = fallo; marcos de menos a más reciente):

* **FIFO (9 fallos):** 2* → [2]; 3* → [2,3]; 2 → [2,3]; 1* → [2,3,1]; 5* → [3,1,5]; 2* → [1,5,2]; 4* → [5,2,4]; 5 → [5,2,4]; 3* → [2,4,3]; 2 → [2,4,3]; 5* → [4,3,5]; 2* → [3,5,2].
* **LRU (7 fallos):** 2* [2]; 3* [2,3]; 2 [3,2]; 1* [3,2,1]; 5* [2,1,5]; 2 [1,5,2]; 4* [5,2,4]; 5 [2,4,5]; 3* [4,5,3]; 2* [5,3,2]; 5 [3,2,5]; 2 [3,5,2].
* **Óptimo (6 fallos):** 2* [2]; 3* [2,3]; 2; 1* [2,3,1]; 5* [2,3,5] (sale el 1); 2; 4* [3,5,4]; 5; 3; 2* [5,4,2]; 5; 2.

Anomalía de Belady con $R=1,2,3,4,1,2,5,1,2,3,4,5$: FIFO con 3 marcos ⇒ **9** fallos; con 4 marcos ⇒ **10** (más marcos, más fallos). LRU: 10 y 8; óptimo: 7 y 6.

#### H‑P6 · Complete la clase `MMU`

Ver §6.5. Prueba: `MMU(1024, 65536, {7,2,5,0,9,1}, 6144)` ⇒ `fromLogicToPhysic(0x0C35)=0x0035`, `0x1400→0x0400`, `0x17FF→0x07FF`, `0x0041→0x1C41`, y `0x1800` lanza `MemoryException`.

#### H‑P7 · Fragmentación interna

Un proceso de **10 500 bytes**: con páginas de 1 KB necesita 11 páginas (11 264 B) ⇒ **764 B** de fragmentación interna; con 2 KB, 6 páginas (12 288 B) ⇒ **1788 B**; con 4 KB, 3 páginas (12 288 B) ⇒ **1788 B**. Páginas más grandes: tabla más pequeña pero más desperdicio.

#### H‑P8 · Diez preguntas de selección múltiple (con respuesta)

1. 32 bits y 4 KB → **$2^{20}$ páginas.**
2. Después de resolver un fallo de página el proceso queda en → **Listo.**
3. Para páginas de 2048 B, ¿cuántos bits tiene el desplazamiento? → **11.**
4. ¿Qué registro de la MMU apunta a la tabla de páginas cuando está en memoria? → **PTBR.**
5. Con TLB, ¿cuántos accesos a memoria en un acierto y en un fallo de TLB? → **1** y **2**.
6. ¿La paginación produce fragmentación interna o externa? → **Interna** (elimina la externa).
7. ¿Qué pasa si el número de página supera el límite de la tabla? → **Página inválida: trap al kernel.**
8. ¿Dónde se guarda la tabla de páginas de un proceso? → **En su BCP**, y el despachador la carga en la MMU.
9. El número de marcos que necesita un proceso de 9K con marcos de 2K → **5**.
10. ¿Qué principio justifica la TLB y la paginación por demanda? → **Localidad (temporal y espacial).**

---

## 7. Simulacro completo (formato del Parcial 3, ~2 h)

> Hazlo cronometrado y sin mirar las soluciones. Las respuestas están debajo.

**Punto 1 · Concurrencia (30 %).** Un puente de un solo carril admite autos en ambos sentidos, pero **nunca en sentidos opuestos a la vez**, y como máximo **3 autos** simultáneos. Cada auto ejecuta `entrar(sentido)` y `salir(sentido)`. Resuelva con **semáforos** o con un **monitor** (diga cuál). Justifique que no hay condición de carrera.

**Punto 2 · Bloqueos (30 %).** Procesos P0–P3 y recursos A, B, C (existencias 8, 5, 7).
Asignación: P0 (1,0,2) · P1 (2,1,0) · P2 (1,2,3) · P3 (2,0,1). Máximo: P0 (4,2,3) · P1 (3,2,2) · P2 (5,3,4) · P3 (3,1,2).
a) Calcule *Disponible* y *Necesidad*. b) ¿Es seguro el estado? Dé una secuencia. c) P1 solicita (1,0,1): ¿se concede? d) Mencione la condición de Coffman que se niega al numerar globalmente los recursos.

**Punto 3 · Memoria continua (20 %).** Huecos en este orden: `0x02000000/0x00600000`, `0x03400000/0x00300000`, `0x05000C00/0x00A00000`, `0x08100000/0x00500000`. Solicitudes: 0x00400000, 0x00500000, 0x00200000. Resuelva con primer, mejor y peor ajuste (hueco elegido, base y tabla final).

**Punto 4 · Paginación (20 %).** Direcciones de 20 bits, páginas de 512 B. Tabla: pág.0→marco 6, 1→2, 2→9, 3→4. a) Bits de página y de desplazamiento. b) Traduzca 0x005FF, 0x00400, 0x00600 y 0x007FF. c) Un proceso de 1300 B: ¿cuántos marcos y cuánta fragmentación interna?

### Soluciones del simulacro

**Punto 1 (monitor, probado en estilo Java).**

```java
class Puente {
    private int dentro = 0, sentido = -1;            // -1 = vacío
    synchronized void entrar(int s) throws InterruptedException {
        while (dentro == 3 || (dentro > 0 && sentido != s)) wait();
        sentido = s; dentro++;
    }
    synchronized void salir() {
        dentro--;
        if (dentro == 0) sentido = -1;
        notifyAll();                                    // despierta a los de ambos sentidos
    }
}
```

Justificación: todo el estado (`dentro`, `sentido`) se modifica dentro de métodos `synchronized` (exclusión mutua) y la condición se reevalúa en un `while` tras cada despertar. Inanición: este diseño permite que un sentido acapare el puente; si el enunciado lo pide, añadir un turno/contador (mencionarlo gana puntos).

**Punto 2.** Disponible = existencias − suma de asignaciones = (8,5,7) − (6,3,6) = **(2,2,1)**.
Necesidad = Máximo − Asignación: P0 (3,2,1) · P1 (1,1,2) · P2 (4,1,1) · P3 (1,1,1).
b) Trabajo=(2,2,1): P3 (1,1,1)≤ ⇒ Trabajo=(4,2,2); P0 (3,2,1)≤ ⇒ (5,2,4); P1 (1,1,2)≤ ⇒ (7,3,4); P2 (4,1,1)≤ ⇒ (8,5,7). Secuencia **⟨P3, P0, P1, P2⟩**: estado **seguro**.
c) P1 pide (1,0,1): ≤ Necesidad (1,1,2) ✓ y ≤ Disponible (2,2,1) ✓. Simulando: Disponible=(1,2,0); P1 asignado (3,1,1), necesita (0,1,1). Ningún proceso tiene Necesidad ≤ (1,2,0) salvo… P3 (1,1,1) no (0<1 en C). P1 (0,1,1) no (C=0). P0 (3,2,1) no. P2 no ⇒ estado **inseguro** ⇒ **NO se concede**, P1 espera.
d) Se niega la **espera circular** (ordenación global de recursos).

**Punto 3.** Tamaños: 0x600000, 0x300000, 0xA00000, 0x500000.
*Primer ajuste:* 0x400000 → #0 (base 0x02000000; resto `0x02400000/0x200000`) · 0x500000 → #2 (el #0 tiene 0x200000, #1 0x300000; base 0x05000C00; resto `0x05500C00/0x500000`) · 0x200000 → #0 (base 0x02400000; el hueco desaparece).
Final: `0x03400000/0x300000 · 0x05500C00/0x500000 · 0x08100000/0x500000`.
*Mejor ajuste:* 0x400000 → el menor ≥ es #3 (0x500000; base 0x08100000; resto `0x08500000/0x100000`) · 0x500000 → #0 (0x600000 < 0xA00000; base 0x02000000; resto `0x02500000/0x100000`) · 0x200000 → #1 (0x300000; base 0x03400000; resto `0x03600000/0x100000`).
Final: `0x02500000/0x100000 · 0x03600000/0x100000 · 0x05000C00/0xA00000 · 0x08500000/0x100000`.
*Peor ajuste:* 0x400000 → #2 (0xA00000; base 0x05000C00; resto `0x05400C00/0x600000`) · 0x500000 → empatan #0 y #2' con 0x600000; se toma el **primero de la lista**, #0 (base 0x02000000; resto `0x02500000/0x100000`) · 0x200000 → #2' (0x600000, el mayor; base 0x05400C00; resto `0x05600C00/0x400000`).
Final: `0x02500000/0x100000 · 0x03400000/0x300000 · 0x05600C00/0x400000 · 0x08100000/0x500000`.

**Punto 4.** a) $n=\log_2 512=9$ bits de desplazamiento; $20-9=11$ bits de página (tabla de hasta 2048 entradas).
b) 0x005FF = 1535: $p=\lfloor1535/512\rfloor=2$, $d=511$ → marco 9 ⇒ $9\cdot512+511=5119=$ **0x013FF**. · 0x00400 = 1024: $p=2$, $d=0$ → **0x01200** (4608). · 0x00600 = 1536: $p=3$, $d=0$ → marco 4 ⇒ **0x00800** (2048). · 0x007FF = 2047: $p=3$, $d=511$ → **0x009FF** (2559).
c) $\lceil1300/512\rceil=3$ marcos (1536 B) ⇒ fragmentación interna **236 B**.

---

## 8. Errores típicos y checklist de última hora

### Errores que cuestan puntos

| Tema | Error común | Cómo evitarlo |
|------|-------------|----------------|
| Concurrencia | Usar `if` en lugar de `while` antes de `wait()` | Siempre `while(!condición) wait();` |
| Concurrencia | Inicializar mal los semáforos (mutex=0, vacíos=0) | mutex=1; "espacios"=n; "datos"=0; **señalización** (esperar un evento) = 0 |
| Concurrencia | Hacer `wait(mutex)` antes de `wait(vacíos)` ⇒ interbloqueo | Primero el semáforo de **condición**, luego el mutex |
| Concurrencia | Olvidar `notifyAll` (o usar `notify` con varias condiciones) | `notifyAll` si hay condiciones distintas |
| Concurrencia | Variables compartidas fuera de la sección crítica | Todo estado compartido, solo con exclusión mutua |
| Bloqueos | Confundir *Necesidad* con *Máximo* | Necesidad = Máximo − Asignación |
| Bloqueos | No volver a sumar lo liberado al *Trabajo* | Trabajo += Asignación del proceso que termina |
| Bloqueos | En detección, usar Necesidad en vez de **Solicitud** | Detección compara Solicitud ≤ Trabajo |
| Bloqueos | Dar una sola secuencia sin verificar | Escribe Trabajo en cada paso |
| Bloqueos | Arista de petición/asignación mal dirigida | Proceso→recurso = solicitud; recurso→proceso = asignación; discontinua = reclamo |
| Memoria continua | Reordenar la lista de huecos | Mantén el orden del enunciado |
| Memoria continua | Empezar el "primer ajuste" en el último asignado | Eso es *siguiente ajuste* |
| Memoria continua | Error de suma hexadecimal | Verificar con calculadora; revisa que base+límite no solape otro hueco |
| Memoria continua | No fusionar huecos adyacentes al terminar un proceso | Si base₁+límite₁ = base₂ ⇒ se unen |
| Memoria continua | Olvidar que el proceso que no cabe **espera** | Se atiende al liberar memoria, en orden de llegada |
| Paginación | Dividir por el tamaño equivocado | $p=D\div P$, $d=D\bmod P$ |
| Paginación | Tomar marcos libres en desorden | Se toman **en el orden de la lista**; los liberados van **al final** |
| Paginación | Asignar parcialmente un proceso | O se le dan **todos** sus marcos o ninguno |
| Paginación | Olvidar redondear hacia arriba | #marcos = ⌈tamaño/marco⌉ |
| Paginación | Decir que el fallo de página deja al proceso en "ejecución" | Queda **bloqueado**, y al terminar la E/S pasa a **Listo** |

### Checklist (léelo la noche anterior)

**Concurrencia**
- [ ] Los 6 requisitos de la sección crítica y qué falla en un intento dado.
- [ ] Semáforos: `wait`/`signal`, valor negativo = # bloqueados, cola de espera.
- [ ] Productor‑consumidor, lectores‑escritores, filósofos, fumadores, barrera, control modular (act/done = 0).
- [ ] Monitor: condición con `while`, `notifyAll`, un solo hilo dentro.
- [ ] Tabla de ejecución con valores de semáforos paso a paso (a, b, c).

**Bloqueos**
- [ ] Las 4 condiciones y cómo negar cada una (orden global ⇒ sin espera circular).
- [ ] Grafo de asignación: ciclo, estado seguro, aristas de reclamo, "¿se concede?".
- [ ] Banker: Disponible, Necesidad, secuencia segura, solicitud (3 verificaciones).
- [ ] Detección con Solicitud y qué procesos están bloqueados.
- [ ] Corrección con orden de recursos (renumera A…F y reordena las solicitudes).

**Memoria continua**
- [ ] Base+límite, protección, relocalización, qué guarda el BCP.
- [ ] 3 algoritmos con tabla final; cuándo desaparece un hueco; fusión.
- [ ] Cola de espera por falta de memoria.

**Paginación**
- [ ] $F=\text{MARCO}(D/P)\cdot P+D\bmod P$ y bits de $p$/$d$.
- [ ] Tamaño de la tabla de páginas, PTBR, TLB, doble acceso a memoria.
- [ ] Marcos libres como cola; terminar ⇒ liberar al final; esperar si no alcanzan.
- [ ] Fallo de página ⇒ bloqueado ⇒ Listo; $t_p=t_m+t_d(1-p)$.
- [ ] (Opcional) FIFO/LRU/óptimo, Belady, segmentación.

---

## 9. Fuentes, supuestos y límites

**Fuentes usadas (todas del Proyecto):** las transcripciones de las sesiones 1 y 2 (`.vtt`) y los `.docx` de las sesiones (donde el profesor enumeró los temas del Parcial 3 y comentó cómo califica), el Capítulo 3 (concurrencia y bloqueos) y el Capítulo 2 (memoria), los PDF de parciales anteriores (`ST0257-Parciales-Anteriores.pdf`, `Parcial01`), `Taller antes del parcial 3.vtt` y `Examen_1.md`.

**Etiquetas:**

* `[REAL]` = ejercicio tomado de un parcial anterior (2013‑2025), con su solución; cuando el PDF no traía clave, la resolví y lo indico.
* `[HIP]` = ejercicio hipotético en el estilo del profesor, **con solución verificada por código** (Python para banker, detección, huecos, paginación, reemplazo y tiempos; Java compilado y ejecutado para los monitores y la clase `MMU`).

**Supuestos que debes confirmar (o declarar en el examen):**

1. Colas de monitor: 1 cola de entrada + 1 por variable de condición (el PDF no trae clave oficial).
2. Java: una sola variable de condición implícita por objeto (`wait`/`notifyAll`).
3. Contabilidad "GO‑NEAS" 2020: dos lecturas posibles (los módulos permanecen cargados vs. se descargan); ambas están resueltas.
4. Política de marcos libres: cola FIFO; los liberados se añaden al final; los procesos que esperan se atienden primero.

**Errores en las soluciones oficiales (para que no te confundan):**

* Detección 2020/2025: la secuencia publicada ⟨P2,P0,P1⟩ tiene los valores de *Trabajo* mal rotulados; el orden correcto es ⟨P2,P1,P0⟩.
* "Menor x" 2015: la solución tiene un desliz aritmético; la respuesta correcta es x = 1 con el orden D, A, C, B.
* Parcial 2016: aparece la base 0x674B donde debía ser 0x67AB.
* Las tablas de selección múltiple de 2013/2014 salieron con OCR inconsistente; no copié sus números.

**Límites.** No tengo el examen real. El profesor dijo que las preguntas salen de **concurrencia, bloqueos, memoria continua y memoria paginada**; reemplazo de páginas, segmentación y memoria virtual aparecen en parciales viejos, pero la probabilidad es baja y por eso están como material de refuerzo. Si el profesor publica un taller o corrige su alcance, ese cambio prevalece sobre este documento.

*Fin del documento. Mucho éxito en el parcial.*
