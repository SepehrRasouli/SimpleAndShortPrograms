# Speedrun to write a good todo app.
from colorama import Fore,Style
from colorama import init
init()


file = "todo.txt"
def clearTodo():
    with open(file,'w') as f:
        f.write('')
    main()

def markTodo(line):
    with open(file,'r') as f:
        f = f.readlines()
        todos = [x.strip() for x in f]
    if todos[line].startswith('####'):
        print(Fore.CYAN+'Already Marked Done !'+Fore.RESET+"\n\n\n\n\n")
        return False

    if todos[line].startswith('(((('):
        print(Fore.CYAN+"This is a Reminder ! You can't Mark it done !"+Fore.RESET+"\n\n\n\n\n")
    else:
        todos[line] = "####"+todos[line][4:]


    with open(file,'w') as f:
        f.write('')

    with open(file,'a') as f:
        for todo in todos:
            f.write(todo+"\n")

    print(Fore.GREEN+'Done !'+Fore.RESET+"\n\n\n\n\n")

def addTodo():
    """ 
    1 = %%%% 2- ^^^^ 3- &&&& 4- @@@@ , #### = Done """
    print("Which One ?")
    choice = input("1- Todo 2- Reminder > ")

    if choice == '1':
        pass

    else:
        addReminder()
    
    print("How much important ? ")
    choice = input("1- Very Important 2- Important 3- Ehh... 4- Fun ha ? > ")
    meta = ""
    if choice == "1":
        meta = "%%%%"

    elif choice == "2":
        meta = "^^^^"

    elif choice == "3":
        meta = "&&&&"

    else:
        meta = "@@@@"

    todo = input('Todo ? > ')

    with open(file,'a') as f:
        f.write(f'{meta}{todo}\n')

    print(Fore.GREEN+'Done !'+Fore.RESET+"\n\n\n\n\n")
    main()


def addReminder():
    """  Adds Reminder
    reminder = ((((  ."""

    reminder = input("Reminder ? > ")
    with open(file,'a') as f:
        f.write(f"(((({reminder}")

    print(Fore.GREEN+'Done !'+Fore.RESET+"\n\n\n\n\n")
    main()

def seedata():
    with open(file,'r') as f:
        f = f.readlines()
        if len(f) < 1:
            print(Fore.MAGENTA+'No TODO !')
            print(Fore.RESET)
            return None
        todos = [x.strip() for x in f]
    number = 1
    print('Line Number         State                          TODO'.center(50))
    for todo in todos:
        if todo.startswith('%%%%'):
            print(Fore.LIGHTMAGENTA_EX+str(number)+Fore.RED+Style.BRIGHT+'         VERY IMPORTANT   -   '.center(50)+todo[4:]+Fore.RESET+Style.RESET_ALL)
            number += 1
        elif todo.startswith('^^^^'):
            print(Fore.LIGHTMAGENTA_EX+str(number)+Fore.LIGHTRED_EX+Style.DIM+'IMPORTANT   -   '.center(50)+todo[4:]+Fore.RESET+Style.RESET_ALL)
            number += 1
        elif todo.startswith('&&&&'):
            print(Fore.LIGHTMAGENTA_EX+str(number)+Fore.LIGHTYELLOW_EX+'Eh...   -   '.center(50)+todo[4:]+Fore.RESET)
            number += 1
        elif todo.startswith('@@@@'):
            print(Fore.LIGHTMAGENTA_EX+str(number)+Fore.LIGHTGREEN_EX+'Fun !  -   '.center(50)+todo[4:]+Fore.RESET)
            number += 1

        elif todo.startswith('(((('):
            print(Fore.LIGHTMAGENTA_EX+str(number)+Fore.LIGHTCYAN_EX+'Reminder  -   '.center(50)+todo[4:]+Fore.RESET)
            number += 1

        elif todo.startswith('####'): 
            print(Fore.LIGHTMAGENTA_EX+str(number)+Fore.LIGHTCYAN_EX+'Done !  -   '.center(50)+todo[4:]+Fore.RESET)
            number += 1
        else:
            pass

    print(Fore.RESET)


def main():
    print(Fore.GREEN+"Hello Sepehr , I hope you're doing well.")
    print(Style.RESET_ALL)
    print('Your current Data list : ')
    seedata()
    print(r"1- Mark a todo 2-Add a todo\reminder 3- Clear Todo 4- Exit")

    choice = input("> ")
    if choice == "1":
        line = input('Line number ? > ')
        print('\n')
        markTodo(int(line)-1)
        main()
    elif choice == "2":
        addTodo()

    elif choice == "3":
        clearTodo()
    elif choice == "4":
        SystemExit

    else:
        print(Fore.RED+"Wrong Choice Sepehr !!\n\n\n")
        print(Style.RESET_ALL)
        main()

main()
