# CODE STILL IN PRODUCTION !
# Simple app to record tasks and their times , with notifications and reminders
import argparse as arg
import threading
import datetime
from dateutil.parser import parse
"""
-r For reminders
-t For tasks
-d For date
-du For duration * in seconds *
-c For comment
-rl For reminder list
-tl For task list
-dr To delete a reminder
-dt To delete a task
"""
def argparser(args):
    if args.r:
        reminder_tools(args.r,args.d,args.c,args.dr,args.lr)
        

    if args.t:
        tasks_tools(args.t,args.du,args.c,args.dt,args.lt)

def start_reminder(reminder):
    #TODO : Add comment and etc here.
    pass


def reminder_tools(
    reminder:str,date:str,comment:str,delete_reminder=False,list_reminders=False):
    active_reminders = []
    #     ┌─────────────────┐
    #     │                 │
    #     │      Start      │
    #     │                 │
    #     └────────┬────────┘
    #              │
    #              │
    #              │
    #              │
    #              │
    #              │
    #              │
    #              ▼
    #      ┌───────────────┐
    #      │ Is there any  │     Yes
    #      │ Active        ├──────────────────┐
    #      │ Reminders?    │                  ▼
    #      └───────┬───────┘             ┌──────────────┐
    #              │                     │Import them   │
    #              │                     │And run new   │
    #           No │                     │Threads For   │
    #              │                     │Each reminder.│
    #              │                     │              │
    #              ▼                     └──────────────┘
    #   ┌───────────────────────┐                │
    #   │  Is the user          │<───────────────│
    #   │  Requesting to add a  │
    #   │  new reminder?        ├──────┐
    #   │                       │      │
    #   │                       │      │
    #   └─────┬─────────────────┘      │
    #         │                        │
    #         No                      Yes
    #         │                        │
    #         │                        ▼
    #         │                        │
    # ┌───────┴─────┐                  │
    # │  Does the   │                  │
    # │  User want  │                  │
    # │  To list    │<─  ┌─────────────┴─────┐
    # │  reminders? │ │  │  Add the new      │
    # │             │ │  │ Date and time Into│
    # └────│───│────┘ │  │ database.txt      │
    #      │   │      │  │ And run a new     │
    #      Yes No     │  │ thread for the    │
    #      │   │      │──│   reminder        │
    #      │   │──────   └───────────────────┘             
    # ┌────┴─────┐    │                   
    # │ List the │    │
    # │remidners │    │   
    # │          │    │
    # │          │    │
    # │          │    │
    # └────┬─────┘    │
    # ┌────┴─────┐    │                   
    # │  End     │<───│
    # └──────────┘

    print("Checking for active Reminders...")

    # Checking for active reminders :
    with open("database.txt", "r") as file:
        for element in file:
            active_reminders.append(element)


    active_reminders = [x.strip() for x in active_reminders]
    if len(active_reminders) == 0:
        print("No active reminders")

    else:
        print("Active reminders : ")
        for element in active_reminders:
            print(element)
            new_reminder = threading.Thread(target=start_reminder, args=(element,)) #TODO : Fix start_reminder
            new_reminder.start()

    # If not :
    # Checking if the date is correct
    date = parse(date)

    if date.year and date.month and date.day and \
    date.hour and date.minute and date.second:
        print("Date is correct")

    else:
        print("Date is not correct")
        return "Date Is Not Correct."



    # Setting new reminders :
    print("Setting new reminders...")
    if reminder:
        print(f"Setting reminder {reminder}")
        try:
            new_reminder = threading.Thread(target=start_reminder, args=(reminder,))
            new_reminder.start()
        except Exception as e:
            return e

        else:
            print("Reminder set")
            with open("database.txt", "a") as file:
                file.write(f"{reminder}/{date}\n")

    else:
        print("No reminder set")

    # Deleting reminders :
    print("Checking for reminders to delete...")
    if delete_reminder and reminder:
        print(f"Deleting reminder {reminder}")
        try:
            with open("database.txt", "r") as file:
                lines = file.readlines()
            with open("database.txt", "w") as file:
                for line in lines:
                    if f"{reminder}/{date}" not in line:
                        file.write(line+"\n")
        except Exception as e:
            print("Unknown Error...")
            return e
        else:
            print("Reminder deleted")
            # TODO : Delete the reminder from the active reminders list.

    else:
        print("No reminder to delete")

    if list_reminders:
        print("Listing reminders...")
        try:
            with open("database.txt", "r") as file:
                lines = file.readlines()
            for line in lines:
                print(line)
        except Exception as e:
            print("Unknown Error...")
            return e
        else:
            print("Reminders listed")

def tasks_tools(task:str,duration:str,comment:str,delete_tasks=False,list_tasks=False):
    pass

parser = arg.ArgumentParser(description="Simple app to record tasks and their times , with notifications and reminders")
parser.add_argument("-r", "--reminder", help="Reminder for task", action="store_true")
parser.add_argument("-t", "--task", help="Task to be recorded")
parser.add_argument("-d", "--date", help="Date of task")
parser.add_argument("-du", "--duration", help="Duration of task in seconds")
parser.add_argument("-c", "--comment", help="Comment for task")
#TODO : Add other args
args = parser.parse_args()
argparser(args)

