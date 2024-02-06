# -*- coding: utf-8 -*-
"""
Created on Wed 07 Feb 2024

Author: YIJU WU (gn02129251)

File: app.py

Topic: This module includes a template class for application development.

"""
import tkinter as tk


class App(tk.TK):
    def __init__(self, title, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(title)
        self.geometry("800x600")
        self.resizable(width=False, height=False)
        self.create_widgets()

        # Configure padding for all child widgets to optimize application apperance
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def create_widgets(self):
        pass  # Overwrite in subclass


def main(*args):
    return 0


if __name__ == "__main__":
    main()
