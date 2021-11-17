# Simple app to record tasks and their times , with notifications and reminders
import argparse as arg
"""
-r For reminders
-t For tasks
-d For date
-du For duration * in seconds *
-c For comment
"""

def reminder():
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

