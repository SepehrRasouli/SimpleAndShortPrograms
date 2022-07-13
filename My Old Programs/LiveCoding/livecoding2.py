# For Learning
# Improvments
import os
import os.path
import datetime
pfile = None
pfilecontent = None
infunction = None
functionname = None
logmake = 1
user_input = None
user_input_index = None
lenvariablesnames = None
length = None
endofpfile = None
lenfunctionsmade = None
librariesimportedlen = None
logmakefile = "log.txt"
misscommandslen = None
usrinput = None
usrinput_index = None
linenumber = None
texttofilepath = None
texttocommandinput = None
i = None

AINFUNCTION = "AINFUNCTION"
# Are In Function
LIBRARYUSED = "LIBRARYUSED"
VARIABLENAMEUSED = "VARIABLENAMEUSED"
FILENOTSPECIFIED = "FILENOTSPECIFIED"
FILEDONTEXIST = "FILEDONTEXIST"
NOTINFUNCTION = "NOTINFUNCTION"
AINPROJECT = "AINPROJECT"  # Are In Project
FILEEXIST = "FILEEXIST"
ABOUT = "This is project is the first generation of live coding systems. I wrote this version to learn more."
FUNCTIONEXISTS = "FUNCTIONEXISTS"

commands = ["openfile", "exitfile", "removeline", "removecode", "makefunction", "outfunction", "makevariable", "printcommand", "importlibrary", "seecode", "runcode", "delfile", "newproject", "about", "texttocommand", "comments", "append", "help", "status"]
semicommands = ["VV", "F", "LI", "R", "AL"] # For The Status Commands #VV = Variables With Values,F = Functions(Names),LI = Libraries Imported,#R = Return
variablesmade = []  # For The Status
functionsmade = []  # For The Status
librariesimported = []  # For The Status
variablesmadevalue = []  # For The Status


def openfile(name):
    if os.path.isfile("" +name+".py"):
        global pfile
        pfile = name+".py"
        print(pfile)
        return True
    else:
        return FILEDONTEXIST


def removecode():
    if pfile is not None:
        file2 = open( pfile, "w")
        file2.write("")
        file2.close()
        return True

    else:
        return FILENOTSPECIFIED


def makefunction(functionname):
    global infunction
    if functionname not in functionsmade:
        if infunction is True and pfile is not None:
            return AINFUNCTION

        elif pfile is None:
            return FILENOTSPECIFIED

        else:
            file3 = open(pfile, "a")
            file3.write("""
"""+"def "+ functionname+"():")
            file3.close()
            infunction = True
            functionsmade.append(functionname)

            return True

    else:
        return FUNCTIONEXISTS


def outfunction():
    if pfile is not None:
        global infunction
        if infunction is False:
            return NOTINFUNCTION

        else:
            infunction = False
            return True
    else:
        FILENOTSPECIFIED


def makevariable(value, variablename):
    if pfile is not None:
        if variablename in variablesmade:
            return VARIABLENAMEUSED
        
        elif infunction:
            value = '"'+ value+'" '
            file4 = open( pfile, "a")
            file4.write("""
    """+ variablename+" = "+ value)
            file4.close()
            variablesmade.append(variablename)
            variablesmadevalue.append(value)
            return AINFUNCTION

        else:
            value = '"'+ value+'" '
            file4 = open( pfile,"a")
            file4.write("""
"""+ variablename+"= "+ value)
            file4.close()
            variablesmade.append(variablename)
            variablesmadevalue.append(value)
            return True
    else:
        return FILENOTSPECIFIED


def printcommand(content):
    if infunction is True and pfile is not None:
        file25 = open(pfile,"a")
        file25.write("\n")
        file25.write('      print(')
        file25.write('"')
        file25.write(content)
        file25.write('"')
        file25.write(")")
        file25.close()
        return AINFUNCTION

    if infunction is False and pfile is not None:
        file26 = open( pfile, "a")
        file26.write("\n")
        file26.write('print(')
        file26.write('"')
        file26.write(content)
        file26.write('"')
        file26.write(")")
        file26.close()
        return True  
    else:
        return FILENOTSPECIFIED


