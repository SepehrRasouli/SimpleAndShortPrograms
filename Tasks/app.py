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

def start_reminder(reminder,comment:str = '',date:str = '',delete_reminder:bool = False):
    # This function stores the reminders in a dicitonary and keeps track of them
    # when the timer is over , it will send a notification , and if it's prompted to delete
    # a reminder it will change the dictionary value of that remidner to 0 so the thread would
    # be able to check for it and terminate itself.
    pass


def reminder_tools(
    reminder:str,date:str,comment:str,delete_reminder=False,list_reminders=False):
    active_reminders = []
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
            new_reminder = threading.Thread(target=start_reminder, args=(reminder,date,comment))
            new_reminder.start()
        except Exception as e:
            return e

        else:
            print("Reminder set")
            with open("database.txt", "a") as file:
                file.write(f"{reminder}/{date}/{comment}\n")

    else:
        print("No reminder set")

    # Deleting reminders :
    print("Checking for reminders to delete...")
    if delete_reminder and reminder and date:
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
            start_reminder(f"{reminder}/{date}",delete_reminder=True)

    else:
        print("No reminder to delete or not efficent data to delete the reminder.")

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

