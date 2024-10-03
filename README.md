# Hi there 👋
This is an application to help material substitution from ArchiCAD material to Twinmotion material. There are some default settings done for you, but the app may be modified for your own convenience!

## Requirements
Overall, only the ZIP file that will be containing this readme file and the other files will be needed. For installation of the application, I would like to recommend keeping the exe inside the unzipped folder. Otherwise, it must be inevitable to manually set the directory for the overall directory.

### Input Requirements

#### JSON Input
In order to correctly execute the program, the correct format for the JSON input is required. The sample JSON structure can be seen under the help navigator ("How do I format the JSON file as class-name-input format?" and "How do I format the JSON file as name-input format?"). To change the input JSON file, please find "File > Add input JSON file". To change the material ID csv file, please find "File > Add constant Material ID file". To change the default directory for the required default files, please find "File > Change default directory".

#### Material ID input
The material ID table from Twinmotion is also required for substitution to its UUID. The instructions to export the Material ID csv is given in one of the help tabs ("How do I export material IDs from Twinmotion?").

#### Toggling
You can toggle between the name-input structure mode and class-name-input structure mode by the checkbox indicating "name-input format for JSON". If done, it will save the CSV file with the desired structure.

### Output Requirements
The results will be saved in the desired directory saved within one instance of the app or settings.json file. If you would like to change the saving directory, please find "File > Change saving directory for final csv".

## Side notes
 * If the saved directory indicates ".", it means that the file was directed/saved in the directory which the current executable binary file is located in.
 * Whenever there is a FATAL ERROR, then it indicates that the required image files or sample files are missing, so please check the location of the default files and change the directory accordingly. If this does not work, reinstalling the application may help.
 * Moving around the executable bin file is not normally tolerated without manual directory change. However, creating a shortcut widget is tolerated without changing the working directory manually.
 * To save the manually set directories and inputs, please press the "save default settings" button.