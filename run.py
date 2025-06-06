import classes as c
import main as m
from fileHandling import *
import pickle

# Checking if file exists, creating one if not. Then loading accounts object from file and running main menu
def run():
    if not checkFile():
        print('No file, creating file')
        createFile()
    accounts = loadAccounts()
    m.mainMenu(accounts)

# Returns the accounts object after loading it from file
def loadAccounts(): 
    # Extra validation to avoid possible data problems, if pickle.load returns an error runs the except condition, otherwise returns account object
    def checkForAccount(file):
        try:
            accountObject = pickle.load(file)
            print("Account object found")
            return accountObject
        except:
            print('No object loaded on that file')
            return False
     
    # Creates a new object to load into file if none are found
    def createFileObject():
        accounts = c.Accounts(True)
        print('Creating new accounts object')
        with open(filePath, 'wb') as f: 
            pickle.dump(accounts, f, pickle.HIGHEST_PROTOCOL)

    # Opens the accounts file if one exists, otherwise creates new one then opens
    with open(filePath, "rb") as f:
        accountObject = checkForAccount(f)
        if not accountObject:
            createFileObject()
            accountObject = checkForAccount(f)
            
    return accountObject

run()