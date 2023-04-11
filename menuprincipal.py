import tkinter as tk
import tkinter.font as tkFont
from tkinter.ttk import *

class App:
    def __init__(self, root):
        #setting title
        root.title("Algoritmos de Búsqueda")
        #setting window size
        width=1200
        height=800
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        label_1=tk.Label(root)
        ft = tkFont.Font(family='Times',size=38)
        label_1["font"] = ft
        label_1["fg"] = "#333333"
        label_1["justify"] = "center"
        label_1["text"] = "Bienvenido"
        label_1.place(x=0,y=20,width=306,height=50)
        

        label_2=tk.Label(root)
        ft = tkFont.Font(family='Times',size=33)
        label_2["font"] = ft
        label_2["fg"] = "#333333"
        label_2["justify"] = "center"
        label_2["text"] = "¿Qué desea ver?"
        label_2.place(x=50,y=130,width=346,height=56)

        btn_prof=tk.Button(root)
        btn_prof["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=28)
        btn_prof["font"] = ft
        btn_prof["fg"] = "#000000"
        btn_prof["justify"] = "center"
        btn_prof["text"] = "Algoritmo de Primero en Profundidad"
        btn_prof.place(x=90,y=230,width=1020,height=160)
        btn_prof["command"] = self.btn_prof_command
        

        btn_expa=tk.Button(root)
        btn_expa["anchor"] = "center"
        btn_expa["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=28)
        btn_expa["font"] = ft
        btn_expa["fg"] = "#000000"
        btn_expa["justify"] = "center"
        btn_expa["text"] = "Algoritmo de Expansión"
        btn_expa.place(x=90,y=440,width=1020,height=160)
        btn_expa["command"] = self.btn_expa_command

        btn_salir=tk.Button(root)
        btn_salir["bg"] = "#ff8484"
        ft = tkFont.Font(family='Times',size=23)
        btn_salir["font"] = ft
        btn_salir["fg"] = "#ffffff"
        btn_salir["justify"] = "center"
        btn_salir["text"] = "Salir"
        btn_salir.place(x=490,y=690,width=195,height=59)
        btn_salir["command"] = self.btn_salir_command

    def btn_prof_command(self):
        prof = tk.Toplevel(root)
        prof.title("Algoritmo de Primero en Profundidad")
        prof.geometry("1200x800")
        

    def btn_expa_command(self):
        print("command")


    def btn_salir_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
