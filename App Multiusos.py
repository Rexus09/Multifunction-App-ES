#MI PRIMER PROGRAMA DE PYTHON
#la idea es, un programa con interfaz escrita, sin nada gráfico,
# que permita acceder a un cronómetro
# que permita acceder al traductor
# que permita acceder a una calculadora
#Creador de notas
#===========================================================================================================================================
from datetime import datetime, date, time, timedelta
import time
import calendar
#DESARROLLO:
#=========================================================================================================================================================#
#Pregunta
def preguntar():
    print("=======================================\nINICIO\n=======================================")
    print("Bienvenido a la interfaz escrita, a que herramienta desea acceder: \n-Cronómetro---> A\n-Calculadora---> B\n-Crear una nota--> C\nMODO RELOJ --> D")
    pregunta_modo = input("Introduce un valor aquí:") #Input y DECLARACÍON de la HERRAMIENTA que va a USAR
    if pregunta_modo == "A" or pregunta_modo == "a":
        cronometro()
    elif pregunta_modo == "B" or pregunta_modo == "b":
        calculadora()
    elif pregunta_modo == "C" or pregunta_modo == "c":
        notas()
    elif pregunta_modo == "D" or pregunta_modo == "d":
        clock()
def clock():
    import datetime
    import time
    import os
    from datetime import date, time, timedelta
    import time
    import calendar
    while True:
        tiempo = datetime.datetime.now()
        print(tiempo.hour,":", tiempo.minute,":", tiempo.second)
        time.sleep(1)
        os.system('cls')

#Cronómetro-->
def cronometro():
    print("\n=======================================\nCRONÓMETRO\n=======================================")
    print("Hola, esta es la opción cronómetro: \n Selecciona una opción:\n\n-Temporizador rapido --> A \n-Alarma --> B \n-Temporizador Específico --> C")
    crono_option = input() #Input y sus opciones
    if crono_option == "A" or crono_option == "a":
        modo_elegido = "Temporizador Rapido"
        print("Bien, has escogido la opción de ->", "Temporizador Rapido")
        modo_temporizador_rapido()
    elif crono_option == "B" or crono_option == "b":
        modo_elegido = "Alarma"
        print("Bien, has escogido la opción de ->", "Alarma")
        modo_alarma()
    elif crono_option == "C" or crono_option == "c":
        modo_elegido = "Temporizador Específico"
        print("Bien, has escogido la opción de ->", "Temporizador Específico")
        modo_temporizador_especifico()
