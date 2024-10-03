import tkinter as tk
from tkinter import ttk
import json

"""
JSON displayer in tkinter
Author: Seunghyeon (Hyeon) Kim
Link: https://www.w3resource.com/python-exercises/tkinter/python-tkinter-file-operations-and-integration-exercise-4.php
Copyright belongs to w3resource.com
"""

class TK_JSON:
    def __init__(self, root, title, file):
        """
        initialization of class. Initializes necessary variables for the class to comprehend
        """
        # Initialize required variables
        self.root = root
        self.root.title(title)

        # Create a frame for displaying the data obtained
        self.frame = ttk.Frame(root)
        self.frame.pack(padx = 20, pady = 20, fill = tk.BOTH, expand=True)

        # Create a Text widget for displaying JSON content
        self.text_widget = tk.Text(self.frame, wrap=tk.WORD)
        self.text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a Scrollbar for the frame for JSON viewer
        self.scrollbar = ttk.Scrollbar(self.frame, command=self.text_widget.yview)
        self.scrollbar.pack(side = tk.RIGHT, fill=tk.Y)
        self.text_widget.config(yscrollcommand=self.scrollbar.set)

        # Load the data into the class
        self.load_json_data(file)

    def load_json_data(self, filedir):
        try:
            file = open(filedir, "r")
            jsonFileData = json.load(file)

            # Formatting JSON data as a string
            formattedJson = json.dumps(jsonFileData, indent=4)
            
            # insert it into the text widget
            self.text_widget.insert(tk.END, formattedJson)

            # Make the text widget uneditable
            self.text_widget.config(state=tk.DISABLED)
            
        except FileNotFoundError:
            self.text_widget.insert(tk.END, "Error code 000001: File not found.")
            self.text_widget.config(state=tk.DISABLED)