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
 
def mostrar_registros():
    for index, (nombre, (entrada, salida)) in enumerate(horarios.items(), start=1):
        print(f"Indice: {index} - Nombre: {nombre} - Hora de entrada:  {entrada} - Hora de salida: {salida}")
            

def contar_entradas():
    contador = 0
    try:
        hora_entrada = input("Indica un horario en formato entero (0 - 23): ")
        hora_entrada = int(hora_entrada)
        # for tupla in horarios.values():
        #     entrada = tupla[0]
        #     entrada = int(entrada)
        #     if (hora_entrada > entrada):
        #         contador = contador + 1

        for index, (nombre, (entrada, salida)) in enumerate(horarios.items()):
            entrada = int(entrada)
            if (hora_entrada < entrada):
                contador = contador + 1

        print(f"{contador} personas han llegado antes del horario indicado. ")
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

