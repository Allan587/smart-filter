import tkinter as tk 

class SmartFilter(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master) 
        self.master = master
        self.pack()
        
        self.entradas()
        
    def entradas(self):
        cantidad = tk.Entry(self, justify="left")
        cantidad.grid(row=1, column=0)
        
def main():
    app = tk.Tk()
    app.title("SmartFilter")
    app.geometry("600x400")
    
    ventana = SmartFilter(app)
    ventana.mainloop()

if __name__ == "__main__": 
    main() 