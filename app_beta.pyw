import tkinter as tk


class smartsilter:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x500") 
        self.ent()  
    
    def ent(self):
        
        self.entry = tk.Entry(self.root)
        self.entry.grid(column=1, row= 1, columnspan=2, sticky="w")
    
    
def main():
    root = tk.Tk()
    root.minsize(800, 500)
    app = smartsilter(root)

    root.mainloop()  
       
if __name__ == "__main__":
    main()