
#WARNING: THIS PROJECT IS STILL IN PRODUCTION.
import logging
from bs4 import BeautifulSoup
from googlesearch import search
import re
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Log


def logger(error):
    with open("log.txt","w") as f:
        f.write("\n"+str(error))
        f.close()


    
driver = webdriver.Firefox(executable_path="PATH")

class Extractor:
    global driver
    def extract_page_links(userText):
        try:
            f = open(userText,"r")

        except Exception as inst:
            logger(inst)
            SystemExit


        f = f.readlines()
        f = [x.strip() for x in f]
        
        rest = open("result.txt","w")
        pagelinkslist = []
        for element in f:
            try:
                ret = requests.get(element)

            except Exception as inst:
                logger(inst)
                SystemExit

            # use html.parser on returned request text
            soup = BeautifulSoup(ret.text, 'html.parser') 
            for link in soup.find_all('a'):
                c = link.get('href')
                try:
                    if c.startswith("https://"):
                        rest.write("\n"+c)
                        pagelinkslist.append(c)

                    if c.startswith("/"):
                        rest.write("\n"+element+c)
                        pagelinkslist.append(c)

                    else:
                        pass

                except Exception as inst:
                    logger(inst)
                    SystemExit

        return pagelinkslist




    def extract_emails(userText):

        try:
            f = open(userText,"r")

        except Exception as inst:
            logger(inst)
            SystemExit

        f = f.readlines()
        f = [x.strip() for x in f]
        c = open("data.txt","w",encoding="utf-8",errors='ignore')
        c.write(" ")
        for url in f:

            try:
                driver.get(f"{url}")

            except Exception as inst:
                logger(inst)
                SystemExit

            sourcedata = driver.page_source

            c = open("data.txt","a",encoding="utf-8",errors='ignore')
            c.write("\n\n\n"+sourcedata)


        EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
        emails = []
        c = open("data.txt","r")
        for code in c.readlines():
            for re_match in re.finditer(EMAIL_REGEX,code):
                if re_match.group() and re_match.group() not in emails:
                    emails.append(re_match.group())
        
        return emails


    def extract_google_search(query,size):
        pp = []
        link_regex = r"""([a-z][a-z0-9+\-.]*:(//[^/?#]+)?)?"""
        c = open("subjects.txt","r")
        c = c.readlines()
        for query in c:
            for link in search(query,num_results=100):
                for re_match in re.finditer(link_regex,link):
                    if re_match.group():
                        pp.append(re_match.group()) 


        return pp


class Main:
    def main():
        print("Welcome.")
        print('''
        1 - Extract Page Links  
        2- Extract Emails 
        3- Extract Site Links From Google Search.''')
        userInput = input('> ')
        if userInput == '1':
            print("""Extract Page Links. Name of the text file Containing Urls?
            *NOTE : Start the URL with https://www. or http://www. Otherwise you will get an error :(""")
            userText = input("> ")
            extractor = Extractor
            if userText.endswith(".txt"):
                retdata = extractor.extract_page_links(userText)  
            else:
                userText += ".txt"
                retdata = extractor.extract_page_links(userText)
            #TODO: Add Errors.
            callmain = Main
            callmain.main()

        if userInput == '2':
            print("""Extract Emails. Name of the text file Containing Urls?
            *NOTE : Start the URL with https://www. or http://www. Otherwise you will get an error""")
            userText = input("> ")
            extractor = Extractor
            if userText.endswith(".txt"):
                retdata = extractor.extract_emails(userText)  
            else:
                userText += ".txt"
                retdata = extractor.extract_emails(userText)
            #TODO: Add Errors. and print each element one by one
            print(retdata)
            callmain = Main
            callmain.main()


        if userInput == '3':
            print("Extract Page Links From Google Search. Name of the text file Contatining Subjects?")
            userSubject = input("> ")
            print("How Many ? *The Bigger The Number Gets , The Slower The Proccess Gets.*")
            userQuanity = input("> ")
            extractor = Extractor
            retdata = extractor.extract_google_search(userSubject,userQuanity)
            print("Page Links : ")
            for element in retdata:
                print(element)
            callmain = Main
            callmain.main()

        else:
            print("Wrong Command.")
            callmain = Main
            callmain.main()





callmain = Main
callmain.main()