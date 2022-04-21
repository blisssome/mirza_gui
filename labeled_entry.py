import tkinter as tk

class LabeledEntry:

    def __init__(self, label_text: str, master: tk.Frame):
        self.label: tk.Label = tk.Label(text=label_text, width=25, master=master)
        self.entry: tk.Entry = tk.Entry(width=25, master=master)

    
    def pack(self):
        self.label.pack()
        self.entry.pack()
