from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import time
import polynanna

class PolyNannaApp:

    def __init__(self, master):

        master.title('PolyNanna')
        master.resizable(False, False)
        master.configure(background = '#db7070')

        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#db7070')
        self.style.configure('TButton', background = '#db7070')
        self.style.configure('TLabel', background = '#db7070')

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.logo = PhotoImage(file = 'fran_hat.gif')
        self.readme_text = """PolyNanna Gift Exchange Application \n
A program designed to randomize a pollyanna gift exchange with familial restrictions. \n
Rule Specifications \n
Parents cannot give to their children.
Children cannot give to their parents.
Siblings cannot give to each other.
Spouses/Couples cannot give to each other."""
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0)
        ttk.Label(self.frame_header, wraplength = 245, text = self.readme_text).grid(row = 0, column = 1, sticky = 'nw')

        self.button_header = ttk.Frame(master)
        self.button_header.pack()

        ttk.Button(self.button_header, text='Run Drawing', command = self.run_drawing, width = 30).grid(row=0, column=0)

    def run_drawing(self):
        start_time = time()
        polynanna.main()
        runtime = round((time() - start_time), 5)
        messagebox.showinfo(title = 'Success', message = 'You are awesome. Drawing completed in {} seconds.'.format(runtime))

def main():

    root = Tk()
    app = PolyNannaApp(root)
    root.mainloop()

if __name__ == '__main__': main()