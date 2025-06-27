"""7 GUIs Counter

An implementation of the 7 GUIs Counter task. It is designed to run with only
the Python standard library.
"""
import typing
import sys
import tkinter as tk
from tkinter import ttk


class Counter(ttk.Frame):
    """Counter encapsulates the GUI into an object to prevent namespace
    pollution.
    """
    def __init__(self, parent: tk.Tk | tk.Toplevel, tool: bool = False):
        """Initialize the GUI:
            1. Setup sizing
            2. Create widgets
            3. Focus the counter button and bind Return to it
        """
        super().__init__(parent, padding="4")
        parent.geometry('250x200')
        parent.resizable(False, False)
        parent.title('Counter')
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.bind('<Escape>', lambda e: parent.destroy())

        if tool:
            # The type stubs for this method are complex, so we ignore the
            # Pylance warning.
            parent.wm_attributes('-toolwindow', True) # type: ignore

        self.grid(row=0, column=0, sticky="news")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.count = tk.IntVar()
        self.count.set(0)
        count_entry = ttk.Entry(
            self,
            textvariable=self.count,
            state='readonly',
            width=10)
        count_entry.grid(row=0, column=0, padx=4, pady=4)
        count_button = ttk.Button(self,
                                 text='Increment',
                                 command=self.increment,
                                 default='active')
        count_button.grid(row=0, column=1, padx=4, pady=4)
        count_button.focus()
        count_button.bind('<Return>', lambda e: count_button.invoke())

    def increment(self) -> None:
        """Increment the count."""
        self.count.set(self.count.get() + 1)


def main():
    """Main entry point."""
    root: typing.Final[tk.Tk] = tk.Tk()
    Counter(root)
    root.mainloop()
    return 0


if __name__ == '__main__':
    sys.exit(main())
