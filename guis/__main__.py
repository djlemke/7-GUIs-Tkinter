"""7 GUIs Tkinter
An implementation of the 7 GUIs tasks in Python using Tkinter and the standard
library.
"""
import typing
import tkinter as tk
from tkinter import ttk

from guis.counter import Counter
from guis.temperature_converter import TemperatureConverter
from guis.flight_booker import FlightBooker
from guis.timer import Timer
from guis.crud import Crud
from guis.circle_drawer import CircleDrawer
from guis.cells import Cells


class Launcher(ttk.Frame):
    """Launcher encapsulates the GUI into an object to prevent namespace
    pollution.
    """
    def __init__(self, parent: tk.Tk):
        """Initialize the GUI:
            1. Setup sizing
            2. Create widgets
        """
        super().__init__(parent)
        self.parent: tk.Tk = parent
        self.parent.geometry("300x250")
        self.parent.resizable(False, False)
        self.parent.title("7 GUIs Launcher")
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky="news", padx=4, pady=4)

        # Create buttons for each GUI.
        guis = [
            "Counter",
            "Temperature Converter",
            "Flight Booker",
            "Timer",
            "CRUD",
            "Circle Drawer",
            "Cells"]
        for i, gui_name in enumerate(guis):
            button = ttk.Button(
                self,
                text=gui_name,
                command=lambda name=gui_name: self.launch_gui(name))
            button.grid(row=i, column=0, padx=4, pady=4)
            self.columnconfigure(0, weight=1)

    def launch_gui(self, name: str):
        """Launches the selected GUI."""
        toplevel = tk.Toplevel(self.parent)
        match name:
            case "Counter":
                Counter(toplevel, tool=True)
            case "Temperature Converter":
                TemperatureConverter(toplevel, tool=True)
            case "Flight Booker":
                FlightBooker(toplevel, tool=True)
            case "Timer":
                Timer(toplevel, tool=True)
            case "CRUD":
                Crud(toplevel, tool=True)
            case "Circle Drawer":
                CircleDrawer(toplevel, tool=True)
            case "Cells":
                Cells(toplevel, tool=True)
            case _:
                toplevel.destroy()


ROOT: typing.Final[tk.Tk] = tk.Tk()
Launcher(ROOT)
ROOT.mainloop()