def importlibrary(name):
    if name not in librariesimported:
        if infunction is True and pfile is not None:
            file8 = open(pfile,"a")
            file8.write("""
    """+"import "+ name)
            file8.close()
            librariesimported.append(name)
            return AINFUNCTION

        elif infunction is False and pfile is not None:
            file9 = open(pfile,"a")
            file9.write("""
"""+"import "+ name)
            file9.close()
            librariesimported.append(name)
            return True

        else:
            return FILENOTSPECIFIED
    else:
        return LIBRARYUSED


def delfile():
    if pfile is not None:
        os.remove(pfile)
        return True
    else:
        return FILENOTSPECIFIED


def newproject(name):
    global pfile
    if pfile is not None:
        return AINPROJECT
    else:
        file10 = open(""+name+".py", "w")
        file10.close()
        pfile = name+".py"
        return True


def comments(comment):
    if pfile != None:
        if infunction is True:
            file11 = open(pfile,"a")
            file11.write("""
    """+"#"+ comment)
            file11.close()
            return AINFUNCTION

        elif infunction is False:
            file12 = open(pfile,"a")
            file12.write("""
"""+"#"+comment)
            file12.close()
            return True

    else:
        return FILENOTSPECIFIED


def about():
    return ABOUT 


def removeliner(linenumber):
    if pfile is not None:
        a_file = open(pfile, "r")
        lines = a_file.readlines()
        a_file.close()
        linenumber = int(linenumber)
        linenumber -= 1
        del lines[linenumber]
        if lines[linenumber].startswith("def"):
            i_l = list(lines[linenumber].split())                                                              
            i_l.remove(i_l[0])                                                                            
            ncname = ''.join(i_l)
            ncname = ncname.replace("():","")
            functionsmade.remove(ncname)
            global infunction
            infunction = 0
            del lines[linenumber]
            return True
        else:
           del lines[linenumber]
        new_file = open(pfile, "w+")
        new_file.close()
        return True

    else:
        return False

def pfile_length(fname):
    i = 0
    with open(fname) as f:
            for i, l in enumerate(f):
                    pass
    return i + 1

def showcode():
    if pfile != None:
        length = pfile_length(pfile)
        endofpfile = 0
        file13 = open(pfile,"r")
        while length != endofpfile:
            endofpfile += 1
            print("Line "+str(endofpfile)+":")
            print(file13.readline())
        return True

    else:
        return False

def help():
    return commands

def appender(content):
    if infunction == True and pfile != None:
        file14 = open(pfile,"a")
        file14.write("""
    """+content)
        file14.close()
        return AINFUNCTION

    elif infunction == False and pfile != None:
        file15 = open(pfile,"a")
        file15.write("""
"""+content)
        file15.close()
        return True
    
    else:
        return FILENOTSPECIFIED




