from datetime import datetime, date
import re
import csv

# Bajo la relación de este sistema, un cliente puede asistir a un evento
# realizando una venta que tiene un precio determinado. Un cliente puede ir a más de un evento.

class Cliente:

    def __init__(self, id, nombre, email, fecha_alta):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.fecha_alta = fecha_alta

    def antiguedad_dias(self) -> int:
        return (date.today() - self.fecha_alta).days

    def __str__(self):
        return f"Cliente = Nombre: {self.nombre} - Email: {self.email} - Fecha de alta: {self.fecha_alta}"

    def __repr__(self):
        return f"Cliente = Nombre: {self.nombre} - Email: {self.email} - Fecha de alta: {self.fecha_alta}"



class Evento:

    def __init__(self, id, nombre, categoria, fecha_evento):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.fecha_evento = fecha_evento
        # El ingreso se calcula despues...
        # Se iterara sobre el precio de las ventas por la cantidad
        # de eventos relacionados que tengan

    def dias_hasta_evento(self) -> int:
        return (self.fecha_evento - date.today()).days

    def __str__(self):
        return f"Evento = {self.nombre} - Categoría: {self.categoria} - Fecha: {self.fecha_evento}"

    def __repr__(self):
        return f"Evento = {self.nombre} - Categoría: {self.categoria} - Fecha: {self.fecha_evento}"



class Venta:

    def __init__(self, id, id_cliente, id_evento, fecha_venta, precio):
        self.id = id
        self.id_cliente = id_cliente
        self.id_evento = id_evento
        self.fecha_venta = fecha_venta
        self.precio = precio

    def __str__(self):
        return f"Venta = Cliente: {self.id_cliente} - Evento: {self.id_evento} - Fecha: {self.fecha_venta} - Precio: {self.precio}"

    def __repr__(self):
        return f"Venta = Cliente: {self.id_cliente} - Evento: {self.id_evento} - Fecha: {self.fecha_venta} - Precio: {self.precio}"



