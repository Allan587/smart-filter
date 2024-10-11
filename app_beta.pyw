import tkinter as tk
from tkinter import Toplevel
import threading as th

class smartfilter_main:
    def __init__(self, root):
        self.root = root
        
        #self.ent()  
        self.lab()
        self.butt()
    
    #def ent(self):
        
        #self.entry = tk.Entry(self.root)
        #self.entry.place(relx=0.1, rely=0.1, relwidth=0.1, relheight=0.03, anchor="center")
    
    def lab(self):
        lab = tk.Label(self.root, text="Smart Filter", bg="#E6E6FA", font=("Arial", 16))
        lab.grid(row=0, column=0, columnspan=3, sticky="nsew")
    
    def secondary(self):
        self.secondary_window = seconday_window(self)
        
    def third(self):
        self.third_window = third_window(self)
           
    def butt(self):
        butt_v = tk.Button(self.root, text="Apartado de Ventas", bg="#E6E6FA", command=self.secondary) .place(relx=0.41, rely=0.14, relwidth=0.2,  relheight=0.05)
        butt_i = tk.Button(self.root, text="Inventario", bg="#E6E6FA", command=self.third).place(relx=0.41, rely=0.21, relwidth=0.2,  relheight=0.05)
        butt_u = tk.Button(self.root, text="Actualización de Inventario", bg="#E6E6FA").place(relx=0.41, rely=0.28, relwidth=0.2,  relheight=0.05)
        
        
class seconday_window:
    
    def __init__(self, Smartfilter_main):
        self.Smartfilter_main = Smartfilter_main
        
        
        self.ventana_secundaria = Toplevel()
        self.ventana_secundaria.grab_set()
        self.ventana_secundaria.geometry("700x400")
        
        self.btn()
        
    def btn(self):
        cerrar_boton = tk.Button(self.ventana_secundaria, text="Cerrar", command=self.ventana_secundaria.destroy)
        cerrar_boton.pack(pady=20)
        
class third_window:
    
    def __init__(self, Smartfilter_main):
        self.Smartfilter_main = Smartfilter_main
        
        
        self.third_windo = Toplevel()
        self.third_windo.grab_set()
        self.third_windo.geometry("700x400")
        
        self.btn()
        
    def btn(self):
        cerrar_boton = tk.Button(self.third_windo, text="Cerrar", command=self.third_windo.destroy)
        cerrar_boton.pack(pady=20)

def main():
    root = tk.Tk()
    root.geometry("800x500") 
    root.minsize(800, 500)
    root.config(bg="lightblue")
    
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    
    app = smartfilter_main(root)

    root.mainloop()  
       
if __name__ == "__main__":
    main()