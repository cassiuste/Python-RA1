import json
# Las horas son en HH:MM, si son HH solo los convierte

# horarios = {
#     'María':  ('08', '16'),
#     'Juan':   ('09', '17'),
#     'Lucía':  ('07', '15'),
#     'Diego':  ('10', '18'),
#     # Ampliación (Actividad sugerida: añade más y verifica que todo sigue funcionando)
#     'Ana':    ('08', '14'),
#     'Raúl':   ('12', '20'),
# }


def leer_horarios():
    with open('practica2/horarios.json', encoding='utf-8') as f:
        data = json.load(f)
        horario_json = data.get('horarios', {})
        horarios = {}
        for nombre, horario in horario_json.items():
            horarios[nombre] = tuple(horario)
        return horarios

horarios = leer_horarios()

def escribir_horarios(nombre_empleado, hora_entrada, hora_salida):
    horarios[nombre_empleado] = (hora_entrada, hora_salida)
    with open('practica2/horarios.json', 'w', encoding='utf-8') as f:
        json.dump({'horarios':horarios}, f, indent=4)


# Valida que la entrada del horario sea correcta y devuelve
# las horas y los minutos si lo es
def formatear_entrada(hora_completa):
    try:
        hora = hora_completa[0:2]
        hora = int(hora)
        
        if(len(hora_completa) == 2):    
            minutos = 00
        elif(len(hora_completa) == 5):    
            minutos = hora_completa[3:5]
            minutos = int(minutos)
        else:
            return False
        
        if(hora>= 0 and hora <=24 and minutos>=0 and minutos<=59):
            return {"hora":hora, "minutos":minutos}
        else:
            return {}
    except:
        return False

def mostrar_registros():
    for index, (nombre, (entrada, salida)) in enumerate(horarios.items(), start=0):
        print(f"Indice: {index} - Nombre: {nombre} - Hora de entrada:  {entrada} - Hora de salida: {salida}")
            

def contar_entradas():
    contador = 0
    try:
        horario_indicado = input("Indica un horario en formato entero (HH) o (HH:MM): ")
        if (formatear_entrada(horario_indicado)):
            # Separar los HH:MM del horario indicado 
                horario_indicado = formatear_entrada(horario_indicado)
                for (nombre, (entrada, salida)) in horarios.items():
                    # Separar los HH:MM de la lista de horarios 
                    entrada = formatear_entrada(entrada)
                    # Comparar el horario con el indicado para ver si es menor 
                    if (entrada["hora"] < horario_indicado["hora"] or entrada["hora"] == horario_indicado["hora"] 
                        and entrada["minutos"] < horario_indicado["minutos"]):
                        contador = contador + 1

                print(f"{contador} personas han llegado antes del horario indicado. ")
        else:
            print("Horario Invalido, tienes que indicar un horario en formato (HH) o (HH:MM):")
    except:
        print("Error al poner el horario")



def crear_trabajador():
    nombre_empleado = input("¿Cual es el nombre del trabajador? ")
    hora_entrada = input("¿Cual es su hora de entrada? (HH) o (HH:MM): ")
    hora_salida = input("¿Cual es su hora de salida? (HH) o (HH:MM): ")
    if(formatear_entrada(hora_entrada) and formatear_entrada(hora_salida)):
        escribir_horarios(nombre_empleado, hora_entrada, hora_salida)
    else:
        print("Error en la creación del trabajador")
    

def menu():
    """
    Menú principal repetitivo (bucle while) para elegir acciones:
      1) Mostrar registros
      2) Contar entradas
      3) Salir
    """
    while True:
        print("========== MENÚ ==========")
        print("1) Mostrar registros")
        print("2) Contar entradas")
        print("3) Crear empleado")
        print("4) Salir")
        opcion = input("Elige una opción (1-4): ").strip()
         
        if opcion == '1':
            mostrar_registros()
        elif opcion == '2':
            contar_entradas()
        elif opcion == '3':
            crear_trabajador()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")
 
 
# ---------------------------------------------------------------------------
# 4) Punto de entrada
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    # Consejo de depuración: descomenta las dos líneas siguientes para pausar en este punto
    # import debugpy
    # debugpy.breakpoint()
    menu()

