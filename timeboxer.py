import argparse as arg
import pickle,os
from tabnanny import verbose
from types import new_class
from colorama import Fore,init
init(autoreset=True)
parser = arg.ArgumentParser

parser.add_argument("-a","--add",help="adds a new entry. time: default:now,interval: default:15 min")
parser.add_argument("-r","--remove",help="removes an entry. task-num: default:0")
parser.add_argument("-sh","--show",help="shows timeboxing text. show_colors: default:True",action="store_false")
parser.add_argument("-sw","--switch",help="switches to another list. list-num: default=0")
parser.add_argument("-cs","--current-state",help="prints current state",action="store_true")
parser.add_argument("-m","--make",help="makes a new list. list-num: default:None")
parser.add_argument("-d","--delete",help="deletes a list. list-num: default:None")
parser.add_argument("-v","--verbose",help="verbose",action="store_true")
args = parser.parse_args()

verboseprinting = print if args.verbose else lambda *a,**k:None
class state:
    def read_state(self):
        verboseprinting("Reading State...")
        if os.path.isfile("state"):
            with open("state","rb") as statefile:
                data = pickle.load(statefile)
                verboseprinting(f"State:{data}")
                return data
        
        else:
            verboseprinting("ERR: statefile not found.")
            
    def change_state(self,new_state):
        verboseprinting("Changing state")
        if os.path.isfile("state"):
            with open("state","rb") as statefile:
                data = pickle.load(statefile)
                verboseprinting(f"Current State:{data}")
                verboseprinting(f"Changing State To : {new_state}")
                
            with open("state","wb") as statefile:
                pickle.dump({"statedata":new_state},statefile)
                verboseprinting(f"Changed state.")

        else:
            verboseprinting("ERR: statefile not found.")

class list_ctrl:
    def add_entry(self,time='now',interval=15):
       pass 
