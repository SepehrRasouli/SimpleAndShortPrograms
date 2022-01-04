import colorama
from colorama import Fore, Back, Style
class Electrons_Configurations:
    #TODO: Complete This Class
    def __init__(self,atomic_number,charge):
        self.atomic_number = atomic_number
        self.charge = charge

    def main(self):
        pass

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
    Electrons_Configuration = Electrons_Configurations(atomic_number,charge)
    configs: list = Electrons_Configuration.main()


if __name__ == '__main__':
    main()
