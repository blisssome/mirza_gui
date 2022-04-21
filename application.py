import tkinter as tk
from labeled_entry import LabeledEntry
from settings import Settings

class Application:


    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry(Settings.WINDOW_SIZE)
        self.window.title(Settings.WINDOW_TITLE)
        self.window.iconbitmap(Settings.WINDOW_ICON_PATH)
        self.window.resizable(False, False)


    def setup_ui(self):
        frame = tk.Frame(master=self.window)
        frequency_data = LabeledEntry(label_text="Path to frequencies dataset", master=frame)
        airports_data = LabeledEntry(label_text="Path to airports dataset", master=frame)
        runways_data = LabeledEntry(label_text="Path to runways dataset", master=frame)
        commit_btn = tk.Button(text="Load Data", width=10, height=1, master=frame)

        airports_data.pack()
        frequency_data.pack()
        runways_data.pack()
        commit_btn.pack()
        frame.pack()
