arranged = ["1s","2s","2p","3s","3p","3d","4s","4p","4d","4f","5s","5p","5d","5f","6s","6p","6d","7s","7p"]
mountain_afba_fillin = {
                "1s":"","2s":"","2p":"","3s":"","3p":"",
                "4s":"","3d":"","4p":"","5s":"","4d":"","5p":"",
                "6s":"","4f":"","5d":"","6p":"","7s":"","5f":"",
                "6d":"","7p":"",
                }
periodicity = {"He":[1,2],"Ne":[2,10],"Ar":[3,18],"Kr":[4,36],"Xe":[5,54],"Rn":[6,86]}


def menu():
    print("*"*10)
    print("Electron's Configuration calculator")
    print("1- Summarized electron configuration 2- Complete electron configuration ")
    choice = input("> ")
    if choice == "1":
        electron_config()
    if choice == "2":
        complete_electron_config()


def get_key_from_value(dic,value):
    for dic_key,dic_value in zip(dic.keys(),dic.values()):
        if dic_value == value:
            return dic_key


def arrange_mountain_afba(mountain_afba_fillin):
    m_afba_arranged = {}
    for orbital in arranged:
        m_afba_arranged[orbital] = mountain_afba_fillin[orbital]
    return m_afba_arranged


def mountain_afba(mountain_afba_list,periodic,atomic_number):
    for orbital in mountain_afba_list[mountain_afba_list.index(f"{periodic}s"):]:
        if orbital.endswith("s") and atomic_number >= 1:
            max = 2
            done = False
            while not done and max >= 1:
                if atomic_number - max >= 0:
                    mountain_afba_fillin[orbital] = max
                    atomic_number -= max
                    done = True

                else:
                    max -= 1
                    continue

            else:
                pass


        if orbital.endswith("p") and atomic_number >= 3:
            max = 6
            done = False

            while not done and max >= 1:
                if atomic_number - max >= 0:
                    mountain_afba_fillin[orbital] = max
                    atomic_number -= max
                    done = True

                else:
                    max -= 1
                    continue
            else:
                pass

        
        if orbital.endswith("d") and atomic_number >= 4:
            max = 10
            done = False
            while not done and max >= 1:
                if atomic_number - max >= 0:
                    mountain_afba_fillin[orbital] = max
                    atomic_number -= max
                    done = True

                else:
                    max -= 1
                    continue
            else:
                pass

        if orbital.endswith("f") and atomic_number >= 5:
            max = 14
            done = False
            while not done and max >= 1:
                if atomic_number - max >= 0:
                    mountain_afba_fillin[orbital] = max
                    atomic_number -= max
                    done = True
                else:
                    max -= 1
                    continue
            else:
                pass


    return mountain_afba_fillin


def check_for_exceptions(mountain_afba_fillin_keys):
    for orbital in mountain_afba_fillin.keys():
        if orbital.endswith("s"):
            if mountain_afba_fillin[orbital] :
                if int(mountain_afba_fillin[orbital]) + 1 == 2:
                    try:
                        next_orbital = mountain_afba_fillin_keys[mountain_afba_fillin_keys.index(orbital)+1]
                    except:
                        continue
                    if mountain_afba_fillin[next_orbital]:

                        pass
                    else:
                        continue
                    mountain_afba_fillin[next_orbital] = int(mountain_afba_fillin[next_orbital]) - 1
                    mountain_afba_fillin[orbital] = int(mountain_afba_fillin[orbital]) + 1

        if orbital.endswith("p"):
            if mountain_afba_fillin[orbital] :
                if int(mountain_afba_fillin[orbital]) + 1 == 3 or int(mountain_afba_fillin[orbital]) + 1 == 6:
                    try:
                        next_orbital = mountain_afba_fillin_keys[mountain_afba_fillin_keys.index(orbital)+1]
                    except:
                        continue
                    if mountain_afba_fillin[next_orbital]:
                        pass
                    else:
                        continue
                    mountain_afba_fillin[next_orbital] = int(mountain_afba_fillin[next_orbital]) - 1
                    mountain_afba_fillin[orbital] = int(mountain_afba_fillin[orbital]) + 1

        if orbital.endswith("d"):
            if mountain_afba_fillin[orbital] :
                if int(mountain_afba_fillin[orbital]) + 1 == 5 or int(mountain_afba_fillin[orbital]) + 1 == 10:
                    try:
                        next_orbital = mountain_afba_fillin_keys[mountain_afba_fillin_keys.index(orbital)+1]
                    except:
                        continue
                    if mountain_afba_fillin[next_orbital]:
                        pass
                    else:
                        continue
                    mountain_afba_fillin[next_orbital] = int(mountain_afba_fillin[next_orbital]) - 1
                    mountain_afba_fillin[orbital] = int(mountain_afba_fillin[orbital]) + 1

        if orbital.endswith("f"):
            if mountain_afba_fillin[orbital] :
                if int(mountain_afba_fillin[orbital]) + 1 == 7 or int(mountain_afba_fillin[orbital]) + 1 == 14:
                    try:
                        next_orbital = mountain_afba_fillin_keys[mountain_afba_fillin_keys.index(orbital)+1]
                    except:
                        continue
                    if mountain_afba_fillin[next_orbital]:
                        pass
                    else:
                        continue
                    mountain_afba_fillin[next_orbital] = int(mountain_afba_fillin[next_orbital]) - 1
                    mountain_afba_fillin[orbital] = int(mountain_afba_fillin[orbital]) + 1\

    return mountain_afba_fillin


