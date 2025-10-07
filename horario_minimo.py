# Las horas son en HH:MM, si son HH solo los convierte

horarios = {
    'María':  ('08', '16'),
    'Juan':   ('09', '17'),
    'Lucía':  ('07', '15'),
    'Diego':  ('10', '18'),
    # Ampliación (Actividad sugerida: añade más y verifica que todo sigue funcionando)
    'Ana':    ('08', '14'),
    'Raúl':   ('12', '20'),
}

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
                # hora_indicada = horario_indicado[0:2]
                # hora_indicada = int(hora_indicada)
                # if(len(horario_indicado) == 2):
                #     min_indicados = 0
                # else:
                #     min_indicados = horario_indicado[3:5]
                #     min_indicados = int(min_indicados)
            
                for (nombre, (entrada, salida)) in horarios.items():
                    
                    # # Separar los HH:MM de la lista de horarios 
                    entrada = formatear_entrada(entrada)
                    # hora = entrada[0:2]
                    # hora = int(hora)
                    # if(len(entrada) == 2):
                    #     minutos = 0
                    # else:
                    #     minutos = entrada[3:5]
                    #     minutos = int(minutos)
                    # # Comparar el horario con el indicado para ver si es menor 
                    if (entrada["hora"] < horario_indicado["hora"] or entrada["hora"] == horario_indicado["hora"] 
                        and entrada["minutos"] < horario_indicado["minutos"]):
                        contador = contador + 1

                print(f"{contador} personas han llegado antes del horario indicado. ")
        else:
            print("Horario Invalido, tienes que indicar un horario en formato (HH) o (HH:MM):")
    except:
        print("Error al poner el horario")


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
        print("3) Salir")
        opcion = input("Elige una opción (1-3): ").strip()
 
        if opcion == '1':
            mostrar_registros()
        elif opcion == '2':
            contar_entradas()
        elif opcion == '3':
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

