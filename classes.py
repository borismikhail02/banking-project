class Accounts():
    def __init__(self, createBlank):
        if createBlank:
            self.accountsList = []

    def getAccounts(self):
        return self.accountsList

    def listAccounts(self):
        print('accounts list: ', self.accountsList)
        for item in self.accountsList:
            item.displayDetails()
        
    def clientSearch(self, type, search):
        if type == 'name' or type == 'dob':
            print("searching by", 'type')
            check = (client.type == search)
        elif type == 'negBalance':
            print("searching by neg balance")
            check = (client.balance > 0)
        else:
            print("Invalid search type")
        
        outputList = []
        for client in self.accountsList:
            if check:
                outputList.append(client)
    
    def addClient(self, clientDetails):
        newClient = ClientAccount(clientDetails)
        self.accountsList.append(newClient)


class ClientAccount():
    def __init__(self, clientDetails):
        self.fname = clientDetails['fname']
        self.lname = clientDetails['lname']
        self.fullName = self.fname, self.lname
        self.title = clientDetails['title']
        self.pronouns = clientDetails['pronouns']
        self.dob = clientDetails['dob']
        self.occupation = clientDetails['occupation']
        self.balance = 0
        self.overdraft = clientDetails['overdraft']

    def getName(self):
        return self.fullName
    
    def getDob(self):
        return self.dob

    def getBalance(self):
        return self.balance

    def changeBalance(self, amount):
        self.balance += amount

    def displayDetails(self):
        display = ('''
        Name: {0} {1}
        Balance: {2}
        Overdraft: {3}
        ''')
        print(display.format(self.fullName[0], self.fullName[1], self.balance, self.overdraft))

class Error(Exception):
    pass

class ValueRangeError(Error):
    pass

class TextValueError(Error):
    pass