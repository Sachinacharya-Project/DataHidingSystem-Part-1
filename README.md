# DataHidingSystem-Part-1
This piece project has ability to hide and secure some of your datas
## Features
1. Can Hide your data (Can be view by (View -> UnCheck Hidden Item) on Explorer Menu) but will be inaccessible.
2. Even though the person managed to make the datas accessible, he won't have any permissions to read or write the files (access control list (ACL))
3. Easily managable
4. Every function included in the Script can be done using command-line functionality of Windows (Command Prompt, Powershell)
5. Pseudo Password Protection (&times;)
6. Hashed password Protection
## How to use?
1. Run Command
````python
python main.py # For Unix python3
````
2. Enter Password will be prompt, do as it says
3. Folder with name "Locked" will be created in the current directory
4. Copy all your secret datas to the very folder
5. Type password again
6. And you are done! Your data is successfully hidden
7. To View/Access your data Enter password again and you have your data
8. Enter Password again, Data Hidden and so on

## Setting Password
Change the Script main.py
Search for variable password (Change it with your password)
