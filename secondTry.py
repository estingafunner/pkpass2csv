#import pandas as pd
from zipfile import ZipFile
import json
import os
import shutil
import tkinter as tk
import tkinter.filedialog as fdi


def json2csv(passJson):
    with open(passJson, "r") as read_file:
        data = json.load(read_file)

    df = pd.json_normalize(data)
    df.to_csv(r'outputFile.csv', index = None)

    #print(data)
    print("wat?")

def unzipper():
    # assign directory

    root = tk.Tk()
    filez = fdi.askopenfilenames(parent=root, title='Choose a file')
    print(filez)

    """     Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    fn = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(fn) """

    #dir1 = 'pkpass' - replaced with user prompt
    dir2 = 'passes'
    dir3 = 'unzipped'
    j = 0

    for filename in filez:
        #f = os.path.join(dir1, filename)

        if os.path.isfile(filename):

            with ZipFile(filename, 'r') as zipObject:
                listOfFileNames = zipObject.namelist()

                for passName in listOfFileNames:

                    if passName == "pass.json":
                        j += 1
                        zipObject.extract(passName, dir3)
                        shutil.move((dir3 + "/" + passName), (dir2 + "/" + str(j) + passName)) 
                        thisFile = dir2 + "/" + str(j) + passName
                        #json2csv(thisFile) 

unzipper()