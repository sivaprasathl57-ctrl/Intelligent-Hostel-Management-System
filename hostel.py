import time
import hashlib
import getpass
from colorama import Fore
import pyttsx3
# ********************************************************************************************
class Warden:
    def __init__(self,name,age,studies,Block):
        self.name=name
        self.age=age
        self.studies=studies
        self.Block=Block
class register(Warden):
        def __init__(self,name,age,studies,Block):
            super().__init__(name,age,studies,Block)
        def display(self):
            print("Warden Name:  ",self.name)
            print("Warden Age:   ",self.age)
            print("Qualification:",self.studies)
            print("Enter the Block: ",self.Block)
            print(" Suscessfully Register ")
            print("*************************************")
# *********************************************************************************************
class student:
    def __init__(self,name,age,dept,block,room):
        self.name=name
        self.age=age
        self.dept=dept
        self.block=block
        self.room=room
class registerstud(student):
    def __init__(self,name,age,dept,block,room):
        super().__init__(name,age,dept,block,room)
        print("✅Registered Successfully")
    def view_data(self):
         
         print("Student Name: ",self.name)
         print("Age:      ",self.age)
         print("Department: ",self.dept)
         print("Block : ",self.block)
         print("Room No: ",self.room)
         print("-------------------------------------------")
# ************************************************************************************************
boy=[]
girl=[]
free=[]
user = {}
g=[]
r=None
engine = pyttsx3.init()

engine.say("Welcome to IHMS, the Intelligent Hostel Management System.")
engine.say("This system helps manage hostel security, user access, and monitoring efficiently.")

engine.runAndWait()
# ***********************************************************************************************
while True:
    print(Fore.GREEN+"🔐  Login")
    print("🔍  Register")
    print("📁  view Registered Data(View)")
    print("=======================================")
    r=input("⚙️ Your Choice: ").lower()
    if r == "login":
        a=3
        while 0<a:
            n=input("Enter Username: ")
            m=getpass.getpass("Enter Password: ")
            hash = hashlib.sha256(m.encode()).hexdigest()
            if n in user and user[n] == hash:
                print("👍  Login Sucessfully  🎉🥳")
                engine = pyttsx3.init()
                engine.say("Access Granded")
                engine.say("Welcome to the System")
                engine.runAndWait()
                print("==============================================")
                print("        IHMS CYBER SECURITY TERMINAL")
                print("==============================================")
                time.sleep(1)
                print("> 💀  Initializing System ",end="")
                for i in range(5):
                    print(".",end="",flush=True)
                    time.sleep(0.5)
                print("\n> 👾  Connecting to Hostel Database",end="")
                for i in range(5):
                    print(".",end="",flush=True)
                    time.sleep(0.5)
                print("\n> 🤖  Verifying Student Records",end="")
                for i in range(5):
                    print(".",end="",flush = True)
                    time.sleep(0.5)
                print("\n>                  🧬 ACCESS GRANDED 🔥",end = "",)
                for i in range(10):
                    print(".",end="",flush = True)
                    time.sleep(1)
                print(Fore.GREEN+ """
██╗██╗  ██╗███╗   ███╗███████╗
██║██║  ██║████╗ ████║██╔════╝
██║███████║██╔████╔██║███████╗
██║██╔══██║██║╚██╔╝██║╚════██║
██║██║  ██║██║ ╚═╝ ██║███████║
╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝

""")

                print("INTELLIGENT HOSTEL MANAGEMENT SYSTEM")
                print("\033[0m")
                print("`````````````````````````````````````")
                print(Fore.GREEN+"1.Warden")
                print("2.Student")
                print("3.exit")
                print("`````````````````````````````````````")
                s=int(input("Enter your Choice: "))
# ****************************************************************************************
                if s == 1:

                    while True:
                        print("=============")
                        print("1.Register")
                        print("2.View Data")
                        print("3.Exit")
                        print("=============")
                        a=input("Enter Your Choice: ")
                        if a == "1":
                            print("Working.......")
                            time.sleep(5)
                            n=input("Enter the Warden Name: ")
                            m=int(input("Enter the Warden Age: "))
                            q=input("Qualification: ")
                            w=input("Enter Your Block: ")
                            r=register(n,m,q,w)
                        elif a == "2":
                            print("Wait a Second....")
                            time.sleep(2)
                            if r is not None:
                                r.display()
                            else:
                                print("❌  No data is avaiable")
                        elif a=="3":
                            print("🚨  See You Next Time")
                            break
                        else:
                            print("🚫  Invalid Option")
