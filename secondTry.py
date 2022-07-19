/import pandas as pd
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

def keyd(passJson2):
    with open(passJson2, "r") as read_file:
        data = json.load(read_file)
    df = pd.json_normalize(data)

    #open pass.jsom file DONE
    #open keys.csv file
    #open outputFile.csv file
    #read the value of organizationName in pass.json
    #find match for organizationName.value in first column of keys.csv
    ##new direction:
        #if organizationName == airlilne
            #for each col in row(orgName's row)
                #input (col,row).val into outputfile.csv @ lastRow in same col
            
        #save outputFile.csv
        #save outputFile.csv
        #close keys.csv
        ####### go to NEXT pkpass file @ unzipper() ::::: update unzipper() to accept multiple or single files

    #assign variables to each value in corresponding row
    #add those values to outputFIle.csv (this may be a seperate fuction, OR 
    #this could be greatly abbreviated by nesting the addition of data to the csv directly from the keys.csv
    #skip the step where variables get defined: for each row in col, add to csv @ new line (enumerate?, maybe go to list, then convert to csv? maybe easier to manage? research)

    #CONVERT json
    #json2csv(thisFile) - useless to this function

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

                        #HERE! 12:49 19-Jul-2022
                        #keyd(thisFile)
:                       
                        #json2csv(thisFile) - probably done with that? may just use later?

unzipper()