import time
import random
import array
import colorama
from colorama import Fore, Style
import os
import sys
import tqdm
from tqdm import tqdm
import ctypes
import pymsgbox

os.system('cls')
time.sleep(1)
print(Fore.LIGHTMAGENTA_EX + "Running Barbara - Version: Public | C. 2021 | Developed by Enortis The Great")
time.sleep(3)
pymsgbox.alert('You need an access key in order to access Barbara.\n Code: 888sf77-T!', 'WARNING!')
response = pymsgbox.prompt('Please enter the access key:')
if response == "PublicRelease":
    pass
else:
    pymsgbox.alert('Key failed, closing program.\n[EXIT CODE: 992-4f]', 'Fatal Error!')
    for q in tqdm(range(100),
                  desc = Fore.RED + "Failure to authenticate...",
                  ascii= False,
                  ncols= 75):
        time.sleep(0.03)
    os.system('pause')
    exit()
time.sleep(1)
os.system('cls')
time.sleep(1)
print("""
><<        ><<     ><<<<<<<<     ><<               ><<            ><<<<          ><<       ><<     ><<<<<<<<
><<        ><<     ><<           ><<            ><<   ><<       ><<    ><<       >< ><<   ><<<     ><<      
><<   ><   ><<     ><<           ><<           ><<            ><<        ><<     ><< ><< > ><<     ><<      
><<  ><<   ><<     ><<<<<<       ><<           ><<            ><<        ><<     ><<  ><<  ><<     ><<<<<<  
><< >< ><< ><<     ><<           ><<           ><<            ><<        ><<     ><<   ><  ><<     ><<      
>< ><    ><<<<     ><<           ><<            ><<   ><<       ><<     ><<      ><<       ><<     ><<      
><<        ><<     ><<<<<<<<     ><<<<<<<<        ><<<<           ><<<<          ><<       ><<     ><<<<<<<<
""")
for cutie in range(20):
    os.system('color 4')
    time.sleep(0.1)
    os.system('color 7')
time.sleep(1)
usr = input(Fore.LIGHTMAGENTA_EX + "Please enter the username you would like to use for this session: ")
if usr == "":
    pass
else:
    pass
time.sleep(1)
print(Fore.LIGHTGREEN_EX + "Welcome, " + usr)
time.sleep(1)
pss = input(Fore.LIGHTMAGENTA_EX + "Please enter the password you would like to use for this session: ")
if pss == "":
    pass
else:
    pass
time.sleep(1)
pymsgbox.alert('Authentication in progress.', 'AUTH')
response1 = pymsgbox.prompt('Enter your credentials in the format "username:password" in the box below: ')
if response1 == usr + ":" + pss:
    pass
else:
    print(Fore.RED + "Authentication failed, Closing.")
    time.sleep(1)
    exit()
time.sleep(1)
print(Fore.LIGHTGREEN_EX + "Hello again, " + usr)
time.sleep(1)
answer = True
while answer:
    question = input(Fore.LIGHTCYAN_EX + "Hello, I am Barbara. Ask me a 'yes' or 'no' question: ")
    answers = random.randint(1, 8)
    f = open("barbararesponses.txt", "a")
    f.write("[Q]: " + question + " [A]: " + str(answers) + "\n")

    if question == "":
        print(Fore.LIGHTBLUE_EX + "Thank you for playing! Goodbye!")
        time.sleep(1)
        os.system('pause')
        sys.exit()

    elif answers == 1:
        print(Fore.LIGHTGREEN_EX + "[!] Without a doubt bro.")
        time.sleep(1)

    elif answers == 2:
        print(Fore.LIGHTGREEN_EX + "[!] Absolutely!")
        time.sleep(1)

    elif answers == 3:
        print(Fore.LIGHTGREEN_EX + "[!] Uhhhh yeah.")
        time.sleep(1)

    elif answers == 4:
        print(Fore.YELLOW + "[/!\] ask me later homie.")
        time.sleep(1)

    elif answers == 5:
        print(Fore.YELLOW + "[/!\] Come on, ask me later.")
        time.sleep(1)

    elif answers == 6:
        print(Fore.YELLOW + "[/!\] Dude, really? Ask me later bro.")
        time.sleep(1)

    elif answers == 7:
        print(Fore.LIGHTRED_EX + "[0] Lol no.")
        time.sleep(1)

    elif answers == 8:
        print(Fore.LIGHTRED_EX + "[0] NOOOOPPPEEEEE.")
        time.sleep(1)

    elif answers == 9:
        print(Fore.LIGHTRED_EX + "[0] Dude no shut up please.")
        time.sleep(1)

    elif answers == 10:
        print(Fore.WHITE + "[1] *PSST* I can't tell you that one.")
        time.sleep(1)

    elif answers == 11:
        print(Fore.WHITE + "[1] Ye- just kidding. I would never tell you lol.")
        time.sleep(1)

    elif answers == 12:
        print(Fore.WHITE + "[1] N- just kidding. I would never tell you lol.")
        time.sleep(1)
