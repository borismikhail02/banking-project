import os
import pickle

filePath = "banking-project/accountsFile.txt"

# Creates new file if one doesnt exist already
def createFile():
    with open(filePath, "w") as f:
        f.write('')

# Returns booleon value whether file exists
def checkFile():
    fileCheck = os.path.isfile(filePath)
    if not fileCheck:
        print("File does not exist")
        return False
    print("File is already created")
    return True

# Saves account object in the file
def saveFile(accounts):
    with open(filePath, 'wb') as f: 
        pickle.dump(accounts, f, pickle.HIGHEST_PROTOCOL)
    print("File successfully saved")