from decimal import Decimal

class Accounts():
    # Class constructor
    def __init__(self, createBlank):
        if createBlank:
            self.accountsList = []


    # Getters used to return values of properties
    def getAccounts(self):
        return self.accountsList

    def getClientName(client):
        return client.getName()


    # Setter methods used to change private properties
    def clearAccounts(self):
        self.accountsList = []


    # Display methods
    def listAccounts(self):
        if len(self.accountsList) == 0:
            print('No accounts found')
        for i in range(len(self.accountsList)):
            print('Account number:', i+1)
            self.accountsList[i].displayFull()
    

    # Account list editor methods
    def addClient(self, clientDetails):
        newClient = ClientAccount(clientDetails)
        self.accountsList.append(newClient)
    
    def replaceClient(self, client, newDetails):
        newClient = ClientAccount(newDetails)
        self.accountsList[self.accountsList.index(client)] = newClient

    def deleteClient(self, client):
        self.accountsList.remove(client)


    # Search methods
    def clientSearch(self, type, search):
        outputList = []
        for client in self.accountsList:
            check = False
            isNegBal = False
            if type == 'name':
                check = ' '.join(str(e) for e in client.getFullName())
            elif type == 'dob':
                check = str(client.getDob())
            elif type == 'negBal':
                isNegBal = (client.getBalance() < 0)
            if check == search or isNegBal:
                outputList.append(client)
        return outputList


class ClientAccount():
    # Class constructor
    def __init__(self, clientDetails):
        self.__fname = clientDetails['fname']
        self.__lname = clientDetails['lname']
        self.__fullName = self.__fname, self.__lname
        self.__title = clientDetails['title']
        self.__pronouns = clientDetails['pronouns']
        self.__dob = clientDetails['dob']
        self.__occupation = clientDetails['occupation']
        self.__balance = Decimal(0)
        self.__overdraft = clientDetails['overdraft']


    # Display functions using getters defined bellow
    def displaySummary(self, index):
        display = ('''Account {0}:
        Name:               {1} {2}
        Date of birth:      {3}
        Occupation:         {4}
        ''').format(index, self.getFirstName(), self.getLastName(), self.getDob(), self.getOccupation())
        print(display)

    def displayFull(self):
        display = ('''Client Details:
        First name:         {0}
        Last name:          {1}
        Title:              {2}
        Pronouns:           {3}
        Date of birth:      {4}
        Occupation:         {5}
        Balance:            {6}
        Overdraft:          {7}
        ''').format(self.getFirstName(), self.getLastName(), self.getTitle(), self.getPronouns(), self.getDob(), self.getOccupation(), self.getBalance(), self.getOverdraft())
        print(display)


    # Getter methods to return private properties
    def getFullName(self):
        return self.__fullName
    
    def getFirstName(self):
        return self.__fname
        
    def getLastName(self):
        return self.__lname
    
    def getTitle(self):
        return self.__title

    def getPronouns(self):
        return self.__pronouns

    def getDob(self):
        return self.__dob

    def getOccupation(self):
        return self.__occupation

    def getBalance(self):
        return self.__balance

    def getOverdraft(self):
        return self.__overdraft

    
    # Setter methods used to change private properties
    def setBalance(self, value):
        self.__balance += value


    # Editor methods to change private properties using setters
    def editBalance(self, amount):
        self.setBalance(Decimal(amount))
        if self.getBalance() < (0-int(self.getOverdraft())):
            print('You have gone over your overdraft, an aditional £5 was charged')
            self.setBalance(-5)


# Custom exception declarations
class Error(Exception):
    pass

class ValueRangeError(Error):
    pass

class TextValueError(Error):
    pass