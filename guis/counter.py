"""7 GUIs Counter

An implementation of the 7 GUIs Counter task. It is designed to run with only
the Python standard library.
"""
import tkinter as tk
from tkinter import ttk


class Counter(ttk.Frame):
    """Counter encapsulates the GUI into an object to prevent namespace
    pollution.
    """
    def __init__(self, parent):
        """Initialize the GUI:
            1. Setup sizing
            2. Create widgets
            3. Focus the counter button and bind Return to it
        """
        super().__init__(parent)
        # This GUI looks like ugly butt when maximized. This is a simple way
        # to prevent maximizing to fill the screen but still allowing some
        # user resizing in case their screen geometry is different.
        screen_width = parent.winfo_screenwidth()
        screen_height = parent.winfo_screenheight()
        initial_width = screen_width // 10
        initial_height = screen_height // 10
        max_width = initial_width * 2
        max_height = initial_height * 2
        parent.title("Counter")
        parent.geometry(f"{initial_width}x{initial_height}")
        parent.maxsize(max_width, max_height)

        mainframe = ttk.Frame(parent, padding="4")
        mainframe.grid(row=0, column=0, sticky="news")
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        mainframe.columnconfigure(0, weight=1)
        mainframe.columnconfigure(1, weight=1)
        mainframe.rowconfigure(0, weight=1)

        self.count = tk.IntVar()
        self.count.set(0)
        count_entry = ttk.Entry(
            mainframe,
            textvariable=self.count,
            state="readonly",
            width=10)
        count_entry.grid(row=0, column=0, padx=4, pady=4)
        count_button = ttk.Button(mainframe,
                                 text="Increment",
                                 command=self.increment)
        count_button.grid(row=0, column=1, padx=4, pady=4)
        count_button.focus()
        count_button.bind("<Return>", self.increment)

    # pylint will complain about unused args but that is wrong. args is
    # implicity sent when the method is bound to a widget.
    def increment(self, *args):
        """Increment the count."""
        self.count.set(self.count.get() + 1)


if __name__ == "__main__":
    root = tk.Tk()
    counter = Counter(root)
    counter.mainloop()