def status():
    if pfile != None:
        print("Python File = "+pfile+". You Have Made "+str(len(variablesmade))+" Variables And "+str(len(functionsmade))+" Functions, And You Imported "+str(len(librariesimported))+" Libraries.")
        print("*"*10)
        print("""
        Enter VV = To See Variables With Their Names And Values
        F = To See Functions Names
        LI = To See Libraries Imported Names
        R = To Return
        AL = To Add The Above Report To Your Python Log""")
        print("*"*10)
        user_input = input("> ")
        if user_input in semicommands:
            
            user_input_index = semicommands.index(user_input)

            if user_input_index == 0:
                print(len(variablesmade))
                if len(variablesmade) and len(variablesmadevalue) != 0:
                    lenvariablesnames = len(variablesmade)
                    global i
                    i = 0
                    while i != lenvariablesnames:
                        print(variablesmade[i]+" = "+variablesmadevalue[i])
                        i += 1
                        continue
                    
                    livecodingmain()
                
                else:
                    print("You Have Made No Variables.")
                    livecodingmain()
            
            elif user_input_index == 1:
                lenfunctionsmade = len(functionsmade)
                i = 0
                while i != lenfunctionsmade:
                    print(functionsmade[i])
                    i += 1

                livecodingmain()
            
            elif user_input_index == 2:
                librariesimportedlen = len(librariesimported)
                i = 0
                while i != librariesimportedlen:
                    print(librariesimported[i])
                    i += 1
                livecodingmain()

            elif user_input_index == 3:
                livecodingmain()
            
            elif user_input_index == 4:
                file20 = open("log.txt","a")
                file20.write("Python File = "+pfile+". You Have Made "+str(len(variablesmade))+" Variables And "+str(len(functionsmade))+" Functions, And You Imported "+str(len(librariesimported))+" Libraries.")
                file20.close()

        else:
            print("Not Successful")
            status()
    else:
        print("Not Successful")
        livecodingmain()








        
