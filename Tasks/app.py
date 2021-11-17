# Simple app to record tasks and their times , with notifications and reminders
import argparse as arg
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

def reminder():
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
    #   ┌───────────────────────┐
    #   │  Is the user          │
    #   │  Requesting to add a  │
    #   │  new reminder?        ├─────┐
    #   │                       │     │
    #   │                       │     │
    #   └─────┬─────────────────┘     │
    #         │                       │
    #         │                       │
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
    with open("database.txt", "r") as file:
        for element in file:
            pass

parser = arg.ArgumentParser(description="Simple app to record tasks and their times , with notifications and reminders")
parser.add_argument("-r", "--reminder", help="Reminder for task", action="store_true")
parser.add_argument("-t", "--task", help="Task to be recorded")
parser.add_argument("-d", "--date", help="Date of task")
parser.add_argument("-du", "--duration", help="Duration of task in seconds")
parser.add_argument("-c", "--comment", help="Comment for task")
args = parser.parse_args()
if args.reminder and args.du:
    print("Reminder set for {} seconds".format(args.du))

