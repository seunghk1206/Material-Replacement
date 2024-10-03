"""
CSVGenUtil.py
Author: Seunghyeon (Hyeon) Kim
Date: Sep. 23 2024
"""

import csv
import json

class CSVGenUtil:
    """
    TwinMotion-desired material substitution CSV table generator. This class serves purpose to
    abstractify the original functions.
    """
    def __init__(self, inpFile, midFile):
        """
        Initiates the CSVGenUtil Class. This is a required step to use any of the other methods in the class.

        :param string inpFile: input file as a JSON
        :param string midFile: the material ID file. If not given properly, the class will load the default file
        """
        # Variable Declarations
        inpFileOpen = open(inpFile, mode='r')
        try:
            constFile = open(midFile, mode='r')
        except FileNotFoundError as e:
            constFile = open('./DefaultMaterialSub/default_mid.csv', mode='r')
        self.material_sub_dict = json.load(inpFileOpen)
        constCsv = csv.reader(constFile, delimiter=",")
        self.the_dict = {rows[1]:rows[2] for rows in constCsv}
        # Constant Variable Declarations
        # Create the header for the output csv file
        header = [
            '#Row ID', 
            'Row Name', 
            'Subsitution Type', 
            'Filter', 
            'Condition', 
            'Value', 
            'TM Library GUID', 
            'Instance Type', 
            'Parameter Overrides >>>'
            ]
        # Initiate the a list to be written into the resultant csv file
        self.outputFileL = [header]
        # Initiate the index counter
        self.i = 0
    def readInInp_class_name_struct(self, savingDir):
        """
        Creates a csv file for the material replacement table in a TwinMotion-desired format. This method should be
        used when the JSON file format is class - name - inputs
        """
        # Utilize each key of the dictionary
        for eachKey in self.material_sub_dict:
            # within each key, there is a categorical reference to the actual material to be replaced
            for eachInnerKey in self.material_sub_dict[eachKey]:
                # forge the 'actual' name of the texture to be replaced
                csv_name = eachKey+"_-_"+eachInnerKey.replace(" ", "_")
                # reference the sub dictionary of each material to be replaced
                currentDict = self.material_sub_dict[eachKey][eachInnerKey]
                if not('material_name' in currentDict) or not(currentDict['material_name'] in self.the_dict):
                    print ("The material name for " + csv_name + " is not valid. Please fix it in the JSON input file.")
                    continue
                # for each material, create a row to be written in the csv file
                currentL = [self.i, currentDict['material_name'], 'Material', 'Name', 'Equals', csv_name, self.the_dict[currentDict['material_name']], 'Copy']
                # there might not be any inputs for additional inputs section, so make it into an edge case
                if 'additional_inputs' in currentDict: 
                    if currentDict['additional_inputs'] != None:
                        for eachAI in currentDict['additional_inputs']:
                            currentL.append(eachAI)
                self.outputFileL.append(currentL)
                self.i+=1

        outputFile = open(savingDir+'/ReplacementJSONOutput.csv', 'w', newline='')
        writer = csv.writer(outputFile)
        writer.writerows(self.outputFileL)
    def readInInp_name_struct(self,savingDir):
        """
        Creates a csv file for the material replacement table in a TwinMotion-desired format. This method should be
        used when the JSON file format is name - inputs
        """
        # Utilize each key of the dictionary
        for eachKey in self.material_sub_dict:
            # forge the 'actual' name of the texture to be replaced
            csv_name = eachKey.replace(" ", "_")
            # reference the sub dictionary of each material to be replaced
            currentDict = self.material_sub_dict[eachKey]
            if not('material_name' in currentDict) or not(currentDict['material_name'] in self.the_dict):
                print ("The material name for " + csv_name + " is not valid. Please fix it in the JSON input file.")
                continue
            # for each material, create a row to be written in the csv file
            currentL = [self.i, currentDict['material_name'], 'Material', 'Name', 'Equals', csv_name, self.the_dict[currentDict['material_name']], 'Copy']
            # there might not be any inputs for additional inputs section, so make it into an edge case
            if 'additional_inputs' in currentDict: 
                if currentDict['additional_inputs'] != None:
                    for eachAI in currentDict['additional_inputs']:
                        currentL.append(eachAI)
            self.outputFileL.append(currentL)
            self.i+=1

        outputFile = open(savingDir+'/ReplacementJSONOutput.csv', 'w', newline='')
        writer = csv.writer(outputFile)
        writer.writerows(self.outputFileL)