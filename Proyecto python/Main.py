import Funciones as fc
from tkinter import messagebox
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import tkinter as tk
import pandas as pd

fc.Extraccion_datos("Pruebas_Resultados.xlsx")

def main():
    ventana = tb.Window(themename="superhero")
    ventana.title("Aplicacion")
    ventana.geometry("400x320")

    def handle_click():  # Handle button click event
        opcion_1.configure(text="opcion 1")
        
    def handle_click_13():
        messagebox.showinfo(
            "Información para el botón “Log in”",
            "Información"
        )

    entrada_texto = tb.Text(ventana, height=4, width=40, font=("Helvetica", 12), wrap="word")
    entrada_texto.grid(row=0, column=0, columnspan=2,padx=8, pady=8)
    entrada_texto.insert("1.0", "Acá va la pregunta")
    entrada_texto.config(state="disabled")
    
    boton_ejecutar_13 = tb.Button(ventana, text="?", command=handle_click_13, bootstyle="info")
    boton_ejecutar_13.grid(row=6, column=1, padx=8, pady=8)
   
    opcion_1 = tb.Label(ventana, text="_______________________", font=("Helvetica", 10), bootstyle="info")
    opcion_1.grid(row=1, column=0, padx=8, pady=8)
    boton_1 = tb.Button(ventana, text="Click opción", command=handle_click, bootstyle="success")
    boton_1.grid(row=2, column=0, padx=8, pady=8)
    
    opcion_2 = tb.Label(ventana, text="_______________________", font=("Helvetica", 10), bootstyle="info")
    opcion_2.grid(row=3, column=0, padx=8, pady=8)
    boton_2 = tb.Button(ventana, text="Click opción", command=handle_click, bootstyle="success")
    boton_2.grid(row=4, column=0, padx=8, pady=8)
    
    opcion_3 = tb.Label(ventana, text="_______________________", font=("Helvetica", 10), bootstyle="info")
    opcion_3.grid(row=1, column=1, padx=8, pady=8)
    boton_3 = tb.Button(ventana, text="Click opción", command=handle_click, bootstyle="success")
    boton_3.grid(row=2, column=1, padx=8, pady=8)
    
    opcion_4 = tb.Label(ventana, text="_______________________", font=("Helvetica", 10), bootstyle="info")
    opcion_4.grid(row=3, column=1, padx=8, pady=8)
    boton_4 = tb.Button(ventana, text="Click opción", command=handle_click, bootstyle="success")
    boton_4.grid(row=4, column=1, padx=8, pady=8)

    ventana.mainloop()

if __name__ == "__main__":
    main()
