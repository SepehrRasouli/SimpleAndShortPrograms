import argparse as arg
from datetime import datetime,timedelta
import pickle,os
from colorama import Fore,init
init(autoreset=True)
parser = arg.ArgumentParser()

parser.add_argument(
    "-a","--add",help=
    """
        adds a new entry. task_details: default: None, time: default:now: 'H:M' format,when: default: now(AM/PM) interval: default:15 min
    """,nargs=4,metavar="\b"
    )
parser.add_argument("-r","--remove",help="removes an entry. task-num: default:0",nargs=1,metavar='\b')
parser.add_argument("-sh","--show",help="shows timeboxing text.",action="store_true")
parser.add_argument("-sw","--switch",help="switches to another list. list-num: default=1",nargs=1,metavar='\b')
parser.add_argument("-cs","--current-state",help="prints current state",action="store_true")
parser.add_argument("-m","--make",help="makes a new list. list-num: default:None",nargs=1,metavar='\b')
# parser.add_argument("-d","--delete",help="deletes a list. list-num: default:None",nargs=1,metavar='\b')
parser.add_argument("-v","--verbose",help="verbose",action="store_true")
args = parser.parse_args()

verboseprinting = print if args.verbose else lambda *a,**k:None

def choose_color_and_box(task_data):
    if int(task_data) <= 15:
        return ["\033[32m","#"] # green
    
    if 15 < int(task_data) <= 30:
        return ["\033[34m","/"] # blue 

    if 30 < int(task_data) <= 45:
        return ["\033[0;35m","*"] # purple
    
    if int(task_data) > 45:
        return ["\033[31m","^"]

    else:
        return ["\033[39m"] # end

def show(data):
    reset = "\033[0m"
    for i in data:
        chosen_data =  choose_color_and_box(data[i][3])
        chosen_color = chosen_data[0]
        header = chosen_color+ \
        f"""TaskNum: {i} StartTime:{data[i][0]} {data[i][1]}, EndTime:{data[i][2]}, Interval:{data[i][3]}M """.center(150,'-')+reset
        print('\n')
        print(header)
        task_details = "Task Details : " + data[i][4] + ' ' + chosen_data[1]
        print(chosen_color+chosen_data[1]*len(task_details)+reset)
        print(chosen_color+task_details+reset)
        print(chosen_color+chosen_data[1]*len(task_details)+reset)


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
            
    def change_state(self,new_state:str):
        verboseprinting("Changing state")
        if os.path.isfile("state"):
            with open("state","rb") as statefile:
                data = pickle.load(statefile)
                verboseprinting(f"Current State:{data}")
                verboseprinting(f"Changing State To : {new_state}.pickle")
                
            with open("state","wb") as statefile:
                pickle.dump({"timebox_file":new_state+".pickle"},statefile)
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
        return datetime.today().strftime("%I/%M/%p").split("/")

    def read_data(self) -> dict:
        state_ctrl = state()
        current_state = state_ctrl.read_state()
        file_to_read = current_state["timebox_file"]
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

        
    def add_entry(self,task_details:str,time='now',when='now',interval=15):
        verboseprinting(f"Adding new entry task_details:{task_details}, time:{time},interval:{interval}")
        time_data = self.when_is_now()
        when = when if when != "now" else time_data[-1] 
        time = time if time != "now" else ':'.join(time_data[0:-1])
        end_time = self.calculate_end_time(time,int(interval))
        verboseprinting(f"selected {time_data=},{when=},{time=}")
        state_ctrl = state()
        current_state = state_ctrl.read_state()
        file_to_write = current_state["timebox_file"]
        entry_data = self.read_data()
        if isinstance(entry_data,dict):
            # start adding data
            if entry_data:
                entry_data[list(entry_data.keys())[-1]+1] = [
                    time,end_time,when,interval,task_details
                ]
            else:
                entry_data[0] = [
                    time,end_time,when,interval,task_details
                ]
            with open(file_to_write,"wb") as f:
                pickle.dump(entry_data,f)

        verboseprinting("Done.")

    def remove_entry(self,task_num:int):
        state_ctrl = state()
        current_state = state_ctrl.read_state()
        file_to_write = current_state["timebox_file"]
        entry_data = self.read_data()
        if task_num in entry_data.keys():
            verboseprinting(f"Deleting task_num {task_num}")
            entry_data.pop(task_num)
            with open(file_to_write,"wb") as f:
                pickle.dump(entry_data,f)
        else:
            verboseprinting("ERR: Invalid task number.")
            return "Invalid task number."
        
    def make_new(self,listnum:int):
        if os.path.isfile(listnum+'.pickle'):
            verboseprinting(f"ERR: {listnum} already exists")
            return f"ERR: {listnum} already exists"
        
        else:
            with open(listnum+'.pickle',"wb") as f:
                pickle.dump({})
                verboseprinting("Done.")
                return "Done."

if args.add:
    if all(
        map(
            lambda x: isinstance(x,str) or x.isidigit()
            ,args.add[0:len(args.add)-1])):
                list_ctrl = list_ctrl()
                list_ctrl.add_entry(*args.add)
                print("Done.") #TODO: change this
    else:
        pass #TODO: change this

if args.remove:
    if ''.join(args.remove).isdigit():
        list_ctrl = list_ctrl()
        list_ctrl.remove_entry(int(''.join(args.remove)))
        print("Done.") #TODO: change this

    else:
        pass #TODO: change this

if args.switch:
    state_ctrl = state()
    state_ctrl.change_state(''.join(args.switch))
    print("Done.") #TODO: change this

if args.current_state:
    state_ctrl = state()
    data = state_ctrl.read_state()
    print(data)

if args.make:
    list_ctrl = list_ctrl()
    if ''.join(args.make).isdigit():
        if ''.join(args.make).endswith('.pickle'):
            print("ERR: Don't put .pickle as a list num")

        else:
            list_ctrl.make_new(int(''.join(args.make)))
            print("Done.") #TODO: change this

    else:
        pass #TODO: change this

# if args.delete:
# later add this.

if args.show:
    list_ctrl = list_ctrl()
    data = list_ctrl.read_data()
    show(data)
