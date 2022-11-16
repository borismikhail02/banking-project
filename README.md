# banking-project

Overview and how to run:
------------------------
This is a terminal based program operated by menus and user inputs. To run the program simply open the 'run.py' file in the 'banking-project' folder. This should open a terminal window from where you can access the menus and use the program.

Once the accounts object is loaded from 'accountsList.txt' or a new one is created if one is not found, the 'main.py' file will run the main menu. From here the entire program is designed to be used through a series of terminal menus and user inputs. Each user input is validated using the validation functions (found at the top of the def for 'mainMenu()' in 'main.py') relevant for the type of input, and exceptions are handled by displaying a simple error message and restarting the appropriate menu/input field. All of the basic functionality required by the specification is implimented through theses menus and can be navigated to and used by the user, requiring no further commands. 

No changes made in the runtime of the application will be saved unless the "Save and Exit" option is seletected from the main menu, which will save the edided accounts object to the file and close the program.

Notes:
- Data validation is all done within the user interface, and only valid data is sent to class methods. This is to avoid unnexpected errors within the classes and possible data corruption.


Assumptions made in building:
-----------------------------
Most assumptions made in this project are in the user inputs and their validation, explanations of expected inputs for every case follow:

- Navigation in numbered menus
    Any integer from 1 to the last option displayed in the menu, i.e. menu with 4 options will accept integers 1, 2, 3 and 4.

- Entering first name when creating account
- Entering last name when creating account
- Entering occupation when creating account
    Only letters of the alphabet, no symbols, no spaces, no numbers

- Entering year of birth when creating account
    Any year from current year to 150 years in the past (updates with time)

- Entering month of birth when creating account
    Any integer from 1 to 12

- Entering day of birth when creating account
    Any integer from 1 to 31

- Entering overdraft when creating account
    Any integer from 0 to 350

- Searching by full name
    Accepts any input, but exact match of client first name and last name required to find a match. i.e. if fname='John' and lname='Doe' the required search will be 'John Doe' (space is required)

- Searching by date of birth
    Exact date in the form YYYY/MM/DD, symbols splitting the numbers can be any mix of the following:
    - ','
    - '.'
    - '/'
    - '-'
    Date must match exactly to find a match, 0's are required i.e. if the month is 6th input must be '06'

- Depositing and withdrawing from balance
    Any decimal greater than 0 and with no more than 2 decimal places, integers are accepted also

- Deleting client account and clearing all clients menus
    Accept the following string values: 'y', 'Y', 'n', 'N'


Use case example of running program:
------------------------------------
The following exmple will walk you through how to do the following: delete all current accounts; create a new client account under the name "John Doe" and with an overdraft of 50; create a second account named "John Doe" but a different date of birth; search for accounts by the name "John Doe" and select the latter account created; deposit 100 to that accounts balance; search for accounts by date of birth and selecting the first "John Doe"; withdrawing 60 from their balance; list all client accounts and their details; if all goes as planned the balance shown on the first John Doe should be -65 (as this client has gone over their overdraft) and the balance on the second John Doe should be 100.

Step 1: Open cmd in the project folder and run the following command: banking-project\run.py

Step 2: The main menu will display in terminal, type '4' and press enter to select 'Clear all clients'

Step 3: You will be asked if you are sure you want to delete all current clients, type 'y' or 'Y' and press enter

Step 4: Type '2' and press enter to select 'Add client'

Step 5: Type 'John' and press enter, then type 'Doe' and press enter, this will set your name to John Doe

Step 6: Type '1' and press enter, then type '1' again and press enter to select the title of Mr and pronouns of He/Him

Step 7: Type '1999' and press enter, then type '13' and press enter. This should return an error of "Input was not valid, please press enter to try again". This is expected as there are only 12 months in the year

Step 8: You will need to re-enter the date of birth starting from year, press enter to exit the error message

Step 9: Type '1999' and press enter, then type '12' and press enter, then type '1' and press enter, this will save 1999-12-01 as the inputed date of birth

Step 10: Type 'Manager' and press enter, then type '50' and press enter. This will set the clients overdraft to £50

Step 11: A summary of the client you just created will be displayed, press enter to return to main menu

Step 12: Repeat steps 4 to 11 but with the following sample date (ignore quotaion marks):
    First name: 'John'
    Last name: 'Doe'
    Title: Other (select option 6)
    Pronouns: They/Them (select option 3)
    Date of birth: 2000-01-01 (ensure these are entered in the correct order)
    Occupation: 'None'
    Overdraft: '100'

Step 13: Now that two accounts have been created we can search/select between them, in the main menu type '3' and press enter to select 'Select client'

Step 14: Type '1' and press enter to search by full name, then type 'John Doe' exactly (this is case sensetive and blank space sensetive) and press enter

Step 15: Two accounts will be shown, type '2' and press enter to select the latter account, then type '3' and press enter to select 'Deposit/Withdraw'

Step 16: Type '1' and press enter, then type '100' and press enter to deposit £100 to the selected client

Step 17: Type '3' and press enter, then type '2' and press enter to select 'Search by date of birth'

Step 18: Type '1999/12/01' (the zero in the '01' is important to the validation) and press enter

Step 19: Type '3' and press enter, then type '2' and press enter, then type '60' and press enter. This will withdraw £60 from the clients account. As this is over his overdraft an aditional £5 will be withdrawn ontop of this

Step 20: Type '1' and press enter. A list of all client accounts and their details will be displayed. The expected outcome will be a balance of -65 on Account number 1 and a balance of 100 on Account number 2. Whenever ready press enter to return to main menu

(Optional) Step 21: Type '5' and press enter, to select 'Save and Exit' and write all the changes done to the file. The program will then close.