# Se utilizará el gestor para gestionar todas las operaciones de la aplicación
# como en la práctica3.
# Controla la lista de clientes, ventas y eventos, a la vez que la vista del programa
class Gestor:
    def __init__(self):
        self.clientes = {}
        self.eventos = {}
        self.ventas = {}
        self.ingreso_eventos = {}
        self.categorias = set()


    # Método que proporciona una nueva id para
    # guardarla los diccionarios
    @staticmethod
    def nueva_id(diccionario):
        if diccionario:
            id = max(diccionario.keys()) + 1
        else:
            id = 1
        return id


    # Método que da de alta al cliente y lo agrega al dict de clientes del gestor
    def alta_cliente(self):
        while True:
            try:
                nombre = input("¿Cuál es el nombre del cliente? ")
                email = input("¿Cuál es el email del cliente? ")
                # Se utiliza la librería re para la validación del mail
                patron_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                if not re.fullmatch(patron_email, email):
                    print("Email inválido. Ejemplo válido: usuario@mail.com")
                    continue
                fecha = input("¿Cuál es su fecha de alta? (YYYY-MM-DD) ")
                try:
                    fecha_alta = datetime.strptime(fecha, "%Y-%m-%d").date()
                except:
                    print("Formato de fecha inválido. Usa el formato YYYY-MM-DD ")
                    continue

                id = Gestor.nueva_id(self.clientes)
                cliente = Cliente(id, nombre, email, fecha_alta)
                self.clientes[cliente.id] = cliente

                # Este método guarda al cliente en el csv de clientes de forma incremental
                self.guardar_clienteCSV(cliente)
                print("Cliente guardado exitosamente")
                break

            except:
                print("Error en la entrada de datos")


    # Método que se utiliza en el alta de cliente para cuando se crea el cliente
    # agregarlo al csv de clientes incrementalmente
    def guardar_clienteCSV(self, cliente):
        with open('Final/data/clientes.csv', 'a', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            escritor.writerow([cliente.id, cliente.nombre, cliente.email, cliente.fecha_alta])



    # Método para cargar los clientes del csv a
    # la lista de clientes del gestor
    def cargar_clientes_csv(self):
        try:
            with open('Final/data/clientes.csv', newline='', encoding='utf-8') as file:
                lector = csv.reader(file, delimiter=';', quotechar='"')
                next(lector)
                for fila in lector:
                    id, nombre, email, fecha = fila
                    id = int(id)
                    fecha_alta = datetime.strptime(fecha, "%Y-%m-%d").date()
                    cliente = Cliente(id, nombre, email, fecha_alta)
                    self.clientes[id] = cliente
        except FileNotFoundError:
            print("No se encontró el archivo clientes.csv")


    # Carga los eventos y los agrega a la lista de eventos del gestor
    def cargar_eventos_csv(self):
        try:
            with open('Final/data/eventos.csv', newline='', encoding='utf-8') as file:
                lector = csv.reader(file, delimiter=';', quotechar='"')
                next(lector)
                for fila in lector:
                    id, nombre, categoria, fecha = fila
                    id = int(id)
                    fecha_evento = datetime.strptime(fecha, "%Y-%m-%d").date()
                    evento = Evento(id, nombre, categoria, fecha_evento)
                    self.eventos[id] = evento
                    # Se añade la categoria al set de categorias del gestor
                    self.categorias.add(categoria)
        except FileNotFoundError:
            print("No se encuentra el archivo eventos.csv")
        except:
            print("Error en la lectura de eventos.csv")


    # Carga las ventas y las agrega a la lista de ventas del gestor
    def cargar_ventas_csv(self):
        try:
            with open('Final/data/ventas.csv', newline='', encoding='utf-8') as file:
                lector = csv.reader(file, delimiter=';', quotechar='"')
                next(lector)
                for fila in lector:
                    id, id_cliente, id_evento, fecha, precio = fila
                    id = int(id)
                    id_cliente = int(id_cliente)
                    id_evento = int(id_evento)
                    fecha_venta = datetime.strptime(fecha, "%Y-%m-%d").date()
                    precio = float(precio)
                    venta = Venta(id, id_cliente, id_evento, fecha_venta, precio)
                    self.ventas[id] = venta

        except FileNotFoundError:
            print("No se encuentra el archivo ventas.csv")
        except:
            print("Error en la lectura de ventas.csv")


    def listar_clientes(self):
        if (len(self.clientes) == 0):
            print("No hay clientes en el sistema.")
        else:
            for id, cliente in self.clientes.items():
                print(f"Id = {id}: {cliente}")

    def listar_eventos(self):
        if (len(self.eventos) == 0):
            print("No hay eventos en el sistema.")
        else:
            for id, evento in self.eventos.items():
                print(f"Id = {id}: {evento}")


    def listar_ventas(self):
        if (len(self.ventas) == 0):
            print("No hay ventas en el sistema.")
        else:
            for id, venta in self.ventas.items():
                print(f"Id = {id}: {venta}")


    # Método que carga los datos de los 3 csv
    def cargar_datos(self):
        self.cargar_clientes_csv()
        self.cargar_eventos_csv()
        self.cargar_ventas_csv()


    # Rellena el diccionario del gestor de ingreso por evento cuando se lo pide
    def ingreso_por_evento(self):
        ingresos_eventos = {}
        for venta in self.ventas.values():
            if venta.id_evento not in ingresos_eventos.keys():
                ingresos_eventos[venta.id_evento] = venta.precio
            else:
                ingresos_eventos[venta.id_evento] += venta.precio
        self.ingreso_eventos = ingresos_eventos


    def listar_ingresos_eventos(self):
        if (self.ingreso_eventos):
            print("Los ingresos por evento son:")
            for evento in self.eventos.values():
                ingresos = self.ingreso_eventos.get(evento.id, 0)
                print(f"Id del Evento = {evento.id} - Nombre: {evento.nombre} - Ingresos: {ingresos}")
        else:
            print("No hay ingresos en los eventos del sistema.")



    def filtar_ventas_por_rango(self):
        while True:
            try:
                fecha1 = input("Indique la fecha inicial (YYYY-MM-DD): ")
                fecha_inicial = datetime.strptime(fecha1, "%Y-%m-%d").date()
                fecha2 = input("Indique la fecha final (YYYY-MM-DD): ")
                fecha_final = datetime.strptime(fecha2, "%Y-%m-%d").date()
                ventas_rango = [venta for venta in self.ventas.values()
                                if fecha_inicial <= venta.fecha_venta <= fecha_final]
                print(f"Hay {len(ventas_rango)} ventas en el rango seleccionado")
                if (len(ventas_rango) > 0):
                    print(f"Las ventas que están dentro del rango seleccionado son: {ventas_rango}")
                break
            except:
                print("Error en la lectura de las fechas")


    def calcular_ingresos_totales(self):
        ingresos_totales = 0.0
        for venta in self.ventas.values():
            ingresos_totales += venta.precio
        return ingresos_totales


    # Retorna el evento más próximo y los días que faltan para que ocurra
    def evento_mas_proximo(self):
        dias_hasta_evento = {}

        for evento in self.eventos.values():
            dias = (evento.fecha_evento - date.today()).days
            if dias >= 0:
                dias_hasta_evento[dias] = evento

        if dias_hasta_evento:
            dias_minimos = min(dias_hasta_evento.keys())
            evento = dias_hasta_evento[dias_minimos]
            print(f"Faltan {dias_minimos} días para el evento más próximo: {evento}")
        else:
            print("No hay eventos próximos en el sistema")


    def estadistica_precios(self):
        # Set que devuelve los precios que estan los precios de las ventas
        precios = {venta.precio for venta in self.ventas.values()}
        if precios:
            minimo = min(precios)
            maximo = max(precios)
            promedio = sum(precios) / len(precios)
            return (minimo, maximo, promedio)
        else:
            return (0, 0, 0)



    # Crea el informe_resumen.csv que da el evento por el ingreso por evento
    def exportar_informe(self):
        if not self.ingreso_eventos:
            self.ingreso_por_evento()

        with open('Final/data/informe_resumen.csv', 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            escritor.writerow(['id_evento', 'nombre', 'categoria', 'fecha_evento', 'ingreso_evento'])

            for evento in self.eventos.values():
                ingresos = self.ingreso_eventos[evento.id]
                escritor.writerow([evento.id, evento.nombre, evento.categoria, evento.fecha_evento, ingresos])

        print("Se ha generado el archivo informe_resumen.csv")



    def estadisticas(self):

        while True:

            print("========== Métricas ==========")
            print("1) Ingresos Totales")
            print("2) Ingreso por Evento")
            print("3) Mostrar categorías existentes")
            print("4) Días hasta el evento más próximo")
            print("5) Estadística de precios")
            print("6) Volver al menú")
            opcion = input("Elige una opción (1-6): ").strip()

            if opcion == '1':
                print(f"Los ingresos totales de los eventos son {self.calcular_ingresos_totales()}")

            elif opcion == '2':
                self.ingreso_por_evento()
                self.listar_ingresos_eventos()

            elif opcion == '3':
                print(f"Las Categorías existentes son: {self.categorias}")

            elif opcion == '4':
                self.evento_mas_proximo()

            elif opcion == '5':
                min, max, promedio = self.estadistica_precios()
                print(f"El precio mínimo es: {min}")
                print(f"El precio máximo es: {max}")
                print(f"La media de precios es: {promedio}")

            elif opcion == '6':
                break

            else:
                print("Opción no válida. Intenta de nuevo.\n")


    # Menú que lista la cantidad de clientes, eventos y ventas
    def menu_listar(self):
        while True:
            print("========== Listar ==========")
            print("1) Clientes")
            print("2) Eventos")
            print("3) Ventas")
            print("4) Volver al menú")
            opcion = input("Elige una opción (1-4): ").strip()

            if opcion == '1':
                self.listar_clientes()

            elif opcion == '2':
                self.listar_eventos()

            elif opcion == '3':
                self.listar_ventas()

            elif opcion == '4':
                break

            else:
                print("Opción no válida. Intenta de nuevo.\n")



def menu():
    
    gestor = Gestor()

    while True:
        print("========== MENÚ ==========")
        print("1) Cargar CSV")
        print("2) Listar Tablas")
        print("3) Alta de Cliente")
        print("4) Filtrar ventas por rango de fechas")
        print("5) Métricas")
        print("6) Exportar Informe")
        print("7) Salir")
        opcion = input("Elige una opción (1-7): ").strip()

        if opcion == '1':
            gestor.cargar_datos()
            print("Los datos se han cargado correctamente")

        elif opcion == '2':
            gestor.menu_listar()

        elif opcion == '3':
            gestor.alta_cliente()

        elif opcion == '4':
            gestor.filtar_ventas_por_rango()

        elif opcion == '5':
            gestor.estadisticas()

        elif opcion == '6':
            gestor.exportar_informe()
            print("El archivo informe_resumen se ha creado exitosamente")

        elif opcion == '7':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")


if __name__ == '__main__':
    menu()
