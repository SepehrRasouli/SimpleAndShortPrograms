'''
Timeboxing alternative for google schedule because i was tired of how hard it is to work with it :).
'''
import argparse as arg
from datetime import datetime,timedelta
import pickle
import os
from typing import List
parser = arg.ArgumentParser()
parser.add_argument(
    "-a","--add",help="adds a new entry. task_details: default: None, time: default:now: \
    'H:M' format,when: default: now(AM/PM) interval: default:15 min",nargs=4,metavar="\b"
    )
parser.add_argument(
    "-r","--remove",help="removes an entry. task-num: default:0",nargs=1,metavar='\b'
    )
parser.add_argument(
    "-sh","--show",help="shows timeboxing text.",action="store_true"
    )
parser.add_argument(
    "-sw","--switch",help="switches to another list. list-num: default=1",nargs=1,metavar='\b'
    )
parser.add_argument(
    "-cs","--current-state",help="prints current state",action="store_true"
    )
parser.add_argument(
    "-m","--make",help="makes a new list. list-num: default:None",nargs=1,metavar='\b'
    )
parser.add_argument(
    "-v","--verbose",help="verbose",action="store_true"
    )
args = parser.parse_args()

verboseprinting = print if args.verbose else lambda *a,**k:None

def choose_color_and_box(task_data:int) -> List[str,str]:
    '''
    Chooses color and boxing character based on task_data
    '''
    if int(task_data) <= 15:
        return ["\033[32m","#"] # green

    if 15 < int(task_data) <= 30:
        return ["\033[34m","/"] # blue

    if 30 < int(task_data) <= 45:
        return ["\033[0;35m","*"] # purple

    if int(task_data) > 45:
        return ["\033[31m","^"]

    return ["\033[39m"] # end

def show(data:list):
    '''shows timeboxing data.
    Args:
        list: task-data
    '''
    reset = "\033[0m"
    for i in data:
        chosen_data =  choose_color_and_box(data[i][3])
        chosen_color = chosen_data[0]
        header = chosen_color + f"""TaskNum: {i} StartTime:{data[i][0]} {data[i][1]}, \
        EndTime:{data[i][2]}, Interval:{data[i][3]}M """.center(150,'-')+reset
        print('\n')
        print(header)
        task_details = "Task Details : " + data[i][4] + ' ' + chosen_data[1]
        print(chosen_color+chosen_data[1]*len(task_details)+reset)
        print(chosen_color+task_details+reset)
        print(chosen_color+chosen_data[1]*len(task_details)+reset)


class StateCtrl:
    '''
    Base for any state-file control functions.
    '''
    @staticmethod
    def read_state():
        '''
        Reads state-data and returns it.
        Returns:
            dict: state-data
        '''
        verboseprinting("Reading State...")
        if os.path.isfile("state"):
            with open("state","rb") as statefile:
                data = pickle.load(statefile)
                verboseprinting(f"State:{data}")
                return data

        else:
            verboseprinting("ERR: statefile not found.")
            return False

    @staticmethod
    def change_state(new_state:str):
        '''
        Changes state-data.
        Args:
            new_state(str): new state
        '''
        verboseprinting("Changing state")
        if os.path.isfile("state"):
            with open("state","rb") as statefile:
                data = pickle.load(statefile)
                verboseprinting(f"Current State:{data}")
                verboseprinting(f"Changing State To : {new_state}.pickle")

            with open("state","wb") as statefile:
                pickle.dump({"timebox_file":new_state+".pickle"},statefile)
                verboseprinting("Changed state.")
                return True

        else:
            verboseprinting("ERR: statefile not found.")
            return "ERR: statefile not found."

