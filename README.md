# banking-project

Overview and how to run:
This is a terminal based program operated by menus and user inputs. To run the program it is recommended you open a terminal in the project folder and run the command 'banking-project\run.py' (ignore quotation marks). If you run the program directly from the run.py file you'll need to change the 'filePath' variable in 'fileHandling.py' accordingly so that the rest of the program can locate the 'accountsFile.txt'.

Once the accounts object is loaded from 'accountsList.txt' or a new one is created if one is not found, the 'main.py' file will run the main menu. From here the entire program is designed to be used through a series of terminal menus and user inputs. Each user input is validated using the validation functions (found at the top of the def for 'mainMenu()' in 'main.py') relevant for the type of input, and exceptions are handled by displaying a simple error message and restarting the appropriate menu/input field. All of the basic functionality required by the specification is implimented through theses menus and can be navigated to and used by the user, requiring no further commands.

