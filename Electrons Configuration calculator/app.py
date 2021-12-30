import colorama

class Electrons_Configurations:
    pass

def main():
    print(f'{colorama.Fore.CYAN}Elements Details{colorama.Fore.RESET}')
    print(f'{colorama.Fore.CYAN}Please Enter The atomic number => {colorama.Fore.RESET}')
    atomic_number = int(input("> ")) 
    print(f'{colorama.Fore.CYAN}Please Enter The element\'s Charge *Enter Zero If The Element Dosen\'t Have Any Charge* => {colorama.Fore.RESET}')
    charge = int(input("> "))
    electrons_configs: list = Electrons_Configurations() #TODO : Fix This.

if __name__ == '__main__':
    main()