class ListCtrl:
    '''
    Controls list-data.
    '''
    @staticmethod
    def when_is_now() -> list:
        '''
        Returns(list): ["Hour in 12-hour format","minute","AM/PM"]
        '''
        return datetime.today().strftime("%I/%M/%p").split("/")

    @staticmethod
    def read_data() -> dict:
        '''
        Reads list data.
        Returns(dict): list-data
        '''
        state_ctrl = StateCtrl()
        current_state = state_ctrl.read_state()
        file_to_read = current_state["timebox_file"]
        with open(file_to_read,'rb') as file:
            data = pickle.load(file)
            return data

    @staticmethod
    def calculate_end_time(time:str,interval:int) -> str or bool:
        '''
        Calculates end_time
        Args:
            time(str): start-time
            interval(int): interval to calculate end-time with it.
        '''
        if all(map(lambda x: isinstance(x,(str,int)),[time,interval])):
            # if time : str and interval : int
            time_converted = datetime.strptime(time,"%I:%M")
            time_converted += timedelta(minutes=interval)
            end_time = datetime.strftime(time_converted,"%I:%M")
            return end_time
        return False


    def add_entry(self,task_details:str,time='now',when='now',interval=15):
        '''
        Adds a new entry to list-data.
        Args:
            task_details(str): task-details
            time(str): start-time. default:now
            when(str): end-time. default:now
            interval(int): interval to calculate end-time with it. default:15
        '''
        verboseprinting(f"Adding new entry\
         task_details:{task_details}, time:{time},interval:{interval}")
        time_data = self.when_is_now()
        when = when if when != "now" else time_data[-1]
        time = time if time != "now" else ':'.join(time_data[0:-1])
        end_time = self.calculate_end_time(time,int(interval))
        verboseprinting(f"selected {time_data=},{when=},{time=}")
        state_ctrl = StateCtrl()
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
            with open(file_to_write,"wb") as file:
                pickle.dump(entry_data,file)

        verboseprinting("Done.")

    def remove_entry(self,task_num:int) -> bool or str:
        '''
        Removes an entry from list-data.
        Args:
            task_num(int): task-num to remove
        '''
        state_ctrl = StateCtrl()
        current_state = state_ctrl.read_state()
        file_to_write = current_state["timebox_file"]
        entry_data = self.read_data()
        if task_num in entry_data.keys():
            verboseprinting(f"Deleting task_num {task_num}")
            entry_data.pop(task_num)
            with open(file_to_write,"wb") as file:
                pickle.dump(entry_data,file)
            return True

        verboseprinting("ERR: Invalid task number.")
        return "Invalid task number."

    @staticmethod
    def make_new(listnum:str) -> str:
        '''
        Makes a new list file.
        Args:
            listnum(str): list-number
        '''
        if os.path.isfile(listnum+'.pickle'):
            verboseprinting(f"ERR: {listnum} already exists")
            return f"ERR: {listnum} already exists"

        with open(listnum+'.pickle',"wb") as file:
            pickle.dump({},file)
            verboseprinting("Done.")
            return "Done."

if args.add:
    if all(map(lambda x: isinstance(x,str) or x.isidigit(),args.add[0:len(args.add)-1])):
        list_ctrl = ListCtrl()
        list_ctrl.add_entry(*args.add)
        print("Done.")
    else:
        pass

if args.remove:
    if ''.join(args.remove).isdigit():
        list_ctrl = ListCtrl()
        list_ctrl.remove_entry(int(''.join(args.remove)))
        print("Done.")

    else:
        pass

if args.switch:
    state_ctrl = StateCtrl()
    state_ctrl.change_state(''.join(args.switch))
    print("Done.")

if args.current_state:
    state_ctrl = StateCtrl()
    data = state_ctrl.read_state()
    print(data)

if args.make:
    list_ctrl = ListCtrl()
    if ''.join(args.make).isdigit():
        if ''.join(args.make).endswith('.pickle'):
            print("ERR: Don't put .pickle as a list num")

        else:
            list_ctrl.make_new(''.join(args.make))
            print("Done.")

    else:
        pass

# if args.delete:
# later add this.

if args.show:
    list_ctrl = ListCtrl()
    data = list_ctrl.read_data()
    show(data)
