from tkinter import *



width = 1024
height=1024
root = Frame(height=height, width = width,background="navajowhite")
root.pack(padx = 0,pady = 0)
contador = 0
count_global = 0



def Grafica():
    """
    Esta funcion pregunta al usuario la cantidad de temas que debe estudiar para poder hacer el calculo.
    Genera un boton que redirecciona a la funcion de Pomodoros.
    La funcion Grafica es la funcion principal que llama a todas las demas funciones.
    """
    pregunta = "¿Cuántos temas tiene la asignatura que deseas estudiar?"
    etiqueta = Label(text=pregunta, font= ("Verdana",15),background="white").place(x=0, y=10)
    campo = Entry(root)
    campo.insert(0, "")
    campo.place(x=0, y=45)
    boton = Button(root, text="Aceptar", command = lambda: Iteracion(campo.get()), font= ("Verdana",15),background="white").place(x=0,y=75)



def Iteracion(entry):
    """
    La funcion pomodoros tiene como parametro el campo en donde el usuario ingresa la cantidad de temas que debe estudiar.
    Esta funcion realiza una iteracion de la cantidad de temas para poder realizar las otras funciones.
    Ademas tiene una variable que mide los espacios equitativos para una mejor estetica
    """
    x = 0
    y = 0
    ent = int(entry)
    print(ent)
    m = (height/(ent + 1))
    for i in range(ent):
        y = Temas(i,m,y)



def Temas(i, m, y):
    """
    Esta funcion tiene como parametros "i" que es la varible de la iteracion, ya que esta funcion va necesariamente conectada para que se
    realice por cada tema la pregunta indicada; "m" para tener como global la distribucion del espacio; "y" la necesitamos para generalizar los espacios del campo.
    """
    x = 140
    y += m
    y2 = y + 55
    y3 = y + 30
    tema = "¿El tema número "+ str(i+1)+", es fácil, medio o difícil?"
    etiqueta2 = Label(text=tema,font= ("Verdana",15),background="white").place(x=x , y=y)
    campo2 = Entry(root)
    campo2.insert(0,"")
    campo2.place(x=x, y=y3)
    boton2 = Button(root, text="Aceptar", command = lambda:Pomodoros(campo2.get(), i, y)).place(x=x, y=y2)
    return y



def Pomodoros(parametro, i, y):
    """
    Esta funcion tiene como parametro param, i, y. "param" el cual es lo que le usuario escribe para poder hacer la comparacion de "facil", "medio" o "dificil"; "i"  "i" que es la varible de la iteracion, ya que esta funcion va necesariamente conectada para que se
    realice por cada tema la pregunta indica; "y" la necesitamos para generalizar los espacios del campo
    """
    x = 625
    y2 = y + 55
    pomodorofacil = 2
    pomodoromedio = 4
    pomodorodificil = 8
    tiempo_pomodoro = 0
    global count_global
    if parametro != "":
        if parametro == "fácil" or parametro =="facil" or parametro == "Facil" or parametro == "Fácil":
            tiempo_pomodoro = (25*pomodorofacil)
            parametro1 = ("En el tema "+ str(i+1)+ " debes estudiar " + str(tiempo_pomodoro) + " minutos.\nRecuerda que cada 25 minutos descansas 5 minutos.")
            etiqueta3 = Label(text=parametro1,font= ("Verdana",10),background="white")
            etiqueta3.place(x = x , y = y2)
        elif parametro == "medio" or parametro == "Medio":
            tiempo_pomodoro = (25*pomodoromedio)
            parametro2 = ("En el tema "+ str(i+1)+ " debes estudiar " + str(tiempo_pomodoro) +" minutos.\nRecuerda que cada 25 minutos descansas 15 minutos.")
            etiqueta4 = Label(text=parametro2, font= ("Verdana",10),background="white")
            etiqueta4.place(x=x, y = y2)
        elif parametro == "Difícil" or parametro == "difícil" or parametro == "dificil" or parametro =="Dificil":
            tiempo_pomodoro = (25*pomodorodificil)
            parametro3 =( "En el tema "+ str(i+1)+  " debes estudiar " + str(tiempo_pomodoro) +" minutos.\nRecuerda que cada 100 minutos descansas 25 minutos.")
            etiqueta5= Label(text=parametro3, font= ("Verdana",10),background="white")
            etiqueta5.place(x=x, y = y2)
        count_global = count_global + tiempo_pomodoro
        respuesta_final = ("La cantidad de minutos que vas a estudiar para esta asignatura es " + str(count_global))
    boton3 = Button(root, text="Continuar", command = lambda: Horario(respuesta_final)).place(x=930, y=950)



def limpiar():
    """
    Esta funcion se encarga de limpiar.
    """
    root.destroy()



def Horario(c):
    """
    Esta funcion crea una cuadricula  de labels y entrys.
    """
    limpiar()
    Horas = ["00:00/01:00", "01:00/02:00", "02:00/03:00", "03:00/04:00", "04:00/05:00",
         "05:00/06:00", "06:00/07:00", "07:00/08:00", "08:00/09:00", "09:00/10:00", "10:00/11:00",
         "12:00/13:00", "13:00/14:00", "14:00/15:00", "15:00/16:00", "16:00/17:00", "17:00/18:00",
         "18:00/19:00", "19:00/20:00", "20:00/21:00", "21:00/22:00", "22:00/23:00", "23:00/00:00"]
    Dias = ["LUNES","MARTES","MIERCOLES","JUEVES","VIERNES","SABADO","DOMINGO"]
    cont1 = 0
    cont2 = 0
    cont3 = 0
    etiqueta6 = Label(text="Horario",relief=RIDGE, width=15).grid(row=0, column=0)
    """
    Este for lo que hace es que para todos los elementos en la lista horas, primero se cree un label, y la coordenada de la fila se vaya sumando una para
    cada elemento, para que asi queden todas las horas de arriba a abajo en la primera columna.
    """
    for i in Horas:
        Label(text=i, relief=RIDGE, width=15).grid(row=1+cont1,column=0)
        Entry(relief=SUNKEN, width=15).grid(row=1+cont1,column=1)
        Entry(relief=SUNKEN, width=15).grid(row=1+cont1,column=2)
        Entry(relief=SUNKEN, width=15).grid(row=1+cont1,column=3)
        Entry(relief=SUNKEN, width=15).grid(row=1+cont1,column=4)
        Entry(relief=SUNKEN, width=15).grid(row=1+cont1,column=5)
        Entry(relief=SUNKEN, width=15).grid(row=1+cont1,column=6)
        Entry(relief=SUNKEN, width=15).grid(row=1+cont1,column=7)
        cont1 = cont1 + 1
    """
    El mismo proceso del for anterior se repite con los entry.
    """
    for i in Dias:
        Label(text=i, relief=RIDGE, width=15).grid(row=0,column=1+cont2)
        cont2 = cont2 + 1
    Label(text=c, relief=RIDGE, width= 109).grid(row=2+cont1,columnspan=7,column=1)





Grafica()
root.mainloop()
