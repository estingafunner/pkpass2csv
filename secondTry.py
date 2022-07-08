import pandas as pd
from zipfile import ZipFile
import json
import os
import shutil


def json2csv(passJson):
    with open(passJson, "r") as read_file:
        data = json.load(read_file)

    df = pd.json_normalize(data)
    df.to_csv(r'outputFile.csv', index = None)

    #print(data)
    print("wat?")

def unzipper():
    # assign directory
    dir1 = 'pkpass'
    dir2 = 'passes'
    dir3 = 'unzipped'
    j = 0

    for filename in os.listdir(dir1):
        f = os.path.join(dir1, filename)

        if os.path.isfile(f):

            with ZipFile(f, 'r') as zipObject:
                listOfFileNames = zipObject.namelist()

                for passName in listOfFileNames:

                    if passName == "pass.json":
                        j += 1
                        zipObject.extract(passName, dir3)
                        shutil.move((dir3 + "/" + passName), (dir2 + "/" + str(j) + passName)) 
                        thisFile = dir2 + "/" + str(j) + passName
                        json2csv(thisFile) 

unzipper()