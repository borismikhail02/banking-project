import os
import pickle

filePath = "banking-project/accountsFile.txt"

def createFile():
    # Creates new file if one doesnt exist already
    with open(filePath, "w") as f:
        f.write('')

def checkFile():
    # Booleon return value for if file exists
    fileCheck = os.path.isfile(filePath)
    if not fileCheck:
        print("File does not exist")
        return False
    print("File is already created")
    return True

def saveFile(accounts):
    with open(filePath, 'rb') as f:
        accounts = pickle.load(f)