import classes as c
from fileHandling import createFile, saveFile
from datetime import datetime, date

# Declaration of main application menu
def mainMenu(accounts):

    # Declarations of submenus within main menu
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

        if userInput == 'y' or userInput == 'Y':
            print('You have selected: Yes')
            print("Clearing entire file")
            createFile()
            return mainMenu()
        else:
            print('You have selected: No')
            print("Going back to main menu")
            return mainMenu()

    def addClientMenu():

        # Checks if input is all alphabetical characters and contains at least one character
        def textValidityCheck(inputText):
            if inputText.isalpha():
                return True
            return False

        # Checks if the input is an integer value
        def intValidityCheck(data, range):
            try:
                if (int(data) >= range[0] and int(data) <= range[1]):
                    return True
            except:
                return False

        def dateValidityCheck(inputData):
            pass

        # Selection menu for prefered title
        def titleMenu():
            titles = ['Mr','Mrs','Miss','Ms','Dr','Other']
            userInput = input('''Please select one of the following titles:
            1 - Mr
            2 - Mrs
            3 - Miss
            4 - Ms
            5 - Dr
            6 - Other\n''')
            # Loops an error until a valid input within range is given
            while not intValidityCheck(userInput, (1,6)):
                input('Input was not valid, please press emter to try again')
                return titleMenu()
            return titles[int(userInput)-1]

        # Selection menu for prefered pronouns
        def pronounsMenu():
            pronouns = ['He/Him','She/Her','They/Them','Other']
            userInput = input('''Please select one of the following prefered pronouns:
            1 - He/Him
            2 - She/Her
            3 - They/Them
            4 - Other\n''')
            # Loops an error until a valid input within range is given
            while not intValidityCheck(userInput, (1,4)):
                input('Input was not valid, please press emter to try again')
                return pronounsMenu()
            return pronouns[int(userInput)-1]

        # Input menu for taking the dob of the client and collating it with the datetime library
        def dobMenu():
            print('Please enter your date of birth, giving year then month then day')
            year = input("Please enter the year: ")
            # Loops an error until a valid input within range is given
            while not intValidityCheck(year, (date.today().year-150,date.today().year)):
                input('Input was not valid, please press emter to try again')
                return dobMenu()
            month = input("Please enter the month: ")
            # Loops an error until a valid input within range is given
            while not intValidityCheck(month, (1,12)):
                input('Input was not valid, please press emter to try again')
                return dobMenu()
            day = input("Please enter the day: ")
            # Loops an error until a valid input within range is given
            while not intValidityCheck(day, (1,31)):
                input('Input was not valid, please press emter to try again')
                return dobMenu()
            return date(int(year),int(month),int(day))

        # Input menu for the desired overdraft amount
        def overdraftMenu():
            overdraft = input("Please enter your desired overdraft (min £0, max £350):\n £")
            # Loops an error until a valid input within range is given
            while not intValidityCheck(overdraft, (0,350)):
                input('Input was not valid, please press emter to try again')
                return overdraftMenu()
            return overdraft

        def inputManager(data, check, location):
            if check == 'pass' or check(data):
                details[location] = data
                return True
            else:
                input('Input was not valid, please press emter to try again')
                return False

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

        print(details)
        accounts.addClient(details)

        input('Press enter to go back to main menu')
        return mainMenu(accounts)


    # Beginning of main menu
    print('''
        - - - - - - - - - -
           Bank Project
        - - - - - - - - - -''')
    print('''
    1 - List clients
    2 - Add client
    3 - Select client
        - Show
        - Edit
        - Delete
    4 - Clear all clients
    5 - Save and Exit''')

    # Validation checks for the user input
    try:
        # Raises ValueError if input type is not int
        userInput = int(input('Select a menu item by typing its number: '))
        # Raises custom ValueRangeError if input out of desired range
        if userInput > 5 or userInput <= 0:
            raise c.ValueRangeError
    # Handling differnet error types
    except ValueError:
        print('User input is not a recognisable value for this input')
        input('Please press enter to try again')
        return mainMenu()
    except c.ValueRangeError:
        print("Value inputed is out of range")
        input('Please press enter to try again')
        return mainMenu()
    except:
        print('Unknown error')
        input('Please press enter to try again')
        return mainMenu()
    
    # Once input has passed all validation it triggers next function(s)
    if userInput == 5:
        saveFile(accounts)
        exit()
    elif userInput == 4:
        print('Clearing all clients selected')
        clearClientsMenu()
    elif userInput == 3:
        print('Selecting client selected')
    elif userInput == 2:
        print('Add client selected')
        addClientMenu()
    elif userInput == 1:
        print('List all clients selected')
        listClients(accounts)

def listClients(accounts):
    accounts.listAccounts()
    
    input('Press enter to go back to main menu')
    return mainMenu(accounts)