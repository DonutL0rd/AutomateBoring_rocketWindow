import tkinter as tk
from tkinter import ttk


class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('250x275')
        self.root.title('test app')
        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand=True)

        self.text = ttk.Label(self.mainframe, text='Hello World', background='white', font=("Times New Roman", 16))
        self.text.grid(row=0, column=0)

        self.set_text_field = ttk.Entry(self.mainframe)
        self.set_text_field.grid(row=1, column=0, pady=10, sticky="NWES")

        set_text_button = ttk.Button(self.mainframe, text='Set Text', command=self.set_text)
        set_text_button.grid(row=1, column=1)

        color_options = ["red", "blue", "black"]
        self.set_color_field = ttk.Combobox(self.mainframe, values=color_options)
        self.set_color_field.grid(row=2, column=0, pady=10, sticky="NWES")

        color_options_button = ttk.Button(self.mainframe, text='Set Color', command=self.set_color)
        color_options_button.grid(row=2, column=1)

        self.root.mainloop()
        return

    def set_text(self):
        new_text = self.set_text_field.get()
        self.text.config(text=new_text)

    def set_color(self):
        new_color = self.set_color_field.get()
        self.text.config(foreground=new_color)


if __name__ == "__main__":
    App()
