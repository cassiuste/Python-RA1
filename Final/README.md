# Práctica Final – Sistema de Gestión de Eventos


## Descripción general

Este proyecto es una aplicación en **Python** que permite administrar **clientes, eventos y ventas** desde la consola. La idea es simular un sistema tipo CRM, donde se puedan cargar datos desde archivos CSV, registrar clientes y generar informes con estadísticas de ingresos.

Toda la información se maneja mediante archivos **.csv** ubicados en la carpeta `data/`, que el programa lee y actualiza automáticamente.


## Funcionalidades principales

* **Cargar datos:** lee la información de clientes, eventos y ventas desde los archivos CSV.
* **Listar registros:** muestra los datos guardados en cada tabla (clientes, eventos o ventas).
* **Alta de cliente:** permite agregar un nuevo cliente validando el email y la fecha de alta.
* **Filtrar ventas por fechas:** muestra las ventas que se realizaron entre dos fechas indicadas.
* **Métricas y estadísticas:**

  * Ingresos totales del sistema.
  * Ingreso total por evento.
  * Categorías de eventos existentes.
  * Evento más próximo y días restantes.
  * Precio mínimo, máximo y promedio de las ventas.
* **Exportar informe:** genera el archivo `informe_resumen.csv` con los ingresos por evento.
* **Salir:** finaliza el programa.

## Estructura del proyecto

```
Final/
│
├── practica_final.py         # Código principal del programa
├── README.md                 # Descripción general del proyecto
└── data/
    ├── clientes.csv          # Datos de clientes (id;nombre;email;fecha_alta)
    ├── eventos.csv           # Datos de eventos (id;nombre;categoria;fecha_evento)
    ├── ventas.csv            # Datos de ventas (id;id_cliente;id_evento;fecha_venta;precio)
    └── informe_resumen.csv   # Informe generado con el resumen de actividad
```

## Clases principales

| Clase       | Descripción                                                              |
| ----------- | ------------------------------------------------------------------------ |
| **Cliente** | Representa a un cliente con su nombre, email y fecha de alta.            |
| **Evento**  | Contiene los datos de cada evento y permite calcular los ingresos.       |
| **Venta**   | Relaciona un cliente con un evento e incluye el precio de la venta.      |
| **Gestor**  | Maneja las operaciones principales: carga de datos, métricas e informes. |

## Ejemplo de archivos CSV

**clientes.csv**

```
id;nombre;email;fecha_alta
1;Juan Perez;juanperez@gmail.com;2020-05-20
2;Ana Gomez;anagomez@gmail.com;2021-11-15
3;Pedro Lopez;pedrolopez@gmail.com;2022-07-01
```

**eventos.csv**

```
id;nombre;categoria;fecha_evento
1;Concierto Rock;Musica;2025-12-10
2;Obra de Teatro;Teatro;2022-11-05
3;Exposición de Arte;Arte;2024-10-20
4;Festival de Cine;Cine;2026-03-15
```

**ventas.csv**

```
id;id_cliente;id_evento;fecha_venta;precio
1;1;1;2024-12-15;1500
2;2;1;2024-12-20;1500
3;3;2;2022-10-25;1200
4;1;3;2024-09-15;1000
5;2;3;2024-09-30;1000
6;1;4;2025-11-10;2000
7;2;4;2025-11-12;2000
```

## Ejemplo de informe generado

**informe_resumen.csv**

```
id_evento;nombre;categoria;fecha_evento;ingreso_evento
1;Concierto Rock;Musica;2025-12-10;3000.0
2;Obra de Teatro;Teatro;2022-11-05;1200.0
3;Exposición de Arte;Arte;2024-10-20;2000.0
4;Festival de Cine;Cine;2026-03-15;4000.0
```
