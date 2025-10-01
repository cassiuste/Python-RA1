contador_entradas = 0
trabajador_mas_temprano = ""
salida_mas_temprana = 23

while True:
    try:
        trabajadores = input("¿Cuantos trabajadores tienes? ")
        trabajadores = int(trabajadores)
        hora_referencia = input("¿Cual es el horario de referencia? (0-23) ")
        hora_referencia = int(hora_referencia)
        if(hora_referencia >= 0 and hora_referencia <=23):
            break
            
    except:
        print("Error en la entrada de datos")


while trabajadores > 0:
    try:
        nombre_empleado = input("¿Cual es el nombre del trabajador? ")
        hora_entrada = input("¿Cual es su hora de entrada? ")
        hora_salida = input("¿Cual es su hora de salida? ")
        hora_entrada = int(hora_entrada)
        hora_salida = int(hora_salida)
        
        if(hora_entrada>= 0 and hora_entrada<=23 and hora_salida>=0 and hora_salida<=23):
            if (hora_entrada < hora_salida):
                print("Hora correcta")

                if (hora_entrada <= hora_referencia):
                    contador_entradas += 1

                if (hora_salida < salida_mas_temprana):
                    salida_mas_temprana = hora_salida
                    trabajador_mas_temprano = nombre_empleado    
                elif (hora_salida == salida_mas_temprana):
                    trabajador_mas_temprano += f" y {nombre_empleado}"
                
                trabajadores -= 1
            else:
                print("Hora incorrecta")
        else:
            print("Hora incorrecta")
    except:
        print("Hora incorrecta")
        
print(f"Hay {contador_entradas} de empleados que entran antes o a la misma hora que la hora de refencia")
print(f"El empleado que salio primero es {trabajador_mas_temprano} a las {salida_mas_temprana}")