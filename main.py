from fileHandling import saveFile
import classes as c
from datetime import date
import re
from decimal import Decimal
        
# Declaration of main application menu
def mainMenu(accounts):
    # Checks if input is only alphabetical characters and contains at least one character
    def textValidityCheck(inputText):
        if inputText.isalpha():
            return True
        return False

    # Checks if the input is an integer value within given range
    def intValidityCheck(data, range):
        try:
            if (int(data) >= range[0] and int(data) <= range[1]):
                return True
        except:
            return False

    # Checks if input is in the expected date format YYYY/MM/DD and splits input string into array containing year, month, day
    def dateValidityCheck(date):
        splitData = re.split('\/|\.|\-|,', date)
        try:
            if int(splitData[0]) and int(splitData[1]) and int(splitData[2]):
                pass
            if len(splitData) != 3 or len(splitData[0]) != 4 or len(splitData[1]) != 2 or len(splitData[2]) != 2:
                print('Incorrect date entry, please ensure its in the format YYYY/MM/DD exactly')
                return False
        except:
            return False
        searchDate = ("{0}-{1}-{2}").format(splitData[0],splitData[1],splitData[2])
        return(searchDate)

    # Checks if decimal is equal to 0 and if checks how many decimal points are given, if more than 2 returns false
    def decimalValidityCheck(amount):
            try:
                if Decimal(amount) != 0:
                    splitDecimal = str(amount).split('.')
                    print(splitDecimal, len(splitDecimal))
                    if len(splitDecimal) > 1:
                        print(len(splitDecimal[1]))
                        if not len(splitDecimal[1]) > 2:
                            return True
                        else:
                            print('Incorrect amount entry, please specify up to a max of 2 decimal places')
                    else:
                        return True
            except:
                return False
            

    # Sub-menu for clearing clients
    def clearClientsMenu():
        # Validation checks for the user input
        try:
            userInput = input("Are you sure you want to delete all client accounts? (y/n)\n")
            # Raises custom TextValueError if input is not y,Y,n or N
            if not ((userInput == 'y') or (userInput == 'Y') or (userInput == 'n') or (userInput == 'N')):
                raise c.TextValueError
        # Handling differnet error types
        except ValueError:
            print('User input is not a recognisable value for this input')
            input('Please press enter to try again')
            return clearClientsMenu()
        except c.TextValueError:
            print('Value inputed is not valid')
            input('Please press enter to try again')
            return clearClientsMenu()
        except:
            print('Unknown error')
            input('Please press enter to try again')
            return clearClientsMenu()

        # Handling valid user inputs
        if userInput == 'y' or userInput == 'Y':
            print('You have selected: Yes')
            print("Clearing entire file")
            accounts.clearAccounts()
            return mainMenu(accounts)
        else:
            print('You have selected: No')
            print("Going back to main menu")
            return mainMenu(accounts)
        
    # Sub-menu for selection for adding a new account (also used for editing accounts if editAccount=True)
    def addClientMenu(editAccount=False):
        
        # Checks validity of the data parsed, adds data to details dictionary if passed
        def inputManager(data, check, location):
            if check == 'pass' or check(data):
                details[location] = data
                return True
            else:
                input('Input was not valid, please press enter to try again')
                return False
        
        # Sub-menu for selecting title
        def titleMenu():
            titles = ['Mr','Mrs','Miss','Ms','Dr','Other']
            userInput = input('''Please select one of the following titles:
            1 - Mr
            2 - Mrs
            3 - Miss
            4 - Ms
            5 - Dr
            6 - Other
            ''')
            # Loops an error until a valid input within range is given
            while not intValidityCheck(userInput, (1,6)):
                input('Input was not valid, please press enter to try again')
                return titleMenu()
            return titles[int(userInput)-1]

        # Sub-menu for selecting prefered pronouns
        def pronounsMenu():
            pronouns = ['He/Him','She/Her','They/Them','Other']
            userInput = input('''Please select one of the following prefered pronouns:
            1 - He/Him
            2 - She/Her
            3 - They/Them
            4 - Other\n''')
            # Loops an error until a valid input within range is given
            while not intValidityCheck(userInput, (1,4)):
                input('Input was not valid, please press enter to try again')
                return pronounsMenu()
            return pronouns[int(userInput)-1]

        # Sub-menu for inputing dob and collating it using the datetime library
        def dobMenu():
            print('Please enter your date of birth, giving year then month then day')
            year = input("Please enter the year: ")
            # Loops an error until a valid input within range is given
            while not intValidityCheck(year, (date.today().year-150,date.today().year)):
                input('Input was not valid, please press enter to try again')
                return dobMenu()
            month = input("Please enter the month: ")
            # Loops an error until a valid input within range is given
            while not intValidityCheck(month, (1,12)):
                input('Input was not valid, please press enter to try again')
                return dobMenu()
            day = input("Please enter the day: ")
            # Loops an error until a valid input within range is given
            while not intValidityCheck(day, (1,31)):
                input('Input was not valid, please press enter to try again')
                return dobMenu()
            return date(int(year),int(month),int(day))

        # Sub-menu for inputing overdraft amount
        def overdraftMenu():
            overdraft = input("Please enter your desired overdraft (min £0, max £350):\n £")
            # Loops an error until a valid input within range is given
            while not intValidityCheck(overdraft, (0,350)):
                input('Input was not valid, please press enter to try again')
                return overdraftMenu()
            return overdraft

        # Taking inputs for all of the details required to create a client object, validates each input before adding to dictionary
        details = {}
        fname = input("Please enter your first name:\n")
        while not inputManager(fname, textValidityCheck, 'fname'):
            fname = input("Please enter your first name:\n")
        lname = input("Please enter your last name:\n")
        while not inputManager(lname, textValidityCheck, 'lname'):
            lname = input("Please enter your last name:\n")
        title = titleMenu()
        print('You selected the title:', title)
        inputManager(title, 'pass', 'title')
        pronouns = pronounsMenu()
        print('You selected the pronouns:', pronouns)
        inputManager(pronouns, 'pass', 'pronouns')
        dob = dobMenu()
        print('You selected the date of birth:', dob)
        inputManager(dob, 'pass', 'dob')
        occupation = input("Please enter your occupation:\n")
        while not inputManager(occupation, textValidityCheck, 'occupation'):
            occupation = input("Please enter your occupation:\n")
        overdraft = overdraftMenu()
        print('You selected an overdraft amount of:', overdraft)
        inputManager(overdraft, 'pass', 'overdraft')

        # Returning out of account creation if account is only being edited
        if editAccount:
            return details

        accounts.addClient(details)
        print('The following account has been created: ')
        print(details)

        input('Press enter to go back to main menu')
        return mainMenu(accounts)

    # Sub-menu for selecting client
    def selectClientMenu():
        userInput = input('''How would you like to search for accounts:
        1 - Search by full name
        2 - Search by date of birth
        3 - Search for negative balances
        4 - Return to main menu
        ''')
        # Loops an error until a valid input within range is given
        while not intValidityCheck(userInput, (1,4)):
            input('Input was not valid, please press enter to try again')
            return selectClientMenu()
        # Handing valid user inputs
        if userInput == '1':
            print("You have selected: Search by full name")
            search = input("Please type the full name as seen in account details:\n")
            results = accounts.clientSearch('name', search)
        elif userInput == '2':
            print("You have selected: Search by date of birth")
            search = input("Please type the full date of birth in the format YYYY/MM/DD:\n")
            while not dateValidityCheck(search):
                input('Input was not valid, please press enter to try again')
                return selectClientMenu()
            results = accounts.clientSearch('dob', dateValidityCheck(search))
        elif userInput == '3':
            print("You have selected: Search for negative balances")
            results = accounts.clientSearch('negBal', search=None)
        elif userInput == '4':
            print('You have selected: Return to main menu')
            return mainMenu(accounts)

        selectResultsMenu(results)

        mainMenu(accounts)

    # Sub-menu for selecting between multipile matches of a client search, if there are no matches returns error or if only one match clientMenu is called immediatly
    def selectResultsMenu(results):
        if len(results) == 0:
            print('No results found')
            return selectClientMenu()
        elif len(results) == 1:
            clientMenu(results[0])
        else:
            print('There are more than one account matching your search criteria, please select one:')
            for i in range(len(results)):
                results[i].displaySummary(i+1)
            userInput = input("Please type the number of the correct account\n")
            # Loops an error until a valid input within range is given
            while not intValidityCheck(userInput, (1, len(results))):
                input('Input was not valid, please press enter to try again')
                return selectResultsMenu(results)
            clientMenu(results[int(userInput)-1])

    # Sub-menu for confirming deletion of a client
    def deleteClientMenu(clientAccount):
        userInput = input("Are you sure you want to delete this client account? (y/n)")
        # Loops an error until a valid input is given
        while userInput != 'y' and userInput != 'n' and userInput != 'Y' and userInput != 'N':
            input('Input was not valid, please press enter to try again')
            return deleteClientMenu(clientAccount)
        # Handling valid user inputs
        if userInput == 'y' or userInput == 'Y':
            print('Deleting client')
            accounts.deleteClient(clientAccount)
        elif userInput == 'n' or userInput == 'N':
            print('Returning to main menu')
        mainMenu(accounts)

    # Sub-menu for editing a client's details. Calls addClientMenu to collate inputs then replaces current account object with a new object
    def editClient(clientAccount):
        details = addClientMenu(editAccount=True)
        accounts.replaceClient(clientAccount, details)
        print("Account details replaced")
        input("Press enter to return to main menu")
        mainMenu(accounts)

    # Sub-menu for editing client account balance
    def editBalanceMenu(clientAccount):
        userInput = input('''Would you like to deposit money or withdraw:
        1 - Deposit
        2 - Widthdraw
        ''')
        # Loops an error until a valid input within range is given
        print(intValidityCheck(userInput, (1,2)))
        while not intValidityCheck(userInput, (1,2)):
            input('Input was not valid, please press enter to try again')
            return editBalanceMenu(clientAccount)
        # Handling valid user inputs
        if userInput == '1':
            amount = input("How much would you like to deposit?\n£")
        elif userInput == '2':
            amount = input("How much would you like to widthraw?\n£")
        # Loops an error until a valid (max 2 decimal input is given)
        while not decimalValidityCheck(amount):
            input('Input was not valid, please press enter to try again')
            return editBalanceMenu(clientAccount)
        # If withdrawing money amount is set to negative itself
        if userInput == '2':
            amount = 0 - Decimal(amount)
        clientAccount.editBalance(amount)

    # Sub-menu for selecting what to do with selected client account
    def clientMenu(clientAccount):
        display = ("{0} {1}'s account selected").format(clientAccount.getFirstName(), clientAccount.getLastName())
        print(display)
        userInput = input('''
        1 - Show account details
        2 - Edit account details
        3 - Deposit/Withdraw
        4 - Delete account
        5 - Back to main menu
        ''')

        # Loops an error until a valid input within range is given
        while not intValidityCheck(userInput, (1,5)):
            input('Input was not valid, please press enter to try again')
            return clientMenu(clientAccount)
        # Handling valid user inputs
        if userInput == '1':
            clientAccount.displayFull()
            input("Press enter to return to client menu")
            clientMenu(clientAccount)
        elif userInput == '2':
            editClient(clientAccount)
        elif userInput == '3':
            editBalanceMenu(clientAccount)
        elif userInput == '4':
            deleteClientMenu(clientAccount)
        elif userInput == '5':
            return mainMenu(accounts)

    # Calls the listAccounts method of accounts object
    def listClients(accounts):
        accounts.listAccounts()
        input('Press enter to go back to main menu')
        return mainMenu(accounts)

    # Displaying main menu
    print('''
        - - - - - - - - - -
           Bank Project
        - - - - - - - - - -''')
    userInput = input('''
    1 - List clients
    2 - Add client
    3 - Select client
        - Show details
        - Edit details
        - Depsit/Withdraw
        - Delete
    4 - Clear all clients
    5 - Save and Exit
    ''')
    # Loops an error until a valid input within range is given
    while not intValidityCheck(userInput, (1,5)):
        input('Input was not valid, please press enter to try again')
        return mainMenu(accounts)
    # Handling valid user inputs
    if userInput == '5':
        saveFile(accounts)
        exit()
    elif userInput == '4':
        print('Clearing all clients selected')
        clearClientsMenu()
    elif userInput == '3':
        print('Selecting client selected')
        selectClientMenu()
    elif userInput == '2':
        print('Add client selected')
        addClientMenu()
    elif userInput == '1':
        print('List all clients selected')
        listClients(accounts)