import tkinter as tk
from tkinter import ttk
from tkinter import *

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.title('Temp Converter')
        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand=True)

        self.what_temp_one = ttk.Label(self.mainframe,
                                       text="What what temperature would you like to convert from?",
                                       background="white",
                                       font=("Times New Roman", 10))
        self.what_temp_one.grid(row=0, column=0)

        temp_options = ["Fahrenheit", "Celsius", "Kelvin"]
        self.temp_one_options = ttk.Combobox(self.mainframe, values=temp_options)
        self.temp_one_options.grid(row=1, column=0, pady=10, sticky='NWES')

        self.conversion_temp = ttk.Entry(self.mainframe)
        self.conversion_temp.grid(row=2, column=0, sticky='NWES')

        self.convert_button = ttk.Button(self.mainframe, text="Convert", command=self.calculate())
        self.convert_button.grid(row=2, column=1, sticky='NWES')


        self.root.mainloop()
        return

    def calculate(self):
        temp = self.conversion_temp.get()
        self.what_temp_one.config(text=temp)



if __name__ == "__main__":
    App()