def modo_temporizador_rapido():

    print("Elige:\n 5 segundos ---> A\n10 segundos---> B\n15 segundos---> C\n20 segundos--->D\n25 segundos--->E\n30 segundos--->F \n 5 minutos---> G\n10 minutos---> H\n15 minutos---> I\n20 minutos---> J\n25 minutos---> K\n30 minutos---> L")
    variable_aux_1 = input("Introduce la letra:")
    if variable_aux_1 == "A" or variable_aux_1 == "a":
        ahora = datetime.now() #coge la hora
        print("Hora de inicio:", ahora.hour,":",ahora.minute,":",ahora.second)  # Muestra hora
        hora_de_fin = time.time() + 5 #calculala hora de fin
        hora_de_fin = time.ctime(hora_de_fin)
        print("Hora de fin",hora_de_fin[-13:-5]) #muestra la hora de fin
        ahora = time.time()
        print("Se inició el cronómeto, espera")
        while hora_de_fin > time.ctime(ahora):
            ahora = time.time()

        print("terminó,  ya son las ",hora_de_fin[-13:-5], "horas.")

    if variable_aux_1 == "B" or variable_aux_1 == "b":
        ahora = datetime.now() #coge la hora
        print("Hora de inicio:", ahora.hour,":",ahora.minute,":",ahora.second)  # Muestra hora
        hora_de_fin = time.time() + 10 #calculala hora de fin
        hora_de_fin = time.ctime(hora_de_fin)
        print("Hora de fin",hora_de_fin[-13:-5]) #muestra la hora de fin
        ahora = time.time()
        print("Se inició el cronómeto, espera")
        while hora_de_fin > time.ctime(ahora):
            ahora = time.time()
        print("terminó,  ya son las ",hora_de_fin[-13:-5], "horas.")

    if variable_aux_1 == "C" or variable_aux_1 == "c":
        ahora = datetime.now() #coge la hora
        print("Hora de inicio:", ahora.hour,":",ahora.minute,":",ahora.second)  # Muestra hora
        hora_de_fin = time.time() + 15 #calculala hora de fin
        hora_de_fin = time.ctime(hora_de_fin)
        print("Hora de fin",hora_de_fin[-13:-5]) #muestra la hora de fin
        ahora = time.time()
        print("Se inició el cronómeto, espera")
        while hora_de_fin > time.ctime(ahora):
            ahora = time.time()
        print("terminó,  ya son las ",hora_de_fin[-13:-5], "horas.")

    if variable_aux_1 == "D" or variable_aux_1 == "d":
        ahora = datetime.now() #coge la hora
        print("Hora de inicio:", ahora.hour,":",ahora.minute,":",ahora.second)  # Muestra hora
        hora_de_fin = time.time() + 20 #calculala hora de fin
        hora_de_fin = time.ctime(hora_de_fin)
        print("Hora de fin",hora_de_fin[-13:-5]) #muestra la hora de fin
        ahora = time.time()
        print("Se inició el cronómeto, espera")
        while hora_de_fin > time.ctime(ahora):
            ahora = time.time()
        print("terminó,  ya son las ",hora_de_fin[-13:-5], "horas.")

    if variable_aux_1 == "E" or variable_aux_1 == "e":
        ahora = datetime.now() #coge la hora
        print("Hora de inicio:", ahora.hour,":",ahora.minute,":",ahora.second)  # Muestra hora
        hora_de_fin = time.time() + 25 #calculala hora de fin
        hora_de_fin = time.ctime(hora_de_fin)
        print("Hora de fin",hora_de_fin[-13:-5]) #muestra la hora de fin
        ahora = time.time()
        print("Se inició el cronómeto, espera")
        while hora_de_fin > time.ctime(ahora):
            ahora = time.time()
        print("terminó,  ya son las ",hora_de_fin[-13:-5], "horas.")

    if variable_aux_1 == "F" or variable_aux_1 == "f":
        ahora = datetime.now() #coge la hora
        print("Hora de inicio:", ahora.hour,":",ahora.minute,":",ahora.second)  # Muestra hora
        hora_de_fin = time.time() + 30 #calculala hora de fin
        hora_de_fin = time.ctime(hora_de_fin)
        print("Hora de fin",hora_de_fin[-13:-5]) #muestra la hora de fin
        ahora = time.time()
        print("Se inició el cronómeto, espera")
        while hora_de_fin > time.ctime(ahora):
            ahora = time.time()
        print("terminó,  ya son las ",hora_de_fin[-13:-5], "horas.")
    ###########################################################
    if variable_aux_1 == "G" or variable_aux_1 == "g":
        ahora = datetime.now() #coge la hora
        print("Hora de inicio:", ahora.hour,":",ahora.minute,":",ahora.second)  # Muestra hora
        hora_de_fin = time.time() + 5*60 #calculala hora de fin
        hora_de_fin = time.ctime(hora_de_fin)
        print("Hora de fin",hora_de_fin[-13:-5]) #muestra la hora de fin
        ahora = time.time()
        print("Se inició el cronómeto, espera")
        while hora_de_fin > time.ctime(ahora):
            ahora = time.time()
        print("terminó,  ya son las ",hora_de_fin[-13:-5], "horas.")

    if variable_aux_1 == "H" or variable_aux_1 == "h":
        ahora = datetime.now() #coge la hora
        print("Hora de inicio:", ahora.hour,":",ahora.minute,":",ahora.second)  # Muestra hora
        hora_de_fin = time.time() + 10*60 #calculala hora de fin
        hora_de_fin = time.ctime(hora_de_fin)
        print("Hora de fin",hora_de_fin[-13:-5]) #muestra la hora de fin
        ahora = time.time()
        print("Se inició el cronómeto, espera")
        while hora_de_fin > time.ctime(ahora):
            ahora = time.time()
        print("terminó,  ya son las ",hora_de_fin[-13:-5], "horas.")

    if variable_aux_1 == "I" or variable_aux_1 == "i":
        ahora = datetime.now() #coge la hora
        print("Hora de inicio:", ahora.hour,":",ahora.minute,":",ahora.second)  # Muestra hora
        hora_de_fin = time.time() + 15*60 #calculala hora de fin
        hora_de_fin = time.ctime(hora_de_fin)
        print("Hora de fin",hora_de_fin[-13:-5]) #muestra la hora de fin
        ahora = time.time()
        print("Se inició el cronómeto, espera")
        while hora_de_fin > time.ctime(ahora):
            ahora = time.time()
        print("terminó,  ya son las ",hora_de_fin[-13:-5], "horas.")

    if variable_aux_1 == "J" or variable_aux_1 == "j":
        ahora = datetime.now() #coge la hora
        print("Hora de inicio:", ahora.hour,":",ahora.minute,":",ahora.second)  # Muestra hora
        hora_de_fin = time.time() + 20*60 #calculala hora de fin
        hora_de_fin = time.ctime(hora_de_fin)
        print("Hora de fin",hora_de_fin[-13:-5]) #muestra la hora de fin
        ahora = time.time()
        print("Se inició el cronómeto, espera")
        while hora_de_fin > time.ctime(ahora):
            ahora = time.time()
        print("terminó,  ya son las ",hora_de_fin[-13:-5], "horas.")

    if variable_aux_1 == "K" or variable_aux_1 == "k":
        ahora = datetime.now() #coge la hora
        print("Hora de inicio:", ahora.hour,":",ahora.minute,":",ahora.second)  # Muestra hora
        hora_de_fin = time.time() + 25*60 #calculala hora de fin
        hora_de_fin = time.ctime(hora_de_fin)
        print("Hora de fin",hora_de_fin[-13:-5]) #muestra la hora de fin
        ahora = time.time()
        print("Se inició el cronómeto, espera")
        while hora_de_fin > time.ctime(ahora):
            ahora = time.time()
        print("terminó,  ya son las ",hora_de_fin[-13:-5], "horas.")

    if variable_aux_1 == "L" or variable_aux_1 == "l":

        ahora = datetime.now() #coge la hora
        print("Hora de inicio:", ahora.hour,":",ahora.minute,":",ahora.second)  # Muestra hora
        hora_de_fin = time.time() + 30*60 #calculala hora de fin
        hora_de_fin = time.ctime(hora_de_fin)
        print("Hora de fin",hora_de_fin[-13:-5]) #muestra la hora de fin
        ahora = time.time()
        print("Se inició el cronómeto, espera")
        while hora_de_fin > time.ctime(ahora):
            ahora = time.time()
        print("terminó,  ya son las ",hora_de_fin[-13:-5], "horas.")
