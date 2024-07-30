# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:08:59 2024

@author: Aidan
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("P180")
root.geometry("600x600")
root.config(bg="green")

titulo = Label(root, text="Traductor De Idiomas", bg="green")
titulo.place(relx=0.5, rely=0.1, anchor=CENTER)
ingresar_texto = Label(root, text="Ingresar texto", bg="green")
ingresar_texto.place(relx=0.02, rely=0.2, anchor=w)
area_de_texto = Text(root, bg="green", height=20, wrap, widht=100, padx=10, pady=10, bd)
area_de_texto.place(relx=0.02, rely=0.5, anchor=w)

language = list(LANGUAGES.values())

combobox = ttk.Combobox(root, state="readonly", value=1, width=20)
combobox.place(relx=0.2, rely=0.2, anchor=w)
combobox.set("spanish")

output = Label(root, text="Output", bg="green")
output.place(relx=0.8, rely=0.2, anchor=w)

combobox2 = ttk.combobox(root, state="readonly", value=1, width=20)
combobox2.place(relx=0.9, rely=0.2, anchor=CENTER)
combobox.set("Elige el idioma de output")

area_de_texto2 = Text(root, bg="green", heigth=20, wrap, widht=100, padx=10, pady=10, bd)
area_de_texto2.place(relx=0.98, rely=0.5, anchor=w)

traducir = Button(root, text="Traducir", bg="green", activebackground="lime", relief, pady=1, command=Translate)
traducir.place(relx=0.5, rely=0.8, anchor=w)

def Translate():
    i_origen = combobox.get()
    i_destino = combobox2.get()
    translator = Translator()
    try:translated = translator.translate(text= area_de_texto.get(1.0, End), src = src_lang.get(), dest= dest_lang.get())
    area_de_texto2.delete(1.0, END)
    area_de_texto2.insert(END, translated.text)

by = Label(root, text="Creado por Fer", bg="green")
by.place(relx=0.5, rely=0.9, anchor=CENTER)
    

root.mainloop()