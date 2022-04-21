import tkinter as tk
from application import Application

def setup_app():
    app = Application()
    app.setup_ui()
    return app

if __name__ == "__main__":
    app = setup_app()
    app.window.mainloop()
