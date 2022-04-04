#Programa que Agrega la interfaz GUI
#Author: Jose Perez.

from tkinter import *

tituloVentana = str("Mi aplicacion")

class Guiaplication:
    
    def __init__(self):
        print("Interfaz iniciada")

        #Constructor de la instancia de la appp
        ventana = tkinter.Tk()

        #Configuracion del atributo para que la aplicacion siempre
        #este por encima de todo lo demas
        # atributos: "-alpha, 1.0", 
        ventana.attributes("-topmost", True)
        
        mainFrame = tkinter.Frame(ventana,
                                  background = "red",
                                  #width = 30,
                                  #height=30,
                                  relief = "raised",
                                  borderwidth = 4)
        mainFrame.pack(side = "left", fill = "both", expand = 1)
        
        
                
        ventana.geometry("400x200")
        ventana.title(tituloVentana)
        entrytest = tkinter.Entry(mainFrame,background = "white")
        entrytest.pack()
        

        #eMensaje = tkinter.Label(ventana, text = "Hola")
        #eMensaje.pack()
        
        ventana.mainloop()


