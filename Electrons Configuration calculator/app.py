import colorama
from colorama import Fore, Back, Style
class Electrons_Configurations:
    #TODO: Complete This Class
    def __init__(self,atomic_number:int,charge:int=0):
        self.atomic_number:int = atomic_number
        self.charge:int = charge
        self.aufbau_principle = {
                "1s":"","2s":"","2p":"","3s":"","3p":"",
                "4s":"","3d":"","4p":"","5s":"","4d":"","5p":"",
                "6s":"","4f":"","5d":"","6p":"","7s":"","5f":"",
                "6d":"","7p":"",
                }
        self.noble_gas_list:dict = {"He":[1,2],"Ne":[2,10],"Ar":[3,18],"Kr":[4,36],"Xe":[5,54],"Rn":[6,86]}
        self.arranged:list = ["1s","2s","2p","3s","3p","3d","4s","4p","4d","4f","5s","5p","5d","5f","6s","6p","6d","7s","7p"]

    def main(self):
        '''This is the main function of the Electrons_configuration class.
        Returns: 
        A list of the both complete and summarized configuration of the element and the filled aufbau principle dictionary.
        '''


    def complete_config(self):
        pass

    def summarized_config(self):
        pass

    


def main():
    print(f'{colorama.Fore.CYAN}Elements Details{colorama.Fore.RESET}')
    print(f'{colorama.Fore.CYAN}Please Enter The atomic number => {colorama.Fore.RESET}')
    atomic_number = int(input("> ")) 
    print(f'{colorama.Fore.CYAN}Please Enter The element\'s Charge *Enter Zero If The Element Dosen\'t Have Any Charge* => {colorama.Fore.RESET}')
    charge = int(input("> "))
    Electrons_Configuration = Electrons_Configurations(int(atomic_number),int(charge))
    configs: list = Electrons_Configuration.main() # This will also contain a list with the Aufbau principle of the element's electron's configuration



if __name__ == '__main__':
    main()
