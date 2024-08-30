# Todo.txt Extended: Empower Your Task Management!

---

## Introduction

`todo.txt` es una herramienta poderosa y sencilla para gestionar tus tareas diarias, utilizando un formato de texto plano que te permite máxima flexibilidad. Este archivo te permite mantener todas tus tareas organizadas y accesibles desde cualquier dispositivo, sin necesidad de aplicaciones complicadas. Vamos a ver cómo puedes maximizar su utilidad con algunas reglas y marcas especiales.

---

## Incomplete Tasks

Las tareas incompletas son aquellas que aún no has finalizado. Aquí están las reglas para gestionarlas de manera eficiente:

1. **Un elemento por línea**: Cada tarea debe ocupar una sola línea en el archivo. Esto mantiene el archivo limpio y fácil de manejar.

   ```txt
   2024-08-28 Buy coffee
   ```

2. **Fecha de creación (obligatoria)**: Toda tarea debe comenzar con la fecha en que fue creada. Esto te ayuda a monitorear cuánto tiempo llevan en tu lista.

   Ej.: Sin prioridad, la tarea empieza con la fecha de creación
   
   ```txt
   2024-08-28 Buy coffee
   ```
   
   Ej.: Con prioridad, la tarea empieza con la prioridad, dejando un espacio la fecha de creación
   
   ```txt
   (A) 2024-08-28 Buy coffee
   ```
   

3. **Contextos y proyectos**:

   - *Contextos*: Las palabras que comienzan con `@` refieren a un contexto, como `@phone` `@computer`. Esto te ayuda a agrupar tareas que puedes realizar en un mismo entorno.
   
   - *Proyectos*: Las palabras que comienzan con `+un proyecto`, como `+cleanGarage`. Esto te permite agrupar tareas relacionadas bajo un objetivo común.

   ```txt
   2024-08-28 Call Alice @phone +projectAlpha
   ```

4. **Tags**: Las palabras que comienzan con `#` refieren a un tag, como `#work` `#home`. Esto te ayuda a agrupar tareas relacionadas bajo un objetivo común.

   ```txt
   2024-08-28 Call Alice @phone +projectAlpha #work
   ```

5. **Prioridad (opcional)**: Puedes asignar una prioridad a las tareas usando una letra entre paréntesis al inicio de la línea. Las prioridades van de A a Z, pero solo se recomienda usar A, B, C y D. Esta marca de prioridad siempre debe ser la primera en la línea.

   ```txt
   (A) 2024-08-28 Buy coffee
   ```

5. **Fecha de expiración (opcional)**: Puedes añadir una fecha en la que la tarea debería completarse usando `due:YYYY-MM-DD`. Esto es opcional pero útil para mantener visibles los plazos.

   ```txt
   (B) 2024-08-28 Buy coffee due:2024-09-01
   ````

6. **Estado de ejecución**: Para indicar que una tarea está en progreso, usa la marca `[=]`. Solo una tarea puede tener esta marca en un momento dado.

   ```txt
   (A) 2024-08-28 Buy coffee [=]
   ```

7. **Tareas pausadas**: Si necesitas pausar una tarea que estaba en progreso, marca esa tarea con `[?]`. Puedes tener múltiples tareas en estado de pausa, pero solo una puede estar en progreso (`[=]`)

   ```txt
   2024-08-28 Buy coffee [?]
   ```

8. **Control de tiempo (opcional)**: Si deseas hacer un seguimiento del tiempo que dedicas a una tarea, usa las marcas de tiempo.

   *Marca de inicio*: Inicia el seguimiento con `start:HHmm`

      ```txt
      2024-08-28 Buy coffee [=] start:1000
      ```

   *Marca de fin y tiempo gastado*: Al completar la tarea, registra la hora de finalización con `end:HHmm`el tiempo total invertido con `spent:HHmm`

      ```txt
      2024-08-28 Buy coffee start:1000 end:1030 spent:0030
      ```

9. **Tareas recursivas**: Si deseas que una tarea se repita en intervalos regulares, puedes usar la marca `rec:interval`. La recursividad se define al final de la línea de la tarea.

   * Los intervalos son:
      - "nd": Repetir durante n días sucesivos.
      - "nm": Repetir durante n meses, en la misma fecha.
      - "ny": Repetir durante n años, en la misma fecha.
      - "nw": Repetir durante n semanas, en el mismo día.

   ```txt
   2024-08-28 Buy coffee rec:1d
   ```

## Completed Tasks

Las tareas completadas son aquellas que has finalizado. Aquí te explicamos cómo gestionarlas:

1. **Marcar como completa**: Cuando terminas una tarea, antepones una `x` minúscula al inicio de la línea, junto con la fecha en que se completó. La fecha de creación permanece para referencia.

   ```txt
   x 2024-08-28 2024-08-28 Buy coffee
   ```

2. **Mover al archivo `done.txt`**: Todas las tareas completadas deben moverse a un archivo separado llamado `done.txt`. Esto mantiene tu lista activa limpia y enfocada solo en las tareas pendientes.

3. **Tiempo invertido (si se rastreó)**: Si hiciste un seguimiento del tiempo en una tarea, incluye el tiempo total al final.

   ```txt
   x 2024-08-28 2024-08-28 Buy coffee start:1000 end:1030 spent:0030
   ```

## Ejemplos Comparativos

### Ejemplo 1: Tarea simple sin prioridad

   ```txt
   2024-08-28 Review project plan
   ```

### Ejemplo 2: Tarea con prioridad y fecha de expiración

   ```txt
   (B) 2024-08-28 Submit report +projectBeta due:2024-08-31
   ```


### Ejemplo 3: Tarea en progreso con control de tiempo

   ```txt
   (A) 2024-08-28 Write code +projectAlpha [=] start:0900
   ```


### Ejemplo 4: Tarea pausada

   ```txt
   (C) 2024-08-28 Research topic +projectGamma [?]
   ```

### Ejemplo 5: Tarea completada con tiempo registrado

   ```txt
   x 2024-08-28 2024-08-28 Fix bug +projectAlpha start:1400 end:1500 spent:0100
   ```
