# Simple app to record tasks and their times , with notifications and reminders
import argparse as arg
import threading
import time
"""
-r For reminders
-t For tasks
-d For date
-du For duration * in seconds *
-c For comment
-rl For reminder list
-tl For task list
-dr To delete a reminder
"""
def start_reminder(reminder):
    pass


def reminder():
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
    #   │  new reminder?        ├─────┐
    #   │                       │     │
    #   │                       │     │
    #   └─────┬─────────────────┘     │
    #         │                       │
    #         No                     Yes
    #         │                       │
    #         │                       ▼
    #         │                       │
    # ┌───────┴─────┐   ┌─────────────┴─────┐
    # │             │   │      Add the new  │
    # │     End     │   │ Date and time Into│
    # └─────────────┘   │ database.txt      │
    #                   │ And run a new     │
    #                   │ Thread for the    │
    #                   │ Reminder          │
    #                   └───────────────────┘


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
            new_reminder = threading.Thread(target=start_reminder, args=(element,))
            new_reminder.start()
            


parser = arg.ArgumentParser(description="Simple app to record tasks and their times , with notifications and reminders")
parser.add_argument("-r", "--reminder", help="Reminder for task", action="store_true")
parser.add_argument("-t", "--task", help="Task to be recorded")
parser.add_argument("-d", "--date", help="Date of task")
parser.add_argument("-du", "--duration", help="Duration of task in seconds")
parser.add_argument("-c", "--comment", help="Comment for task")
args = parser.parse_args()
if args.reminder and args.du:
    print("Reminder set for {} seconds".format(args.du))

