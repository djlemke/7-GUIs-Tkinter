# 7 GUIs Tkinter

An implementation of the [7 GUIs](https://eugenkiss.github.io/7guis/) tasks using Python's built-in Tkinter library.

## Background

This project implements the tasks with a focus on modern Python practices: proper encapsulation, type hinting, and clear, reusable components, avoiding the common pitfalls of simple procedural scripts.

## Requirements

- Python 3.x

## Usage

All commands should be run from the root of the project directory.

### As an Application

Launch the main window to access all GUIs:
```sh
python -m guis
```

Or, run a specific GUI directly:
```sh
python guis/counter.py
```

### Code Usage

```python
import sys
import tkinter as tk

import guis.counter as counter


class MyCounter(counter.Counter):
    """A custom counter that increments by 2."""
    def __init__(self, parent):
        super().__init__(parent)
        parent.title("Increment by 2")

    def increment(self):
        """Increment the count by 2 instead of 1."""
        self.count.set(self.count.get() + 2)


def main():
    root = tk.Tk()
    MyCounter(root)
    root.mainloop()


if __name__ == "__main__":
    sys.exit(main())

```

## Maintainer

Daniel J. Lemke <daniel@lemketech.com>

https://lemketech.com/

https://github.com/djlemke

## Contributing

This package is not currently open for contributions.

## License

Licensed under the MIT License. See LICENSE for details.
