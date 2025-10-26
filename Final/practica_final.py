from datetime import datetime, date
import re
import csv

# Bajo la relacion de este sistema, un cliente puede asistir a un evento
# realizando una venta que tiene un precio determinado. Un cliente puede a ir a mas de un evento.

class Cliente:

    clientes = {}

    def __init__(self, id, nombre, email, fecha_alta):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.fecha_alta = fecha_alta


    # Metodo que da de alta al cliente y lo agrega a la lista 
    # estatica de clientes
    @staticmethod
    def alta_cliente():
        while True:
            try:
                nombre = input("¿Cuál es el nombre del cliente? ")
                email = input("¿Cuál es el email del cliente? ")
                # Se utiliza la libreria re para la validacion del mail
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
                
                id = Gestor.nueva_id(Cliente.clientes)
                cliente = Cliente(id, nombre, email, fecha_alta)
                Cliente.clientes[cliente.id] = cliente

                # Este metodo guarda al cliente en el csv de clientes
                cliente.guardar_clienteCSV()
                print("Cliente guardado exitosamente")
                break
            
            except:
                print("Error en la entrada de datos")

    # Metodo que se utiliza en el alta de cliente para cuando se crea el cliente
    # agregarlo al csv de clientes incrementalmente  
    def guardar_clienteCSV(self):
        with open('Final/data/clientes.csv', 'a', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            escritor.writerow([self.id,self.nombre,self.email,self.fecha_alta])


    @staticmethod
    def listar_clientes():
        if (len(Cliente.clientes) == 0): 
            print("No hay clientes en el sistema. ")
        else:
            for id, cliente in Cliente.clientes.items():
                print(f"Id = {id}: {cliente}")
    
    # Metodo de clase estatico para cargar los clientes del csv a 
    # la lista de clientes
    @staticmethod
    def cargar_clientes_csv():
        try:
            with open('Final/data/clientes.csv', newline='', encoding='utf-8') as file:
                lector = csv.reader(file, delimiter=';', quotechar='"')
                # Se pone el next para que no lea la primera linea que es el encabezado
                next(lector)
                for fila in lector:
                    id, nombre, email, fecha = fila
                    id = int(id)
                    fecha_alta = datetime.strptime(fecha, "%Y-%m-%d").date()
                    cliente = Cliente(id, nombre, email, fecha_alta)
                    Cliente.clientes[id] = cliente

        except FileNotFoundError:
            print("No se encontro el archivo clientes.csv")

    def antiguedad_dias(self) -> int:
        return (date.today() - self.fecha_alta).days
    
    def __str__(self):
        return f"Cliente = Nombre: {self.nombre} - Email: {self.email} - Fecha de alta: {self.fecha_alta}"
    
    def __repr__(self):
        return f"Cliente = Nombre: {self.nombre} - Email: {self.email} - Fecha de alta: {self.fecha_alta}"



class Evento:

    eventos = {}
    ingreso_eventos = {}
    categorias = set()

    def __init__(self, id, nombre, categoria, fecha_evento):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        # Se guarda la categoria en un set
        Evento.categorias.add(categoria)
        self.fecha_evento = fecha_evento
        # El ingreso se calcula despues...
        # Se iterara sobre el precio de las ventas

    @staticmethod
    def listar_eventos():
        if (len(Evento.eventos) == 0): 
            print("No hay eventos en el sistema. ")
        else:
            for id, evento in Evento.eventos.items():
                print(f"Id = {id}: {evento}")

    # Lista los ingresos de manera formateada
    @staticmethod
    def listar_ingresos_eventos():
        if (Evento.ingreso_eventos):
            print("Los ingresos por evento son: ") 
            for id, ingresos in Evento.ingreso_eventos.items():
                print(f"Id del Evento = {id}: Ingresos: {ingresos}")
        else:
            print("No hay Ingresos en los eventos del sistema. ")



    def dias_hasta_evento(self) -> int:
        return (self.fecha_evento - date.today()).days


    @staticmethod
    def ingreso_por_evento():
        ingresos_eventos = {}
        for venta in Venta.ventas.values():
            if venta.id_evento not in ingresos_eventos.keys():
                ingresos_eventos[venta.id_evento] = venta.precio
            else:
                ingresos_eventos[venta.id_evento] += venta.precio
        Evento.ingreso_eventos = ingresos_eventos
        

    # Carga los eventos y los agrega a la lista de eventos de la clase
    @staticmethod
    def cargar_eventos_csv():
        try:
            with open('Final/data/eventos.csv', newline='', encoding='utf-8') as file:
                lector = csv.reader(file, delimiter=';', quotechar='"')
                next(lector)
                for fila in lector:
                    # Se espera formato: nombre;categoria;fecha_evento
                    id, nombre, categoria, fecha = fila
                    id = int(id)
                    fecha_evento = datetime.strptime(fecha, "%Y-%m-%d").date()
                    evento = Evento(id, nombre, categoria, fecha_evento)
                    Evento.eventos[id] = evento

        except FileNotFoundError:
            print("No se encuentra el archivo eventos.csv")
        except:
            print("Error en la lectura de eventos.csv")

    def __str__(self):
        return f"Evento = {self.nombre} - Categoría: {self.categoria} - Fecha: {self.fecha_evento}"

    def __repr__(self):
        return f"Evento = {self.nombre} - Categoría: {self.categoria} - Fecha: {self.fecha_evento}"

class Venta:

    ventas = {}

    def __init__(self, id, id_cliente, id_evento, fecha_venta, precio):
        self.id = id
        self.id_cliente = id_cliente
        self.id_evento = id_evento
        self.fecha_venta = fecha_venta
        self.precio = precio

    @staticmethod
    def listar_ventas():
        if (len(Venta.ventas) == 0): 
            print("No hay ventas en el sistema. ")
        else:
            for id, venta in Venta.ventas.items():
                print(f"Id = {id}: {venta}")


    # Carga las ventas y los agrega a la lista de ventas de la clase
    def cargar_ventas_csv():
        try:
            with open('Final/data/ventas.csv', newline='', encoding='utf-8') as file:
                lector = csv.reader(file, delimiter=';', quotechar='"')
                next(lector)
                for fila in lector:
                    # Formato esperado: id_cliente;id_evento;fecha_venta;precio
                    id, id_cliente, id_evento, fecha, precio = fila
                    id = int(id)
                    id_cliente= int(id_cliente)
                    id_evento = int(id_evento)
                    fecha_venta = datetime.strptime(fecha, "%Y-%m-%d").date()
                    precio = float(precio)
                    venta = Venta(id, id_cliente, id_evento, fecha_venta, precio)
                    Venta.ventas[id] = venta

        except FileNotFoundError:
            print("No se encuentra el archivo ventas.csv")
        except:
            print("Error en la lectura de ventas.csv")


    def __str__(self):
        return f"Venta = Cliente: {self.id_cliente} - Evento: {self.id_evento} - Fecha: {self.fecha_venta} - Precio: {self.precio}"

    def __repr__(self):
        return f"Venta = Cliente: {self.id_cliente} - Evento: {self.id_evento} - Fecha: {self.fecha_venta} - Precio: {self.precio}"

# Se utilizara el gestor para gestionar todas las operaciones de la aplicacion
# como en la practica3
class Gestor:
    def __init__(self):
        self.clientes = {}
        self.eventos = {}
        self.ventas = {}

    # Metodo que proporciona una nueva id para 
    # guardarla en el objeto
    @staticmethod
    def nueva_id(diccionario):
        if diccionario:
            id = max(diccionario.keys()) + 1
        else:
            id = 1
        return id


    def filtar_ventas_por_rango(self):
        while True:
            try:
                fecha1 = input("Indique la fecha inicial (YYYY-MM-DD): ")
                fecha_inicial = datetime.strptime(fecha1, "%Y-%m-%d").date()
                fecha2 = input("Indique la fecha final (YYYY-MM-DD): ")
                fecha_final = datetime.strptime(fecha2, "%Y-%m-%d").date()
                ventas_rango = [venta for venta in Venta.ventas.values() 
                                if venta.fecha_venta >= fecha_inicial and 
                                venta.fecha_venta <= fecha_final]  
                print(f"Hay {len(ventas_rango)} ventas en el rango seleccionado" )
                if (len(ventas_rango) > 0):
                    print(f"Las ventas que estan dentro del rango seleccionado son: {ventas_rango}")
                break
                
            except:
                print("Error en la lectura de las fechas")


    # Metodo que carga los datos de los 3 csv
    def cargar_datos(self):
        Cliente.cargar_clientes_csv()
        Evento.cargar_eventos_csv()
        Venta.cargar_ventas_csv()

    def calcular_ingresos_totales(self):
        ingresos_totales = 0.0
        for venta in Venta.ventas.values():
            ingresos_totales += venta.precio
        return ingresos_totales
    

    def ingreso_por_evento(self):
        ingresos_eventos = {}
        for venta in Venta.ventas.values():
            if venta.id_evento not in ingresos_eventos.keys():
                ingresos_eventos[venta.id_evento] = venta.precio
            else:
                ingresos_eventos[venta.id_evento] += venta.precio
        return ingresos_eventos
    

    # Retorna el evento mas proximo y los dias que faltan para que ocurra
    def evento_mas_proximo(self):
        dias_hasta_evento = {}

        for evento in Evento.eventos.values():
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
        # Set que devuelve los precios que estan en las ventas
        precios = {venta.precio for venta in Venta.ventas.values()}
        if precios:
            minimo = min(precios)
            maximo = max(precios)
            promedio = sum(precios) / len(precios)
            return(minimo,maximo,promedio)
        else:
            return (0,0,0)

    # Crea el informe_resumen.csv que da el evento por el ingreso por evento
    def exportar_informe(self):
        if not Evento.ingreso_eventos:
            Evento.ingreso_por_evento()
            
        with open('Final/data/informe_resumen.csv', 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            escritor.writerow(['id_evento', 'nombre', 'categoria', 'fecha_evento', 'ingreso_evento'])
            for evento in Evento.eventos.values():
                ingresos = Evento.ingreso_eventos[evento.id]
                escritor.writerow([evento.id, evento.nombre, evento.categoria, evento.fecha_evento, ingresos])
        
        print("Se ha generado el archivo informe_resumen.csv")
    

    def estadisticas(self):
        while True:
            print("========== Métricas ==========")
            print("1) Ingresos Totales")
            print("2) Ingreso por Evento")
            print("3) Mostrar categorias existentes")
            print("4) Dias hasta el evento mas proximo")
            print("5) Estadistica de precios")
            print("6) Volver al menu")
            opcion = input("Elige una opción (1-6): ").strip()
            
            if opcion == '1':
                print (f"Los ingresos totales de los eventos son {gestor.calcular_ingresos_totales()}")

            elif opcion == '2':
                Evento.ingreso_por_evento()
                Evento.listar_ingresos_eventos()

            elif opcion == '3':
                print(f"Las Categorias existentes son: {Evento.categorias}")
            
            elif opcion == '4':
                gestor.evento_mas_proximo()
            
            elif opcion == '5':
               min, max, promedio = gestor.estadistica_precios()
               print(f"El precio minimo es: {min}")
               print(f"El precio maximo es: {max}")
               print(f"La media de precios es: {promedio}")
            
            elif opcion == '6':
                break

            else:
                print("Opción no válida. Intenta de nuevo.\n")

    # Menu que lista la cantidad de clientes, eventos y ventas
    def menu_listar(self):
        while True:
            print("========== Listar ==========")
            print("1) Clientes")
            print("2) Eventos")
            print("3) Ventas")
            print("4) Volver al menu")
            opcion = input("Elige una opción (1-4): ").strip()
            
            if opcion == '1':
                Cliente.listar_clientes()

            elif opcion == '2':
                Evento.listar_eventos()

            elif opcion == '3':
                Venta.listar_ventas()
            
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
            Cliente.alta_cliente()
        
        elif opcion == '4':
            gestor.filtar_ventas_por_rango()

        elif opcion == '5':
            gestor.estadisticas()

        elif opcion == '6':
            gestor.exportar_informe()
            print("El archivo informa_resumen se ha creado exitosamente")

        elif opcion == '7':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")


if __name__ == '__main__':
    # Consejo de depuración: descomenta las dos líneas siguientes para pausar en este punto
    # import debugpy
    # debugpy.breakpoint()
    gestor = Gestor()
    menu()