def livecodingmain():
    p_l = None
    if os.path.isfile(logmakefile):
        file = open(logmakefile,"a")


    else:
        file = open(logmakefile,"w")
        
    print("*"*10)
    print("Live Coding Version 2 Made By Sepehr Rasouli")
    print("To See Avalaible Commands Write Help.")
    print("*"*10)
    usrinput = input("> ")
    i_l = list(usrinput.split())
    #print(len(i_l))
    if len(i_l) == 2:
        p_l = list(i_l[1])                                                                  
        i_l.remove(i_l[1])                                                                            
        usrinput = ''.join(i_l)
        p_l = ''.join(p_l)

    elif len(i_l) == 3:
        listi = list(usrinput.split())
        usrinput = ''.join(listi[0])
        variablename = listi[1]
        variablevalue = listi[2]
    
    else: 
        listi = list(usrinput.split())
        usrinput = ''.join(listi[0])
        listi.remove(listi[0])
        content = ''.join(listi)
    
    
    if usrinput in commands:
        print("It Is In ")
        usrinput_index = commands.index(usrinput)
        if p_l is not None:
            usrinput = usrinput +" " +p_l
        else:
            usrinput = usrinput
        print(usrinput)
        if usrinput_index == 0:
            i_l = list(usrinput.split()) 
            print(i_l)                                                                 
            i_l.remove('openfile')                                                                            
            line = ''.join(i_l)
            openf = openfile(line)
            if openf == True:
                print("Successful")
                print(pfile)
                file.write("\n")
                file.write("Log : Correct Command With Command "+usrinput+" At Time "+str(datetime.datetime.now()))
                livecodingmain()
            else:
                file.write("\n")                
                file.write("Log : Wrong Command With Command "+usrinput+" At Time "+str(datetime.datetime.now())+" With Error Code "+openf)
                print("Not Successful")
                livecodingmain()

        if usrinput_index == 1:
            if pfile == None:
                file.write("\n")                
                print("Not Successful")
                file.write("Log : Wrong Command With Command "+usrinput+" At Time "+str(datetime.datetime.now())+" With Error Code NOTINFILE")
                livecodingmain()

            else:
                file.write("\n")                
                pfile == None
                print("Successful")
                file.write("Log : Correct Command With Command "+usrinput+" At Time "+str(datetime.datetime.now()))
                livecodingmain()
        
        if usrinput_index == 2:                                                                
            i_l = list(usrinput.split())                                                              
            i_l.remove(i_l[0])                                                                            
            linenumber = ''.join(i_l)
            lr = removeliner(linenumber)
            if lr == True:
                file.write("\n")                
                print("Successful")
                file.write("Log : Correct Command With Command "+usrinput+" At Time "+str(datetime.datetime.now()))
                livecodingmain()

            else:
                file.write("\n")                
                print("Not Successful")
                file.write("Log : Wrong Command With Command "+usrinput+" At Time "+str(datetime.datetime.now())+" With Error Code NOLINENUMBER")
                livecodingmain()

        if usrinput_index == 3:
            yon = input("Are You Sure You Want To Delete All Of Your Codes? [Y/N]")
            if yon == "Y":
                rm = removecode()
                if rm == True:
                    file.write("\n")                    
                    print("Successful")
                    file.write("Log : Correct Command With Command "+usrinput+" At Time "+str(datetime.datetime.now()))
                    livecodingmain()

                else:
                    file.write("\n")  
                    print("Not Successful")
                    file.write("Log : Wrong Command With Command "+usrinput+" At Time "+str(datetime.datetime.now())+" With Error Code "+rm)
                    livecodingmain()
            
            else:
                livecodingmain()

        if usrinput_index == 4:
            i_l = list(usrinput.split())                                                              
            i_l.remove(i_l[0])                                                                            
            fncname = ''.join(i_l)
            fmr = makefunction(fncname)
            if fmr == True:
                file.write("\n")  
                print("Successful")
                infunction = True
                file.write("Log : Correct Command With Command "+usrinput+" At Time "+str(datetime.datetime.now()))
                livecodingmain()

            else:
                file.write("\n")  
                print("Not Successful")
                file.write("Log : Wrong Command With Command "+usrinput+" At Time "+str(datetime.datetime.now())+" With Error Code "+fmr)
                livecodingmain()

        if usrinput_index == 5:
            ofnc = outfunction()
            if ofnc == True:
                file.write("\n")  
                print("Successful")
                file.write("Log : Correct Command With Command "+usrinput+" At Time "+str(datetime.datetime.now()))
                livecodingmain()


            else:
                file.write("\n")  
                print("Not Successful")
                file.write("Log : Wrong Command With Command "+usrinput+" At Time "+str(datetime.datetime.now())+" With Error Code "+ofnc)
                livecodingmain()

        if usrinput_index == 6:
            valm = makevariable(variablevalue,variablename)
            if valm == True or AINFUNCTION:
                file.write("\n")  
                print("Successful")
                file.write("Log : Correct Command With Command "+usrinput+" At Time "+str(datetime.datetime.now()))
                livecodingmain()

            else:
                file.write("\n")  
                print("Not Successful")
                file.write("Log : Wrong Command With Command "+usrinput+" At Time "+str(datetime.datetime.now())+" With Error Code "+valm)
                livecodingmain()

        if usrinput_index == 7:
            printc = printcommand(content)
            if printc == True or AINFUNCTION:
                file.write("\n")  
                print("Successful")
                file.write("Log : Correct Command With Command "+usrinput+" At Time "+str(datetime.datetime.now()))
                livecodingmain()

            else:
                file.write("\n")  
                print("Not Successful")
                file.write("Log : Wrong Command With Command "+usrinput+" At Time "+str(datetime.datetime.now())+" With Error Code "+printc)
                livecodingmain()

        if usrinput_index == 8:
            libimp = list(usrinput.split())
            libimp.remove(libimp[0])
            libraryimp = ''.join(libimp)
            libraryimport = importlibrary(libraryimp)
            if libraryimport == True or AINFUNCTION:
                file.write("\n")  
                print("Successful")
                file.write("Log : Correct Command With Command "+usrinput+" At Time "+str(datetime.datetime.now()))
                livecodingmain()


            else:
                print("Not Successful")
                file.write("\n")  
                file.write("Log : Wrong Command With Command "+usrinput+" At Time "+str(datetime.datetime.now())+" With Error Code "+libraryimport)
                livecodingmain()

        if usrinput_index == 9:
            seec = showcode()
            print(pfile)
            if seec == True:
                file.write("\n")  
                print("Successful")
                file.write("Log : Correct Command With Command "+usrinput+" At Time "+str(datetime.datetime.now()))
                livecodingmain()
            
            else:
                file.write("\n")  
                print("Not Successful")
                file.write("Log : Wrong Command With Command "+usrinput+" At Time "+str(datetime.datetime.now())+" With Error Code "+str(seec))
                livecodingmain()

        if usrinput_index == 10:
            if pfile != None:
                file.write("\n")  
                print("Successful")
                print("Result:")
                try:
                    exec(open(pfile).read())
                    file.write("Log : Correct Command With Command "+usrinput+" At Time "+str(datetime.datetime.now()))
                    livecodingmain()
                except:
                    file.write("\n")  
                    print("Not Successful")
                    file.write("Log : Wrong Command With Command "+usrinput+" At Time "+str(datetime.datetime.now())+" With Error Code "+seec)
                    livecodingmain()
            
            else:
                file.write("\n")  
                print("Not Successful")
                file.write("Log : Wrong Command With Command "+usrinput+" At Time "+str(datetime.datetime.now())+" With Error Code "+seec)
                livecodingmain()

        if usrinput_index == 11:
            if pfile != None:
                yon = input("Are You Sure You Want To Delete "+pfile + " ?")
                if yon == "Y":
                    delf = delfile()
                    if delf == True:
                        file.write("\n")  
                        print("Successful")
                        file.write("Log : Correct Command With Command "+usrinput+" At Time "+str(datetime.datetime.now()))
                        livecodingmain()

                    else:
                        file.write("\n")  
                        print("Not Successful")
                        file.write("Log : Wrong Command With Command "+usrinput+" At Time "+str(datetime.datetime.now())+" With Error Code "+delf)
                        livecodingmain()

                else:
                    livecodingmain()
        
        if usrinput_index == 12:
            name = list(usrinput.split())
            name.remove(name[0])
            name = ''.join(name)
            print("Exiting "+pfile+ " And entering "+name)
            
            if os.path.isfile(name+".py"):

                file.write("\n")  
                print("Not Successful")
                file.write("Log : Wrong Command With Command "+usrinput+" At Time "+str(datetime.datetime.now())+" With Error Code FILEEXISTS")
                livecodingmain()

            else:
                file111 = open(name+".py","w")
                file111.close()
                openfile(name)
                file.write("\n")  
                print("Successful")
                file.write("Log : Correct Command With Command "+usrinput+" At Time "+str(datetime.datetime.now()))
                livecodingmain()

        if usrinput_index == 13:
            ab = about()
            print(ab)
            livecodingmain()

        if usrinput_index == 14:
            print("Will be added in next update...")
            livecodingmain()

        if usrinput_index == 15:
            comm = list(usrinput.split())
            comm.remove(comm[0])
            comm = ''.join(comm)
            comments(comm)
            if comments == True or AINFUNCTION:
                file.write("\n")  
                print("Successful")
                file.write("Log : Correct Command With Command "+usrinput+" At Time "+str(datetime.datetime.now()))
                livecodingmain()
            
            else:
                file.write("\n")  
                print("Not Successful")
                file.write("Log : Wrong Command With Command "+usrinput+" At Time "+str(datetime.datetime.now())+" With Error Code "+comm)
                livecodingmain()
            
        if usrinput_index == 16:
            name = list(usrinput.split())
            name.remove(name[0])
            name = ''.join(name)
            app = appender(name)
            if app == True or AINFUNCTION:
                file.write("\n")  
                print("Successful")
                file.write("Log : Correct Command With Command "+usrinput+" At Time "+str(datetime.datetime.now()))
                livecodingmain()
            else:
                file.write("\n")  
                print("Not Successful")
                file.write("Log : Wrong Command With Command "+usrinput+" At Time "+str(datetime.datetime.now())+" With Error Code "+str(app))
                livecodingmain()
            
        if usrinput_index == 17:
            hel = help()
            print(hel)
            livecodingmain()

        if usrinput_index == 18:
            status()
    else:
        print("Not Successful")
        livecodingmain()
livecodingmain()









