import argparse as arg
from datetime import datetime,timedelta
import pickle,os
from colorama import Fore,init
init(autoreset=True)
parser = arg.ArgumentParser

parser.add_argument(
    "-a","--add",help=
    """
        adds a new entry. task_details: default: None, time: default:now: 'H:M' format,when: default: now(AM/PM) interval: default:15 min
    """
    )
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
            return "ERR: statefile not found."

class list_ctrl:
    @staticmethod
    def when_is_now() -> list:
        '''
        # Returns ["Hour in 12-hour format","minute","AM/PM"]
        '''
        return [datetime.today().strftime("%I/%M/%p").split("/")]

    def read_data(self) -> str or dict:
        state = state()
        data = state.read_state()
        if not isinstance(data,dict):
            verboseprinting("ERR: state-data type is not dict")
            return "ERR: state-data type is not dict"
        file_to_read = data["timebox_file"]
        with open(file_to_read,'rb') as file:
            data = pickle.load(file)
            return data
    
    def calculate_end_time(self,time:str,interval:int) -> str:
        if all(map(lambda x: isinstance(x,(str,int)),[time,interval])):  
            # if time : str and interval : int
            time_converted = datetime.strptime(time,"%I:%M")
            time_converted += timedelta(minutes=interval)
            end_time = datetime.strftime(time_converted,"%I:%M")
            return end_time

        
    def add_entry(self,task_details,time='now',when='now',interval=15):
        verboseprinting(f"Adding new entry task_details:{task_details}, time:{time},interval:{interval}")
        time_data = self.when_is_now()
        when = when if when != "now" else time_data[-1] 
        time = time if time != "now" else ':'.join(time_data[0:-1])
        end_time = self.calculate_end_time(time,interval)
        verboseprinting(f"selected {time_data=},{when=},{time=}")
        state = state()
        state = state.read_state()
        if not isinstance(state,dict):
            verboseprinting("ERR: state-data type is not dict")
            return "ERR: state-data type is not dict"
        file_to_write = state["timebox_file"]
        entry_data = self.read_data()
        if isinstance(entry_data,dict):
            # start adding data
            entry_data[list(entry_data.keys())[-1]+1] = [
                time,end_time,when,task_details
            ]
            with open(file_to_write,"rb") as f:
                pickle.dump(entry_data)

        verboseprinting("Done.")

    def remove_entry(self,task_num):
        state = state()
        state = state.read_state()
        if not isinstance(state,dict):
            verboseprinting("ERR: state-data type is not dict")
            return "ERR: state-data type is not dict"
        file_to_write = state["timebox_file"]
        entry_data = self.read_data()
        if task_num in entry_data.keys():
            verboseprinting(f"Deleting task_num {task_num}")
            entry_data.pop(task_num)
        else:
            verboseprinting("ERR: Invalid task number.")
            return "Invalid task number."
        
    def make_new(self,listnum):
        if os.path.isfile(listnum):
            verboseprinting(f"ERR: {listnum} already exists")
            return f"ERR: {listnum} already exists"
        
        else:
            with open(listnum,"wb") as f:
                pickle.dump({})
                verboseprinting("Done.")
                return "Done."

