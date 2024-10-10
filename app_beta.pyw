import tkinter as tk
from tkinter import Toplevel

class smartsilter:
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
        
    def abrir_ventana_secundaria(self):
        ventana_secundaria = Toplevel(self.root)
    
        # Establecer el tamaño de la ventana secundaria
        ventana_secundaria.geometry("700x400")
    
        ventana_secundaria.grab_set() 
        ventana_secundaria.transient(self.root)  
        
        ventana_secundaria.resizable(False, False)

        cerrar_boton = tk.Button(ventana_secundaria, text="Cerrar", command=ventana_secundaria.destroy)
        cerrar_boton.pack(pady=20)

    
        ventana_secundaria.update_idletasks()
        x = self.root.winfo_x() + 100
        y = self.root.winfo_y() + 50
        ventana_secundaria.geometry(f"+{x}+{y}")  # Posicionar dentro de la ventana principal
        
    def limit_window(self, event):
        # Obtener las dimensiones de la ventana principal
        root_x = self.root.winfo_x()
        root_y = self.root.winfo_y()
        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()

        sec_x = self.abrir_ventana_secundaria.winfo_x()
        sec_y = self.abrir_ventana_secundaria.winfo_y()

    
        if sec_x < root_x:
            self.abrir_ventana_secundaria.geometry(f"+{root_x}+{sec_y}")
        elif sec_x + 200 > root_x + root_width:  
            self.abrir_ventana_secundaria.geometry(f"+{root_x + root_width - 200}+{sec_y}")

        if sec_y < root_y:
            self.abrir_ventana_secundaria.geometry(f"{self.abrir_ventana_secundaria.winfo_width()}x{self.abrir_ventana_secundaria.winfo_height()}+{sec_x}+{root_y}")
        elif sec_y + 150 > root_y + root_height:  
            self.abrir_ventana_secundaria.geometry(f"{self.abrir_ventana_secundaria.winfo_width()}x{self.abrir_ventana_secundaria.winfo_height()}+{sec_x}+{root_y + root_height - 150}")
    
    def butt(self):
        butt_v = tk.Button(self.root, text="Apartado de Ventas", bg="#E6E6FA", command=self.abrir_ventana_secundaria).place(relx=0.41, rely=0.14, relwidth=0.2,  relheight=0.05)
        butt_i = tk.Button(self.root, text="Inventario", bg="#E6E6FA").place(relx=0.41, rely=0.21, relwidth=0.2,  relheight=0.05)
        butt_u = tk.Button(self.root, text="Actualización de Inventario", bg="#E6E6FA").place(relx=0.41, rely=0.28, relwidth=0.2,  relheight=0.05)


def main():
    root = tk.Tk()
    root.geometry("800x500") 
    root.minsize(800, 500)
    root.config(bg="lightblue")
    
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    app = smartsilter(root)

    root.mainloop()  
       
if __name__ == "__main__":
    main()