def ion_charge_calculator(ion_charge,mountain_afba_fillin):
    if ion_charge:
        if int(ion_charge):
            mountain_afba_fillin = list([i,j] for i,j in mountain_afba_fillin.items())
            ion_charge = int(ion_charge)
            if ion_charge > 0:
                for row in mountain_afba_fillin[::-1]:
                    if ion_charge > 0:
                        if row[1]:
                            if int(row[1]) > 0:
                                while int(row[1]) > 0 and ion_charge > 0:
                                    row[1] -= 1
                                    ion_charge -= 1
                                    continue
                                else:
                                    pass

                        else:
                            continue
                else:
                    mountain_afba_fillin = {key:value for key,value in mountain_afba_fillin}

            else:
                for row in mountain_afba_fillin[::-1]:
                    if row[1] and ion_charge != 0:
                        if int(row[1]) > 0:
                            done = False
                            while not done:
                                if row[0].endswith("s"):
                                    max = 2
                                elif row[0].endswith("p"):
                                    max = 6
                                elif row[0].endswith("d"):
                                    max = 10
                                else:
                                    max = 14
                                if row[1] < max:

                                    row[1] = int(row[1])  + 1
                                    ion_charge += 1
                                    continue
                                else:
                                    done = True
                            else:
                                pass

                    else:
                        continue
                else:
                    mountain_afba_fillin = {key:value for key,value in mountain_afba_fillin}

    return mountain_afba_fillin

        
                



def electron_config():
    global mountain_afba_fillin
    print("Enter the atomic number => ")
    atomic_number = int(input("> "))
    print("Is your atom an ion ? If yes please provide the charge , otherwise leave it blank")
    ion_charge = input("> ")
    # Finding the noble gass we should use
    for element_name,element_data in zip(periodicity.keys(),periodicity.values()):
        # element_data[0] is periodicity number & element_data[1] is atomic number of the noble gass

        if atomic_number > 118:
            print("Can't calculate element's higher than 118")
        if atomic_number > 85:
            print("[Rn^86]")
            atomic_number -= 86
            periodic = 7
            mountain_afba_list = list(mountain_afba_fillin.keys())
            mountain_afba_fillin = mountain_afba(mountain_afba_list,periodic,atomic_number)
            break

        elif element_data[1] <= atomic_number <= list(periodicity.values())[element_data[0]][1]:
            element_name = get_key_from_value(periodicity,element_data)
            print(f"[{element_name}^{element_data[1]}]")
            atomic_number -= element_data[1]
            periodic = element_data[0] + 1
            mountain_afba_list = list(mountain_afba_fillin.keys())
            mountain_afba_fillin = mountain_afba(mountain_afba_list,periodic,atomic_number)
            break

    mountain_afba_fillin = arrange_mountain_afba(mountain_afba_fillin)
    mountain_afba_fillin_keys = list(mountain_afba_fillin.keys())
    mountain_afba_fillin = check_for_exceptions(mountain_afba_fillin_keys)
    mountain_afba_fillin = ion_charge_calculator(ion_charge,mountain_afba_fillin)

    for orbital,value in zip(mountain_afba_fillin.keys(),mountain_afba_fillin.values()):
        if value:
            print(f"{orbital}^{value}")


def complete_electron_config():
    global mountain_afba_fillin
    print("Enter the atomic number => ")
    atomic_number = int(input("> "))
    print("Is your atom an ion ? If yes please provide the charge , otherwise leave it blank")
    ion_charge = input("> ")
    # Finding the noble gass we should use
        # element_data[0] is periodicity number & element_data[1] is atomic number of the noble gass
    mountain_afba_list = list(mountain_afba_fillin.keys())
    for orbital in mountain_afba_list:
        if orbital.endswith("s"):
            max = 2
            done = False
            while not done and max >= 1:
                if atomic_number - max >= 0:
                    mountain_afba_fillin[orbital] = max
                    atomic_number -= max
                    done = True

                else:
                    max -= 1
                    continue

            else:
                continue


        if orbital.endswith("p"):
            max = 6
            done = False

            while not done and max >= 1:
                if atomic_number - max >= 0:
                    mountain_afba_fillin[orbital] = max
                    atomic_number -= max
                    done = True

                else:
                    max -= 1
                    continue
            else:
                continue


        if orbital.endswith("d"):
            max = 10
            done = False
            while not done and max >= 1:
                if atomic_number - max >= 0:
                    mountain_afba_fillin[orbital] = max
                    atomic_number -= max
                    done = True

                else:
                    max -= 1
                    continue
            else:
                continue

        if orbital.endswith("f"):
            max = 14
            done = False
            while not done and max >= 1:
                if atomic_number - max >= 0:
                    mountain_afba_fillin[orbital] = max
                    atomic_number -= max
                    done = True
                else:
                    max -= 1
                    continue
            else:
                continue

    
    
    mountain_afba_fillin = arrange_mountain_afba(mountain_afba_fillin)
    mountain_afba_fillin_keys = list(mountain_afba_fillin.keys())
    mountain_afba_fillin = check_for_exceptions(mountain_afba_fillin_keys)
    mountain_afba_fillin = ion_charge_calculator(ion_charge,mountain_afba_fillin)
    for orbital,value in zip(mountain_afba_fillin.keys(),mountain_afba_fillin.values()):
        if value:
            print(f"{orbital}^{value}")



menu()