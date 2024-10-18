import tkinter as tk
from PIL import Image, ImageTk

"""
JSON displayer in tkinter
Author: Seunghyeon (Hyeon) Kim
Link: https://www.w3resource.com/python-exercises/tkinter/python-tkinter-file-operations-and-integration-exercise-4.php
Copyright belongs to w3resource.com
"""

class TMExportHelper:
    """
    TMExportHelper
    Class to help exporting the material substitution table from Twin Motion.
    """
    def __init__(self, root, title):
        """
        initialization of class. Initializes necessary variables for the class to comprehend
        """
        # Initialize required variables
        self.root = root
        self.root.title(title)
        self.fullScreenVar = True
        self.pageCounter = 0
        self.instructions = [
                             "Please launch Twin Motion.", 
                             "Go to the Files Tab", 
                             "Click on Export Material IDs", 
                             "Choose the name and directory to save the material ID csv file."]

        self.root.title("Export Instructions")
        text_widget = tk.Text(self.root, wrap=tk.WORD, height=15, width=35)
        # Image Display Sequence
        self.image_label = tk.Label(self.root)
        self.image_label.pack(padx=20, pady=20, side=tk.TOP)
        # Full Screen Control Logic
        self.root.bind("<Escape>", self.end_fullscreen)
        self.root.bind("<F11>", self.toggle_fullscreen)
        # Buttons
        buttons = [
            tk.Button(self.root, text = "quit", command=self.root.destroy),
            tk.Button(self.root, text="next", command=self.nextPage),
            tk.Button(self.root, text="previous", command=self.prevPage)
        ]
        # Bottom right buttons
        for eachButton in buttons:
            eachButton.pack(side=tk.BOTTOM, padx=20, pady=5, anchor= 'e') # Pack each of the buttons with the same paddings and anchor
        minimizeWindowButton = tk.Button(self.root, text="minimize window", command=self.end_fullscreen)
        minimizeWindowButton.pack(side=tk.TOP, padx= 20, pady=5, anchor='w')
        self.status_label = tk.Label(self.root, text="", padx=20, pady=10)
        self.status_label.pack(side=tk.BOTTOM) # Text for instructions
        self.loadImg("./ExportInstructions/0.png", "Please launch Twin Motion.")
    def nextPage(self):
        """
        When "next" button is pressed, this will be the functionality of the button
        """
        if self.pageCounter == 3:
            return None
        self.loadImg(f"./ExportInstructions/{self.pageCounter+1}.png", self.instructions[self.pageCounter+1])
        self.pageCounter += 1
        self.pageCounter %= 4
    def prevPage(self):
        """
        When "prev" button is pressed, this will be the functionality of the button
        """
        if self.pageCounter == 0:
            return None
        self.loadImg(f"./ExportInstructions/{self.pageCounter-1}.png", self.instructions[self.pageCounter-1])
        self.pageCounter -= 1
        self.pageCounter %= 4
    def loadImg(self, imgPath, text):
        """
        Loads the requried image onto the image_label (only works when the mainloop is the main label)
        """
        resizedDim = (700, 400)
        photoDir= Image.open(imgPath)
        photoDir.thumbnail(resizedDim)
        photo = ImageTk.PhotoImage(photoDir)
        tk.PhotoImage(file=imgPath)
        self.image_label.config(image=photo)
        self.image_label.photo = photo
        
        self.status_label.config(text=text, font=("Arial", 15))

    def toggle_fullscreen (self, event=None):
        """
        This function toggles the full screen mode.
        """
        self.fullScreenVar = not self.fullScreenVar
        self.root.attributes('-fullscreen',self.fullScreenVar)

    def end_fullscreen (self, event=None):
        """
        This function ends the full screen mode.
        """
        self.fullScreenVar = False
        self.root.attributes('-fullscreen',False)