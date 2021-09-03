# Speedrun to write a good todo app.
from colorama import Fore,Style
from colorama import init
import time,os
init()

clsCommand = ""
file = "./todo.txt"
def clearTodo():
    with open(file,'w') as f:
        f.write('')
    



def markTodo(line):
    with open(file,'r') as f:
        f = f.readlines()
        todos = [x.strip() for x in f]
    if todos[line].startswith('####'):
        print(Fore.CYAN+'Already Marked Done !'+Fore.RESET)
        time.sleep(3)
        os.system(clsCommand)
        return False

    if todos[line].startswith('(((('):
        print(Fore.CYAN+"This is a Reminder ! You can't Mark it done !"+Fore.RESET)
        time.sleep(3)
        os.system(clsCommand)
        
        return False
    else:
        todos[line] = "####"+todos[line][4:]


    with open(file,'w') as f:
        f.write('')

    with open(file,'a') as f:
        for todo in todos:
            f.write(todo+"\n")

    print(Fore.GREEN+'Done !'+Fore.RESET)
    time.sleep(3)
    os.system(clsCommand)
 
def addTodo():
    """ 
    1 = %%%% 2- ^^^^ 3- &&&& 4- @@@@ , #### = Done """
    print("Which One ?")
    choice = input("1- Todo 2- Reminder 3- Exit > ")

    if choice == '1':
        pass
    
    elif choice == '3':
        return False
    else:
        addReminder()
        return False     
    print("How much important ? ")
    choice = input("1- Very Important 2- Important 3- Not So Important 4- Not Important 5- Exit > ")
    meta = ""
    if choice == "1":
        meta = "%%%%"

    elif choice == "2":
        meta = "^^^^"

    elif choice == "3":
        meta = "&&&&"
    
    elif choice == "4":
        meta = "@@@@"
    else:
        return False
    todo = input('Todo ? > ')

    with open(file,'a') as f:
        f.write(f'{meta}{todo}\n')

    print(Fore.GREEN+'Done !'+Fore.RESET)
    time.sleep(3)
    os.system(clsCommand)
def addReminder():
    """  Adds Reminder
    reminder = ((((  ."""

    reminder = input("Reminder ? [Enter 0 to exit] > ")
    if reminder == "0":
        return False

    else:
        pass
    with open(file,'a') as f:
        f.write(f"(((({reminder}")

    print(Fore.GREEN+'Done !'+Fore.RESET)
    time.sleep(3)
    os.system(clsCommand)
 

def seedata():
    with open(file,'r') as f:
        f = f.readlines()
        if len(f) < 1:
            print(Fore.MAGENTA+'No TODO !')
            print(Fore.RESET)
            return None
        todos = [x.strip() for x in f]
    number = 1
    print('Line Number          State                         TODO/Reminder'.center(50))
    for todo in todos:
        if todo.startswith('%%%%'):
            print(Fore.LIGHTMAGENTA_EX+str(number)+Fore.RED+Style.BRIGHT+'    VERY IMPORTANT'.center(50)+todo[4:]+Fore.RESET+Style.RESET_ALL)
            number += 1
        elif todo.startswith('^^^^'):
            print(Fore.LIGHTMAGENTA_EX+str(number)+Fore.LIGHTRED_EX+Style.DIM+'IMPORTANT'.center(50)+todo[4:]+Fore.RESET+Style.RESET_ALL)
            number += 1
        elif todo.startswith('&&&&'):
            print(Fore.LIGHTMAGENTA_EX+str(number)+Fore.LIGHTYELLOW_EX+'      Not So Important'.center(50)+todo[4:]+Fore.RESET)
            number += 1
        elif todo.startswith('@@@@'):
            print(Fore.LIGHTMAGENTA_EX+str(number)+Fore.LIGHTGREEN_EX+'   Not Important'.center(50)+todo[4:]+Fore.RESET)
            number += 1

        elif todo.startswith('(((('):
            print(Fore.LIGHTMAGENTA_EX+str(number)+Fore.CYAN+'Reminder '.center(50)+todo[4:]+Fore.RESET)

            number += 1

        elif todo.startswith('####'): 
            print(Fore.LIGHTMAGENTA_EX+str(number)+Fore.LIGHTCYAN_EX+'Done !    '.center(50)+todo[4:]+Fore.RESET)
            number += 1
        else:
            pass

    print(Fore.RESET)


def main():
    global clsCommand
    Done = False
    clsCommand = "cls" if os.name == 'nt' else "clear"
    if os.path.isfile("todo.txt"):
        pass
    else:
        print(Fore.RED+"Todo File Not Found ! Creating Todo File."+Fore.RESET)
        with open("todo.txt","w") as f:
            f.write("")
        time.sleep(3)
        os.system(clsCommand)
    while not Done:
        print(Fore.GREEN+"Hello ! , I hope you're doing well.")
        print(Style.RESET_ALL)
        print('Your current Data list : ')
        seedata()
        print(r"1- Mark a todo 2-Add a TODO/Reminder 3- Clear Todo 4- Exit")

        choice = input("> ")
        if choice == "1":
            line = input('Line number ? > ')
            print('\n')
            markTodo(int(line)-1)
            continue
        elif choice == "2":
            addTodo()
            continue
        elif choice == "3":
            clearTodo()
            continue
        elif choice == "4":
            Done = True

        else:
            print(Fore.RED+"Wrong Choice !!")
            print(Style.RESET_ALL)
            time.sleep(3)
            os.system(clsCommand)
    else:
        SystemExit
main()
