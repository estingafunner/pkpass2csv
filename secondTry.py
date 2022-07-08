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

    print(data)
    print(df)

def unzipper():
    # assign directory
    dir1 = 'pkpass'
    dir2 = 'passes'
    dir3 = 'unzipped'
    j = 0
    # iterate over files in
    # that directory
    for filename in os.listdir(dir1):
        f = os.path.join(dir1, filename)
        # checking if it is a file
        if os.path.isfile(f):
            print(f)
        
        with ZipFile(f, 'r') as zipObject:
            listOfFileNames = zipObject.namelist()
            for passName in listOfFileNames:
                if passName == "pass.json":
                    j += 1
                    # Extract a single file from zip
                    zipObject.extract(passName, dir3)
                    #os.rename(passName, (str(j) + passName))
                    shutil.move((dir3 + "/" + passName), (dir2 + "/" + str(j) + passName)) ##"path/to/current/file.foo", "path/to/new/destination/for/file.foo")
                    print('All the python files are extracted')



'''         with ZipFile(f, 'r') as zipObj:
        #Extract all the contents of zip file in different directory
            zipObj.extractall(dir3) 
            #print('File is unzipped in temp folder') 

            for i, passFile in enumerate(os.listdir(dir3)):
                g = os.path.join(dir3, passFile)
                if os.path.isfile(g) and passFile == "pass.json":
                    shutil.move(g, (dir2 + "/" + str(i) + passFile)) ##"path/to/current/file.foo", "path/to/new/destination/for/file.foo")
                    print("what?")
                    #os.remove(dir3 + "/" + passFile)
                elif os.path.isfile(g):
                    os.remove(g)
                
        #json2csv(thisFile) '''

unzipper()