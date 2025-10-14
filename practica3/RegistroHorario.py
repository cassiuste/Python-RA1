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
    

registros = []
with open('horarios.csv', newline='', encoding='utf-8') as f:
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