import os, keyboard
from getpass import getpass
from colorama import init, Fore
from tkinter import filedialog, Tk
import time

init(autoreset=True)
root = Tk()
root.title('Choose Folder to Lock')
root.withdraw()
root.attributes('-topmost', True)

password = "9865032909"
def GetFolderName(info):
    folder = filedialog.askdirectory(title=info)
    return folder
while True:
    password_input = getpass(prompt="Enter Password: ")
    if password_input == password:
        if not os.path.exists('Locked'):
            if not os.path.exists("Locked.{645ff040-5081-101b-9f08-00aa002f954e}"):
                os.mkdir("Locked")
                print("{}Isolated Folder has been created under name Locked!".format(Fore.GREEN))
            else:
                os.popen("attrib -h 'Locked.{645ff040-5081-101b-9f08-00aa002f954e}'")
                os.popen('icacls "Locked.{645ff040-5081-101b-9f08-00aa002f954e}" /inheritance:d')
                os.popen('icacls "Locked.{645ff040-5081-101b-9f08-00aa002f954e}" /c /grant everyone:(f)')
                os.rename("Locked.{645ff040-5081-101b-9f08-00aa002f954e}", "Locked")
                os.system('cls')
                print("{}Success".format(Fore.GREEN))
        else:
            os.rename("Locked", "Locked.{645ff040-5081-101b-9f08-00aa002f954e}")
            os.popen("attrib +h Locked.{645ff040-5081-101b-9f08-00aa002f954e}")
            os.popen("icacls Locked.{645ff040-5081-101b-9f08-00aa002f954e} /inheritance:d")
            os.popen('icacls Locked.{645ff040-5081-101b-9f08-00aa002f954e} /c /remove everyone:(n)')
            print("{}Success".format(Fore.GREEN))
    else:
        print("{}Provided Password is InCorrect".format(Fore.RED))
        input("Press ENTER to Continue")
        os.system("cls")