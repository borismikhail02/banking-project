import os

def main():
    if not checkFile():
        print('No file, creating file')
        createFile()

    with open("banking-project/accountsFile.txt", "a") as f:
        print("File open")
        f.writelines('\n123')

def createFile():
    with open("banking-project/accountsFile.txt", "w") as f:
        f.write("Test")

def checkFile():
    path = "banking-project/accountsFile.txt"
    fileCheck = os.path.isfile(path)
    if not fileCheck:
        print("File does not exist")
        return False
    print("File is already created")
    return True


main()  