# *******************************************************************************
                elif s == 2:
                    print("1. Male")
                    print("2. Female")
                    s=input("Enter Your Male or Female: ").lower()
                    if s == "male":
                        print("Avaiable Blocks")
                        print("A  B  C  D  E  F")
                        while True:
                            print("1. Register")
                            print("2. View Data")
                            print("3. search Student")
                            print("4. Total Boys")
                            print("5. Delete a Student")
                            print("6. Exit")
                            z=int(input("Enter Your Options:  "))
                            if z == 1:
                                a=input("Enter the Boy Name: ")
                                b=int(input("Enter Your Age: "))
                                c=input("Enter Your Department: ")
                                f=input("Enter Your Block: ")
                                d=int(input("Enter Your Room No: "))
                                    
                                r=registerstud(a,b,c,f,d)
                                boy.append(r)
                                
                                n=43
                                b=0
                                for i in boy:
                                    if r.block == f:
                                        b+=1
                                if b>=n:
                                    print("⚠️  Block is Full")
                                count=0 
                                for r in boy:
                                    if r.block==f and r.room==d:
                                        count+=1
                                if count>=4:
                                    print("⚠️   Room Already Full")
                                    for i in range(1,n):
                                        if i == d:
                                            continue
                                        free.append(i)
                                
                                    print("Avaiable Rooms",end="")
                                    for i in range(7):
                                        print(".",end="",flush=True)
                                        time.sleep(0.5)
                                    print(free)
                                
                            elif z == 2:
                                for ee in boy:
                                    ee.view_data()
                            elif z == 3:
                                x=input("Enter a Searching Name:  ").lower()
                                print("🚀  Analysing Data",end="")
                                for i in range(7):
                                    print(".",end="",flush=True)
                                    time.sleep(1)
                                for r in boy:
                                    if r.name == x:
                                        print("Name: ",a)
                                        print("Agr:",b)
                                        print("Department:",c)
                                        print("Room Number:",d)
                                        print("Block:",f)

                                    else:
                                        print("No Student Found")
                            elif z == 4:
                                print("Total Boys Registered: ",len(boy))
                            elif z == 5:
                                m=input("Enter Name to Remove: ")
                                for s in boy:
                                    if s.name == m:
                                        boy.remove(s)
                                        print("👍  Student Removed Successfully")
                                        break
                                    else:
                                        print("❌  Student Not Found")
                            elif z == 6:
                                print("You are Getting Back")
                                break
                            else:
                                print("Invalid Options")
# *********************************************************************************************
                    elif s == "female":
                        print("Avaiable Blocks")
                        print("A  B  C  D")
                        while True:
                            print("1. Register")
                            print("2. View Data")
                            print("3. Search Student")
                            print("4. Total Girls Registered")
                            print("5. Remove the Student")
                            print("6. Exit")
                            p=int(input("Enter Your Choice: "))
                            if p == 1:
                                a=input("Enter the Girl Name: ") 
                                b=int(input("Enter Your Age: "))
                                c=input("Enter Your Department: ")
                                f=input("Enter Your Block: ")
                                d=int(input("Enter Your Room No: "))
                                m=registerstud(a,b,c,f,d)
                                girl.append(m)
                                n=43
                                b=0
                                for i in girl:
                                    if m.block == f:
                                        b+=1
                                if b>=n:
                                    print("⚠️  Block is Full")
                                count=0 
                                for r in girl:
                                    if m.block==f and m.room==d:
                                        count+=1
                                if count>=4:
                                    print("⚠️  Room Already Full")
                                    for i in range(1,n):
                                        if i == d:
                                            continue
                                        g.append(i)
                                    print("Avaiable Rooms",end="")
                                    for i in range(7):
                                        print(".",end="",flush=True)
                                        time.sleep(0.5)
                                    print(free)
                                else:
                                    r=registerstud(a,b,c,f,d)
                                    boy.append(r)
                            elif p == 2:
                                for ee in girl:
                                    ee.view_data()
                            elif p == 3:
                                j=input("Enter You Search Name: ").lower()
                                for m in girl:
                                    if m.name == j:
                                            print("Name: ",a)
                                            print("Agr:",b)
                                            print("Department:",c)
                                            print("Room Number:",d)
                                            print("Block:",f)
                                            print("************************************")
                            elif p == 4:
                                print("Total Girls Registered: ",len(girl))
                            elif p == 5:
                                m=input("Enter Name to Remove: ")
                                for s in girl:
                                    if s.name == m:
                                        girl.remove(s)
                                        print("👍  Student Removed Successfully")
                                        break
                                    else:
                                        print("❌  Student Not Found")
                            elif p== 6:
                                print("❌  Getting Back..........")
                                break
                            else:
                                print("❌  Invalid Options")
        
                elif s== 3:
                    print("Thank you🥳")
                    break
                else:
                    print("❌  Invalid Option")
            else:
                a=a-1
                engine=pyttsx3.init()
                engine.say("Try Again")
                engine.runAndWait()
                print("💀  Invalid Username or Password...")
                
            if a == 0:
                print("💀💀💀  You have failed too Many Account")
                print("🤖  You have been Locked for 1 minutes",end="")
                for i in range(60):
                    print(".",end = " ",flush=True)
                    time.sleep(1)
                
                
        
    elif r == "register":
        print("*******************************")
        n = input("Create Username: ")
        m = input("Create Password: ")
        print("*******************************")
        
        hash = hashlib.sha256(m.encode()).hexdigest()
        user[n]=hash
        print("⚡ Register Successful")
    elif r == "view":
        print(user)
        print("````````````````````````````````````````````````````````````````````````")
        print("small challenge guess how to convert to plain text in the manuval way")
        print("````````````````````````````````````````````````````````````````````````")
    