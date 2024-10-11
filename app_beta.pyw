import tkinter as tk
from tkinter import Toplevel


def fonts():
    arial = "Arial"

#<------------------------------------------------------------------------------------------------------------------------>
class smartfilter_main:
    def __init__(self, root):
        self.root = root
                
        #self.ent()  
        self.lab()
        self.butt()
    
    def lab(self):
        lab = tk.Label(self.root, text="Smart Filter", bg="#E6E6FA", font=("Arial", 16))
        lab.grid(row=0, column=0, columnspan=3, sticky="nsew")
    
    def secondary(self):
        self.secondary_window = seconday_window(self)
        
    def third(self):
        self.third_window = third_window(self)
        
    def forth(self):
        self.forth_window = forth_window(self)
           
    def butt(self):
        butt_v = tk.Button(self.root, text="Apartado de Ventas", bg="#E6E6FA", command=self.secondary) .place(relx=0.35, rely=0.16, relwidth=0.3,  relheight=0.1)
        butt_i = tk.Button(self.root, text="Inventario", bg="#E6E6FA", command=self.third).place(relx=0.35, rely=0.3, relwidth=0.3,  relheight=0.1)
        butt_u = tk.Button(self.root, text="Actualización de Inventario", bg="#E6E6FA", command=self.forth).place(relx=0.35, rely=0.44, relwidth=0.3,  relheight=0.1)    
#<------------------------------------------------------------------------------------------------------------------------>       
class seconday_window:
    
    def __init__(self, Smartfilter_main):
        self.Smartfilter_main = Smartfilter_main
        
        
        self.ventana_secundaria = Toplevel()
        self.ventana_secundaria.title("Apartado de ventas")
        self.ventana_secundaria.grab_set()
        self.ventana_secundaria.geometry("800x500")
        
        self.btn()
        self.ent()
        
    def ent(self):
        
        self.entry = tk.Entry(self.ventana_secundaria)
        self.entry.place(relx=0.1, rely=0.1, relwidth=0.1, relheight=0.03, anchor="center")
        
    def btn(self):  
        cerrar_boton = tk.Button(self.ventana_secundaria, text="Salir", bg="Red", fg="White", command=self.ventana_secundaria.destroy).place(relx=0.85, rely=0.9, relwidth=0.1, relheight=0.05)
#<------------------------------------------------------------------------------------------------------------------------>       
class third_window:
    
    def __init__(self, Smartfilter_main):
        self.Smartfilter_main = Smartfilter_main
        
        
        self.third_window = Toplevel()
        self.third_window.title("Inventario")
        self.third_window.grab_set()
        self.third_window.geometry("800x500")
        self.btn()
        
    def btn(self):
        cerrar_boton = tk.Button(self.third_window, text="Salir", bg="Red", fg="White", command=self.third_window.destroy).place(relx=0.85, rely=0.9, relwidth=0.1, relheight=0.05)
#<------------------------------------------------------------------------------------------------------------------------>
class forth_window:
    
    def __init__(self, Smartfilter_main):
        self.Smartfilter_main = Smartfilter_main
        
        
        self.forth_window = Toplevel()
        self.forth_window.title("Actualización de Inventario")
        self.forth_window.grab_set()
        self.forth_window.geometry("800x500")
        self.btn()
        
    def btn(self):
        cerrar_boton = tk.Button(self.forth_window, text="Salir", bg="Red", fg="White", command=self.forth_window.destroy).place(relx=0.85, rely=0.9, relwidth=0.1, relheight=0.05)

#<------------------------------------------------------------------------------------------------------------------------>
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