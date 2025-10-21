import csv

class RegistroHorario:
    def __init__(self, empleado: str, dia: str, entrada: int, salida: int):
        self.empleado = empleado
        self.dia = dia
        self.entrada = entrada
        self.salida = salida

    def duracion(self) -> int:
        """Devuelve la cantidad de horas trabajadas en este registro"""
        return self.salida - self.entrada
    


class Empleado:

    def __init__(self, nombre: str, registrosHorario: list[RegistroHorario]):
        self.nombre = nombre
        self.registrosHorario = registrosHorario
        

    def agregar_registro(self, registroHorario):
        self.registrosHorario.append(registroHorario) 
    
    def horas_totales(self):
        horas_totales = 0
        for registro in self.registrosHorario:
            horas_totales += registro.duracion()
        
        return horas_totales

    def dias_trabajados(self) -> int:
        for registro in self.registrosHorario:
        # Crea el set con todos los dias trabajados
            if registro.empleado not in trabajador_dias:
                trabajador_dias = set()
            else:
                trabajador_dias[registro.empleado].add(registro.dia)

        return len(trabajador_dias)

    def fila_csv(self):
        return f"{self.nombre};{self.horas_totales()};{self.dias_trabajados()}"


def leer_registros():
    registros = []
    with open('practica3/horarios.csv', newline='', encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=';', quotechar='"')
        for fila in lector:
            # Cada fila es una lista de cadenas: [nombre, dia, entrada, salida]
            nombre, dia, h_entrada, h_salida = fila
            # Convertimos las horas a enteros
            entrada = int(h_entrada)
            salida = int(h_salida)
            registro = RegistroHorario(nombre, dia, entrada, salida)
            registros.append(registro)

    print(f"Se han leído {len(registros)} registros")
    return registros


class GestorHorarios:
    
    def __init__(self, empleados: set[Empleado], registrosHorario: list[RegistroHorario]):
        self.empleados = empleados
        registrosHorario = registrosHorario

    def cargar_registros(self):
        self.registrosHorario = leer_registros()

    def crear_empleados(self):
        empleados_dict = {}

        for registro in self.registrosHorario:
            if registro.empleado not in empleados_dict:
                empleados_dict[registro.empleado] = Empleado(registro.empleado)
            
            empleados_dict[registro.empleado].agregar_registro(registro)

        # Convertir a conjunto de empleados
        self.empleados = set(empleados_dict.values())


    # Crear resumen_clases.csv
    def crear_resumen():
        with open('practica3/resumen_clases.csv', 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # Cabecera
            escritor.writerow(['Empleado','Dias trabajados', 'Horas totales'])
            # Filas con los datos acumulados
            for empleado, total in horas_totales.items():
                dias = ','.join(trabajador_dias[empleado])
                escritor.writerow([empleado, dias, total])


registros = leer_registros()



empleados_por_dia = {}
for registro in registros:
    # Creamos el conjunto para el día si no existe
    if registro.dia not in empleados_por_dia:
        empleados_por_dia[registro.dia] = set()
    # Añadimos el empleado al conjunto del día
    empleados_por_dia[registro.dia].add(registro.empleado)
    
# Mostrar empleados por día
for dia, empleados in empleados_por_dia.items():
    print(f"{dia}: {empleados}")
    

# Resumen Semanal

# Calcular horas totales por empleado
horas_totales = {}
for registro in registros:
    horas_totales.setdefault(registro.empleado, 0)
    horas_totales[registro.empleado] += registro.duracion()

trabajador_dias = {}
for registro in registros:
    # Crea el set con todos los dias trabajados
    if registro.empleado not in trabajador_dias:
        trabajador_dias[registro.empleado] = set()

    trabajador_dias[registro.empleado].add(registro.dia)

print(trabajador_dias)

# Escribir un resumen en un nuevo CSV
with open('practica3/resumen_semanal.csv', 'w', newline='', encoding='utf-8') as f:
    escritor = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # Cabecera
    escritor.writerow(['Empleado','Dias trabajados', 'Horas totales'])
    # Filas con los datos acumulados
    for empleado, total in horas_totales.items():
       dias = ','.join(trabajador_dias[empleado])
       escritor.writerow([empleado, dias, total])
print("Se ha generado el fichero resumen_horarios.csv")

def responder_preguntas():
    #  ¿Qué empleados trabajaron en todos los días?
    # empleados_todos_dias = {empleado for empleado, dias in trabajador_dias.items if len(dias) == 7}
    empleados_todos_dias = empleados_por_dia['Lunes'] & empleados_por_dia['Martes'] &empleados_por_dia['Miercoles'] & empleados_por_dia['Jueves'] & empleados_por_dia['Viernes'] & empleados_por_dia['Sabado']& empleados_por_dia['Domingo']
    print(f'Los empleados que trabajaron todos los dias son: {empleados_todos_dias}')
    # ¿Quiénes trabajaron sólo en un día concreto?
    empleados_un_dia = empleados_por_dia['Lunes'] ^ empleados_por_dia['Martes'] ^ empleados_por_dia['Miercoles'] ^ empleados_por_dia['Jueves'] ^ empleados_por_dia['Viernes'] ^ empleados_por_dia['Sabado'] ^ empleados_por_dia['Domingo']
    print(f'Los empleados que trabajaron un solo dia son: {empleados_un_dia}')

responder_preguntas()

hora_referencia = 10

def cantidad_madrugadores():
    madrugadores = {}
    for registro in registros:
        if registro.entrada < hora_referencia:
            madrugadores[registro.empleado] = registro.entrada
    
    with open('practica3/madrugadores.csv', 'w', newline='', encoding='utf-8') as csvfile:
        escritor = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        escritor.writerow(['Empleado', 'Hora de entrada'])
        for nombre, entrada in madrugadores.items():
            escritor.writerow([nombre, entrada])
    
    print("Se ha generado el fichero madrugadores.csv")

cantidad_madrugadores()


def mostrar_interseccion():
    empleados_lunes_viernes = empleados_por_dia['Lunes'] & empleados_por_dia['Viernes']
    print(f'Los empleados que trabajan los lunes y viernes son: {empleados_lunes_viernes}')

    with open('practica3/en_dos_dias.csv', 'w', newline='', encoding='utf-8') as csvfile:
        escritor = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        escritor.writerow(['Empleados'])
        for nombre in empleados_lunes_viernes:
            escritor.writerow([nombre])
    
    print("Se ha generado el fichero en_dos_dias.csv")

mostrar_interseccion()

def empleados_exclusivos():
    empleados_sabado = empleados_por_dia['Sabado'] - empleados_por_dia['Domingo']
    print(f'Los empleados que trabajan lo sabados y no los domingos son: {empleados_sabado}')

empleados_exclusivos()

def empleado_extenso():
    turno_extenso = {registro.empleado for registro in registros if registro.duracion() >= 6}
    print(f'Las personas que hacen un turno de 6 horas o mas son: {turno_extenso}')

empleado_extenso()