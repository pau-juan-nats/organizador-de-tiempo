#OPERACION DE POMODOROS

pomodorofacil = 2
pomodoromedio = 4
pomodorodificil = 8

pregunta = int(input("¿Cuántos temas tiene la asignatura que deseas estudiar?\n"))
c = 0
"""
Aqui pregunta la dificultad de los temas de la asignatura.
"""
for i in range(pregunta):
    tema = input("El tema número {0} es fácil, medio o difícil?\n".format(i+1))
    if tema != "":
        if tema == "fácil" or tema =="facil" or tema == "Facil" or tema == "Fácil":
            tiempo_pomodoro = (25*pomodorofacil)
            print("En el tema {0} debes estudiar".format(i+1), tiempo_pomodoro," minutos y recuerda que cada 25 minutos descansas 5 minutos.")
        elif tema == "medio" or tema == "Medio":
            tiempo_pomodoro = (25*pomodoromedio)
            print("En el tema {0} debes estudiar".format(i+1), tiempo_pomodoro," minutos y recuerda que cada 25 minutos descansas 15 minutos.")
        elif tema == "Difícil" or tema == "difícil" or tema == "dificil" or tema =="Dificil":
            tiempo_pomodoro = (25*pomodorodificil)
            print("En el tema {0} debes estudiar".format(i+1), tiempo_pomodoro," minutos y recuerda que cada 100 minutos descansas 25 minutos.")
        c += tiempo_pomodoro


print("La cantidad de minutos que vas a dedicar a estudiar para esta asignatura son ", c)

"""
-------------------------------------------------------------------------------------------------------------------------------------------------
"""

#CREAR UN HORARIO

horas = {}
for i in range(0, 10):
    horas["0{0}:00".format(i)] = [None for j in range(7)]
for k in range(11, 24):
    horas["{0}:00".format(k)] = [None for l in range(7)]
print(horas)
"""
 Aqui colocamos las horas de 0 a 9 en el diccionario horas.
 El diccionario tiene de llave la hora y el valor tiene una lista con LAS ACTIVIDADES. La posicion de cada elemnto de la lista es el dia de la semana.
 """
pregunta1 = input("Dia: ")
pregunta2 = input("Hora: ")
pregunta3 = input("Materia: ")

dias = {"Lunes":0, "Martes":1, "Miercoles":2, "Jueves":3, "Viernes":4, "Sabado":5, "Domingo":6}

horas[pregunta2][dias[pregunta1]] = pregunta3

print(horas)
"""
Aqui hace las preguntas respectivas para modificar el dia, la hora en la posicion que es
"""
