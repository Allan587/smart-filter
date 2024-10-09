import tkinter as tk 

class SmartFilter(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master) 
        self.master = master
        self.pack()

def main():
    app = tk.Tk()
    app.title("SmartFilter")
    
    ventana = SmartFilter(app)
    ventana.mainloop()

if __name__ == "__main__": 
    main() 