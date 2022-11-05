import classes as c
import pickle
import menus as m
from fileHandling import *

def main():
    # Checking if file exists, creating one if not
    if not checkFile():
        print('No file, creating file')
        createFile()

    accounts = loadAccounts()
    m.mainMenu(accounts)

def loadAccounts():
    def checkForAccount(file):
        # If pickle.load returns an error runs the except condition, otherwise returns account object
        try:
            accountObj = pickle.load(file)
            print("Account object found")
            return accountObj
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

    print('Accounts loaded:', accountObject)
    return accountObject

main()