def modo_alarma():
    print("Elige a la hora a la que quieres que te avise: ")
    hora_alarma = input()
    print("Ahora introduce lo minutos")
    minutos_alarma = input()
    if hora_alarma == None:
        hora_alarma = 0
    if minutos_alarma == None or minutos_alarma.type != int:
        minutos_alarma = 0
    hora_a_la_que_suena = datetime.datetime.now() 
    hora_a_la_que_suena.hour = hora_alarma
    hora_a_la_que_suena.minute = minutos_alarma
    x = True
    while x == True:
        if hora_a_la_que_suena == hora_alarma:
            print("Ya Acabó")
            x = False
            break
def modo_temporizador_especifico():
    print("Quieres introducir el timepo en A) Minutos B) Segundos")
    election = input()
    mins = 0
    secs = 0
    a = 0
    if election == "a" or election == "A":
        print("Indica el número de minutos que quieres esperar")
        mins = int(input())
    if election == "b" or election == "B":
        print("Indica el número de segundos que quieres esperar")
        secs = int(input())
    if int(mins) == 0:
        mins = int(secs) / 60
    if int(secs) == 0:
        secs = int(mins) * 60
    while True:
        if int(secs)-a == -1:
            break
        print("quedan", int(secs)-a, "segundos")
        a +=1
        time.sleep(1.0)
    print("El temporizador ha terminado")
#Calculadora-->
def calculadora():
    print("Introduce el tipo de operación que quieres hacer")
    x = input ("A = Suma, B = Resta, C = Multiplicación, D= División")
    print("PRESIONA _S_ PARA SALIR")
    while True:
        if x == "A" or x == "a":
            print("Modo Suma")
            a = input()
            b = int(a)
            while True:
                if a == "S":
                    print("La suma da -->", b)
                    break
                else:
                    a = input()
                    if a != "S":
                        b = int(b) + int(a)
        
            
        if x == "B" or x == "b":
            print("Modo Resta")
            a = input()
            b = int(a)
            while True:
                if a == "S":
                    print("La resta da -->", b)
                    break
                else:
                    a = input()
                    if a != "S":
                        b = int(b) - int(a)
            
        if x == "C" or x == "c":
            print("Modo Multiplicación")
            a = input()
            b = int(a)
            while True:
                if a == "S":
                    print("La multiplicación da -->", b)
                    break
                else:
                    a = input()
                    if a != "S":
                        b = int(b) * int(a)
            
        if x == "D" or x == "d":
            print("Modo División")
            a = input()
            b = a
            while True:
                if a == "S":
                    print("La división da -->", b)
                    break
                else:
                    a = input()
                    if a != "S":
                        b = int(b) / int(a)
#Creador de notas 


#Reiniciar
#x=True
#while x==True:
#    tecla = sys.stdin.read(1)
#    if tecla =='x' or tecla =='X' :
#        preguntar()
#    else:
#        pass


#Ejecutar Al Final
print("Si quieres salir de cualquier modo a la pantalla principal, m¡introduce en cualquier campo la letra x")
preguntar()
