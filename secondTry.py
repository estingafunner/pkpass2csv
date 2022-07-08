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
 
    # iterate over files in
    # that directory
    for filename in os.listdir(dir1:
        f = os.path.join(dir1, filename)
        # checking if it is a file
        if os.path.isfile(f):
            print(f)
        with ZipFile(f, 'r') as zipObj:
        #Extract all the contents of zip file in different directory
            zipObj.extractall('unzipped') 
            #print('File is unzipped in temp folder') 
            

            #shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")

        #json2csv(thisFile)

unzipper()