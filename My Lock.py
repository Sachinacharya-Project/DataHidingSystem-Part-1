from getpass import getpass
from colorama import init, Fore
from tkinter import filedialog, Tk
import bcrypt, json, time, os

KEY_LOCATION = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'key_data.json')
ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))

init(autoreset=True)
root = Tk()
root.title('Choose Folder to Lock')
root.withdraw()
root.attributes('-topmost', True)

password = '0123456789'
def isPassword(password):
    with open(KEY_LOCATION, 'r') as file:
        data = str(json.load(file)['password']).encode('utf-8')
        if bcrypt.checkpw(str(password).encode('utf-8'), data):
            return True
        else:
            return False
def set_password(task='new'):
    "Create or Modify new password"
    while True:
        master_password = getpass("Master Password: ")
        password = getpass("Password: ")
        secrete_key = getpass("Secrete Key: ")
        if master_password != '' and password != '' and secrete_key != '':
            break
        else:
            print("None of the Passwords can be empty")
    master_ = bcrypt.hashpw(master_password.encode('utf-8'), bcrypt.gensalt())
    password_ = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    secrete_ = bcrypt.hashpw(secrete_key.encode('utf-8'), bcrypt.gensalt())
    if task == 'new':
        with open(KEY_LOCATION, 'w+') as file:
            data = {
                "master_key": master_.decode('utf-8'),
                "password": password_.decode('utf-8'),
                "secrete_key": secrete_.decode('utf-8')
            }
            json.dump(data, file, indent=4)
    else:
        with open(KEY_LOCATION, 'r+') as file:
            rawdata = json.load(file)
            old_master = rawdata['master_key']
            old_pass = rawdata['password']
            old_secret = rawdata['secrete_key']
            new_master = old_master if master_password == '' else master_
            new_password = old_pass if password == '' else password_
            new_secrete = old_secret if secrete_key == '' else secrete_
            data = {
                "master_key": str(new_master),
                "password": str(new_password),
                "secrete_key": str(new_secrete)
            }
            json.dump(data, file, indent=4)
def GetFolderName(info):
    folder = filedialog.askdirectory(title=info)
    return folder
while True:
    if os.path.exists(KEY_LOCATION):
        password_input = getpass(prompt="Enter Password: ")
        if isPassword(password_input):
            print("Press Enter to Continue! (C) to Change Password")
            opt = input("").lower()
            if opt == 'c':
                set_password('change')
            else:
                if not os.path.exists('Locked'):
                    if not os.path.exists("Locked.{645ff040-5081-101b-9f08-00aa002f954e}"):
                        os.mkdir("Locked")
                        print("{}Isolated Folder has been created under name Locked!".format(Fore.GREEN))
                    else:
                        os.popen('cacls Locked.{645ff040-5081-101b-9f08-00aa002f954e} /c /e /p everyone:f')
                        os.popen("attrib -h 'Locked.{645ff040-5081-101b-9f08-00aa002f954e}'")
                        time.sleep(2)
                        os.rename("Locked.{645ff040-5081-101b-9f08-00aa002f954e}", "Locked")
                        os.system('cls')
                        print("{}Success".format(Fore.GREEN))
                else:
                    os.rename("Locked", "Locked.{645ff040-5081-101b-9f08-00aa002f954e}")
                    os.popen("attrib +h Locked.{645ff040-5081-101b-9f08-00aa002f954e}")
                    os.popen('cacls Locked.{645ff040-5081-101b-9f08-00aa002f954e} /c /e /p everyone:n')
                    print("{}Success".format(Fore.GREEN))
        else:
            print("{}Provided Password is InCorrect".format(Fore.RED))
            input("Press ENTER to Continue")
            os.system("cls")
    else:
        print("Creating new Password database")
        print("One time setup")
        set_password("new")
        print("""Informations
        Please Make Sure to Add to PATH. Check Out Documentation to do so.
        """)
        print(ABSOLUTE_PATH)
        input("Press ENTER to Continue")
        os.system("cls")