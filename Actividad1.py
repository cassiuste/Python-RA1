trabajadores = input("¿Cuantos trabajadores tienes? ")
trabajadores = int(trabajadores)
hora_referencia = input("¿Cual es el horario de referencia? (0-23) ")
hora_referencia = int(hora_referencia)

trabajador_antes_refencia = 0
trabajador_mas_temprano = ""
hora_salida_minima = 23

while trabajadores > 0:
    nombre_empleado = input("¿Como es tu nombre? ")
    hora_entrada = input("¿Cual es tu hora de entrada? ")
    hora_salida = input("¿Cual es tu hora de salida? ")
    hora_entrada = int(hora_entrada)
    hora_salida = int(hora_salida)

    if (hora_entrada < hora_salida):
        print("Hora correcta")

        if (hora_entrada <= hora_referencia):
            trabajador_antes_refencia += 1

        if (hora_salida < hora_salida_minima):
            hora_salida_minima = hora_salida
            trabajador_mas_temprano = nombre_empleado    
        elif (hora_salida == hora_salida_minima):
            trabajador_mas_temprano += f" y {nombre_empleado}"
        
        trabajadores -= 1
    else:
        print("Hora incorrecta")
    
print(f"Hay {trabajador_antes_refencia} de empleados que entran antes de la hora de refencia")
print(f"El empleado que salio primero es {trabajador_mas_temprano}")