"""7 GUIs Temperature Converter

An implementation of the 7 GUIs Temperature Converter task. It is designed to
run with only the Python standard library.
"""
import typing
import sys
import tkinter as tk
from tkinter import ttk


class TemperatureConverter(ttk.Frame):
    """TemperatureConverter encapsulates the GUI into an object to prevent
    namespace pollution.
    """
    def __init__(self, parent: tk.Tk | tk.Toplevel, tool: bool = False):
        """Initialize the GUI:
            1. Setup sizing
            2. Create widgets
        """
        super().__init__(parent, padding="4")
        parent.geometry('300x75')
        parent.resizable(False, False)
        parent.title('Temperature Converter')
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.bind('<Escape>', lambda e: parent.destroy())

        if tool:
            # The type stubs for this method are complex, so we ignore the
            # Pylance warning.
            parent.wm_attributes('-toolwindow', True)  # type: ignore

        self.grid(row=0, column=0, sticky="news")


def main():
    """Main entry point."""
    root: typing.Final[tk.Tk] = tk.Tk()
    TemperatureConverter(root)
    root.mainloop()
    return 0


if __name__ == '__main__':
    sys.exit(main())