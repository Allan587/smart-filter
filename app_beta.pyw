import tkinter as tk
from tkinter import Toplevel

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
        self.secondary_window = sales(self)
        
    def third(self):
        self.third_window = inventory(self)
        
    def forth(self):
        self.forth_window = update_in(self)
           
    def butt(self):
        butt_v = tk.Button(self.root, text="Apartado de Ventas", bg="Grey", command=self.secondary) .place(relx=0.35, rely=0.16, relwidth=0.3,  relheight=0.1)
        butt_i = tk.Button(self.root, text="Inventario", bg="Grey", command=self.third).place(relx=0.35, rely=0.3, relwidth=0.3,  relheight=0.1)
        butt_u = tk.Button(self.root, text="Actualización de Inventario", bg="Grey", command=self.forth).place(relx=0.35, rely=0.44, relwidth=0.3,  relheight=0.1)    
#<------------------------------------------------------------------------------------------------------------------------>       
class sales:
    
    def __init__(self, Smartfilter_main):
        self.Smartfilter_main = Smartfilter_main
        
        
        self.Sales = Toplevel()
        self.Sales.title("Apartado de ventas")
        self.Sales.grab_set()
        self.Sales.minsize(800, 500)
        self.Sales.config(bg="lightblue")
        self.Sales.geometry("800x500")
        
        self.btn()
        self.ent()
        self.lbl()
        
    def lbl(self):
        #inf = list("ID producto", "Nombre", "Marca", "Tipo", "Stock") Terminar y hacer un range con estos datos
        
        lbl_id = tk.Label(self.Sales, text="ID producto", bg="Grey").place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
        lbl_n = tk.Label(self.Sales, text="Nombre", bg="Grey").place(relx=0.17, rely=0.05, relwidth=0.1, relheight=0.05)
        lbl_m = tk.Label(self.Sales, text="Marca", bg="Grey").place(relx=0.29, rely=0.05, relwidth=0.1, relheight=0.05)
        lbl_q = tk.Label(self.Sales, text="Cantidad", bg="Grey").place(relx=0.41, rely=0.05, relwidth=0.1, relheight=0.05)
        
    def ent(self):
        
        self.ent_id = tk.Entry(self.Sales).place(relx=0.05, rely=0.12, relwidth=0.1, relheight=0.05)
        self.ent_n =  tk.Entry(self.Sales).place(relx=0.17, rely=0.12, relwidth=0.1, relheight=0.05)
        self.ent_m =  tk.Entry(self.Sales).place(relx=0.29, rely=0.12, relwidth=0.1, relheight=0.05)
        self.ent_q =  tk.Entry(self.Sales).place(relx=0.41, rely=0.12, relwidth=0.1, relheight=0.05)
        
    def btn(self):  
        cerrar_boton = tk.Button(self.Sales, text="Salir", bg="Red", fg="White", command=self.Sales.destroy).place(relx=0.85, rely=0.9, relwidth=0.1, relheight=0.05)
#<------------------------------------------------------------------------------------------------------------------------>       
class inventory:
    
    def __init__(self, Smartfilter_main):
        self.Smartfilter_main = Smartfilter_main
        
        
        self.inventory = Toplevel()
        self.inventory.title("Inventario")
        self.inventory.grab_set()
        self.inventory.minsize(800, 500)
        self.inventory.config(bg="lightblue")
        self.inventory.geometry("800x500")
        
        self.btn()
        self.lbl()
        self.ent()
            
    def lbl(self):
        #inf = list("ID producto", "Nombre", "Marca", "Tipo", "Stock") Terminar y hacer un range con estos datos
        
        lbl_id = tk.Label(self.inventory, text="ID producto", bg="Grey").place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
        lbl_n = tk.Label(self.inventory, text="Nombre", bg="Grey").place(relx=0.17, rely=0.05, relwidth=0.1, relheight=0.05)
        lbl_m = tk.Label(self.inventory, text="Marca", bg="Grey").place(relx=0.29, rely=0.05, relwidth=0.1, relheight=0.05)
        lbl_t = tk.Label(self.inventory, text="Tipo", bg="Grey").place(relx=0.41, rely=0.05, relwidth=0.1, relheight=0.05)
        lbl_s = tk.Label(self.inventory, text="Stock", bg="Grey").place(relx=0.53, rely=0.05, relwidth=0.1, relheight=0.05)
        
    def ent(self):
        
        self.ent_id = tk.Entry(self.inventory).place(relx=0.05, rely=0.12, relwidth=0.1, relheight=0.05)
        self.ent_n =  tk.Entry(self.inventory).place(relx=0.17, rely=0.12, relwidth=0.1, relheight=0.05)
        self.ent_m =  tk.Entry(self.inventory).place(relx=0.29, rely=0.12, relwidth=0.1, relheight=0.05)
        self.ent_t =  tk.Entry(self.inventory).place(relx=0.41, rely=0.12, relwidth=0.1, relheight=0.05)
        self.ent_s =  tk.Entry(self.inventory).place(relx=0.53, rely=0.12, relwidth=0.1, relheight=0.05)
        
    def btn(self):
        cerrar_boton = tk.Button(self.inventory, text="Salir", bg="Red", fg="White", command=self.inventory.destroy).place(relx=0.85, rely=0.9, relwidth=0.1, relheight=0.05)
#<------------------------------------------------------------------------------------------------------------------------>
class update_in:
    
    def __init__(self, Smartfilter_main):
        self.Smartfilter_main = Smartfilter_main
        
        
        self.update_inventory = Toplevel()
        self.update_inventory.title("Actualización de Inventario")
        self.update_inventory.grab_set()
        self.update_inventory.minsize(800, 500)
        self.update_inventory.config(bg="lightblue")
        self.update_inventory.geometry("800x500")
        self.btn()
        
    def btn(self):
        cerrar_boton = tk.Button(self.update_inventory, text="Salir", bg="Red", fg="White", command=self.update_inventory.destroy).place(relx=0.85, rely=0.9, relwidth=0.1, relheight=0.05)

#<------------------------------------------------------------------------------------------------------------------------>
def main():
    root = tk.Tk()
    root.geometry("800x500")
    root.title("smart_filter") 
    root.minsize(800, 500)
    root.config(bg="lightblue")
    
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    
    app = smartfilter_main(root)

    root.mainloop()  
       
if __name__ == "__main__":
    main()