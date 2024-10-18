import tkinter as tk
from tkinter import filedialog
from CSVGenUtil import CSVGenUtil
from tkJSONloader import TK_JSON
from helpExport import TMExportHelper
import json

"""
material replacement main GUI python script
Author: Seunghyeon (Hyeon) Kim
Description: This file contains the required GUI for the app. It unites all the utilities from
the other python file and offers functionality.
Date: Oct. 3 2024
"""

DEFAULT_FONT = 10

class CSVGUI:
    """
    CSVGUI Class used to dictate the CSVGenUtil with user interface
    """
    def __init__(self):
        """
        Define the default variables
        """
        self.indicator = 0
        try:
            settings = open("./settings.json")
            settingsJson = json.load(settings)
        # When unable to load previously saved settings, use factory defaults.
        except FileNotFoundError:
            self.indicator = 1
            print("settings.json not found. Loading default settings.")
            settings = None
            settingsJson = {
                "overallDir": ".", 
                "matSub" : "./DefaultMaterialSub/default_material_sub.json", 
                "mid" : "./DefaultMaterialSub/default_mid.csv",
                "savingDir" : "."
                }
        self.overallDirectory= settingsJson['overallDir']
        try:
            self.matSub = settingsJson['matSub']
            self.mid = settingsJson['mid']
            self.root = tk.Tk()
            self.root.geometry("1000x700")
            self.savingDir = settingsJson['savingDir']
        except FileNotFoundError:
            self.status_label.config(text = "Fatal Error! Please validate overall directory", font=("Arial", DEFAULT_FONT))
            print("Fatal Error! Please validate overall directory")
    def reloadVar(self):
        """
        After changing Directory, it must be reloaded into the variables that were declared with the previous variables.
        """
        try:
            settings = open(self.overallDirectory+"/settings.json")
        except FileNotFoundError:
            settings = None
        settingsJson = json.load(settings)
        try:
            self.matSub = self.overallDirectory + "/DefaultMaterialSub/default_material_sub.json" if settings == None else settingsJson['matSub']
            self.mid = self.overallDirectory + "/DefaultMaterialSub/default_mid.csv" if settings == None else settingsJson['mid']
            self.savingDir = self.overallDirectory if settings == None else settingsJson['savingDir']
        except FileNotFoundError:
            self.status_label.config(text = "Fatal Error! Please validate overall directory", font=("Arial", DEFAULT_FONT))
            print("Fatal Error! Please validate overall directory")
    def browsingFolder(self):
        """
        Open a file browser to look for the folder for default directory.
        """
        filename = filedialog.askdirectory(initialdir = '/',
                                                title = "Select the default directory")
        self.status_label.config(text = "folder directory Saved as " + filename, font=("Arial", DEFAULT_FONT))
        print("folder directory Saved as " + filename)
        self.overallDirectory = filename
        self.reloadVar()
    def browsingInputJSONFile(self):
        """
        Open a file browser to look for JSON files for input purposes.
        """
        filename = filedialog.askopenfilename(initialdir = '/',
                                                title = "Select a JSON file",
                                                filetypes = (("JSON files", "*.json*"), 
                                                            ("All files", "*.*")))
        self.status_label.config(text = "JSON input saved as " + filename, font=("Arial", DEFAULT_FONT))
        print("JSON Saved as " + filename)
        self.matSub = filename
    def browsingMIDFile(self):
        """
        Open a file browser to look for Twinmotion-exported CSV files.
        """
        filename = filedialog.askopenfilename(initialdir = '/',
                                                title = "Select a CSV file",
                                                filetypes = (("CSV files", "*.csv*"), 
                                                            ("All files", "*.*")))
        self.status_label.config(text = "Material ID input saved as " + filename, font=("Arial", DEFAULT_FONT))
        print("MID Saved as " + filename)
        self.mid = filename
    def helpMIDExport(self):
        """
        Create an image port view to show how to export material ID from Twin Motion
        """
        subRoot = tk.Toplevel()
        subRoot.attributes('-fullscreen',True)
        TMExportHelper(subRoot, "Material ID Export Instructions")
        subRoot.mainloop()
    def browsingSavingFolder(self):
        """
        Open a file browser to look for the folder for default directory.
        """
        filename = filedialog.askdirectory(initialdir = '/',
                                                title = "Select the default directory")
        print("folder directory Saved as " + filename)
        self.status_label.config(text = "Saving directory saved as " + filename, font=("Arial", DEFAULT_FONT))
        self.savingDir = filename
    def saveCsv(self):
        """
        Save the input JSON into the CSV format.
        """
        util = CSVGenUtil(self.matSub, self.mid)
        if self.classTname:
            util.readInInp_class_name_struct(self.savingDir)
        else:
            util.readInInp_name_struct(self.savingDir)
        self.status_label.config(text = "CSV file successfully saved in " + self.savingDir, font=("Arial", DEFAULT_FONT))
    def help1JSON (self):
        subRoot = tk.Tk()
        directory = self.overallDirectory+"/ExampleJSON/class_name_struct_sample.json"
        TK_JSON(subRoot, "sampleJSONViewer", directory)
        subRoot.mainloop()
    def help2JSON (self):
        subRoot = tk.Tk()
        directory = self.overallDirectory+"/ExampleJSON/name_struct_sample.json"
        TK_JSON(subRoot, "sampleJSONViewer", directory)
        subRoot.mainloop()
    def setDefault (self):
        """
        Saving the current environmental variables.
        """
        tempDict = {
            "overallDir" : self.overallDirectory,
            "matSub" : self.matSub,
            "mid" : self.mid,
            "savingDir" : self.savingDir
        }
        self.status_label.config(text = "Default settings saved in the current working directory.", font=("Arial", DEFAULT_FONT))
        json_obj = json.dumps(tempDict)
        with open(self.overallDirectory+'/settings.json', "w") as output:
            output.write(json_obj)
    def classTnameToggle(self):
        self.classTname = not(self.classTname)
    def main(self):
        """
        mainloop of the user interface.
        """
        self.classTname = True
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        filemenu = tk.Menu(menu)
        # Create a drop down menu (e.x. word - file tab)
        menu.add_cascade(label='File', menu=filemenu)
        # Various interation with the drop down menu
        filemenu.add_command(label='Add input JSON file', command = self.browsingInputJSONFile)
        filemenu.add_command(label='Add constant Material ID file', command = self.browsingMIDFile)
        filemenu.add_command(label='Change default directory', command = self.browsingFolder)
        filemenu.add_command(label='Change saving directory for final csv', command = self.browsingSavingFolder)
        helpmenu = tk.Menu(menu)
        # Another dropdown menu 
        menu.add_cascade(label='Help', menu=helpmenu)
        # Various parts to be able to help out the user.
        helpmenu.add_command(label='How do I export material IDs from Twinmotion?', command=self.helpMIDExport)#self.helpMIDExport
        helpmenu.add_command(label='How do I format the JSON file as class-name-input format?', command=self.help1JSON)
        helpmenu.add_command(label='How do I format the JSON file as name-input format?', command=self.help2JSON)
        # saving formatted CSV
        localButtons = [
            tk.Button(self.root, text = 'save default settings', command = self.setDefault),
            tk.Button(self.root, text = 'save csv', command=self.saveCsv),
            tk.Checkbutton(self.root, text='name-input format for JSON',
                           height=5, 
                           width = 20, 
                           command=self.classTnameToggle)
        ]
        for eachButton in localButtons:
            eachButton.pack(side=tk.BOTTOM, anchor='e', padx=20, pady=10)
        self.status_label = tk.Label(self.root, text="setting.json was not found, so default settings was loaded." if self.indicator == 1 else "Great preparation! Your settings.json from the previous trial was successfully saved, and reloaded this instance!", padx=20, pady=10)
        self.status_label.pack(side=tk.BOTTOM) # Text for instructions
        self.root.title("Material Conversion Table CSV Generator")
        self.root.mainloop()

GUIClass = CSVGUI()
GUIClass.main()
