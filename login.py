import gen
import json
import pyperclip as pc
import os

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self, f_name, m_name, l_name, email):
        self.email = email
        self.f_name = f_name
        self.m_name = m_name
        self.l_name = l_name
        guid = gen.generateGUID()
        data = {"guid": guid, "email": self.email, "username": self.username, "password": self.password, "last_name": self.l_name, "first_name": self.f_name, "m_name": self.m_name}
        f = open(f"data/{self.username}.json", "w")
        json.dump(data, f, indent=2)
        f.close()
    
    def login(self):
        print(" ")
        print("===========================================================")
        print(f"Logged in as {self.username}")
        print("===========================================================")
        print(" ")
        while True:
            path = os.getcwd()
            path_name = f"{self.username}.json"
            found = False
            for root, dirs, files in os.walk(path):
                if path_name in files:
                    found = True
            if found == False:
                break
            index = input("Would you like to edit your information: ")
            if index == "no" or index == "n" or index == "quit" or index == "q":
                break
            if index == "yes" or index == "y":
                with open(f"data/{self.username}.json") as file:
                    data = json.load(file)
                    username = data["username"]
                    password = data["password"]
                    email = data["email"]
                    f_name = data["first_name"]
                    m_name = data["m_name"]
                    l_name = data["last_name"]
                    print(" ")
                    print("===========================================================")
                    print(f"Email: {email}\nUsername: {username}\nPassword: {password}\nFirst Name: {f_name}\nMiddle Name: {m_name}\nLast Name: {l_name}\n\nDelete Account")
                    print("===========================================================")
                    print(" ")
                index = input("Edit: ").lower()
                if index == "email":
                    while True:
                        email = input("New Email: ")
                        if email == "quit" or email == "q":
                            break
                        elif email == data["email"]:
                            print("You are already using that email.")
                        elif "@" not in email:
                            print("Not a valid email")
                        else:
                            with open(f"data/{self.username}.json", "r+") as file:
                                data = json.load(file)
                                data["email"] = email
                                file.seek(0)
                                json.dump(data, file, indent=2)
                                file.truncate()
                                print(f"Email Changed to {email}, Succesfully!")
                                break
                elif index == "username":
                    pass
                elif index == "password":
                    while True:
                        password = input("New Password: ")
                        if password == "quit" or password == "q":
                            break
                        elif password == data["password"]:
                            print("You are already using that password.")
                            continue
                        else:
                            with open(f"data/{self.username}.json", "r+") as file:
                                data = json.load(file)
                                data["password"] = password
                                file.seek(0)
                                json.dump(data, file, indent=2)
                                file.truncate()
                                print(f"Email Changed to {password}, Succesfully!")
                                break
                elif index == "first name" or index == "firstname" or index == "name":
                    while True:
                        f_name = input("New First Name: ")
                        if f_name == "quit" or f_name == "quit":
                            break
                        elif f_name == data["first_name"]:
                            print(f"You are already using the name: {f_name}.")
                            continue
                        else:
                            with open(f"data/{self.username}.json", "r+") as file:
                                data = json.load(file)
                                data["first_name"] = f_name
                                file.seek(0)
                                json.dump(data, file, indent=2)
                                file.truncate()
                                print(f"First name changed to {f_name}, succesfully!")
                                break
                elif index == "middle name" or index == "middlename" or index == "mname":
                    while True:
                        m_name = input("New Middle Name: ")
                        if m_name == "quit" or m_name == "quit":
                            break
                        elif m_name == data["m_name"]:
                            print(f"You are already using the name: {m_name}.")
                            continue
                        else:
                            with open(f"data/{self.username}.json", "r+") as file:
                                data = json.load(file)
                                data["m_name"] = m_name
                                file.seek(0)
                                json.dump(data, file, indent=2)
                                file.truncate()
                                print(f"Middle name changed to {m_name}, succesfully!")
                                break
                elif index == "last name" or index == "lastname" or index == "lname":
                    while True:
                        l_name = input("New Last Name: ")
                        if l_name == "quit" or l_name == "quit":
                            break
                        elif l_name == data["last_name"]:
                            print(f"You are already using the name: {l_name}.")
                            continue
                        else:
                            with open(f"data/{self.username}.json", "r+") as file:
                                data = json.load(file)
                                data["last_name"] = l_name
                                file.seek(0)
                                json.dump(data, file, indent=2)
                                file.truncate()
                                print(f"Middle name changed to {l_name}, succesfully!")
                                break
                elif index == "delete account" or index == "deleteaccount":
                    while True:
                        deleteAccount = input("Are you sure you want to delete your account: (y/n) ")
                        if deleteAccount == "yes" or  deleteAccount == "y":
                            os.remove(f"data/{username}.json")
                            break
                        elif deleteAccount == "no" or deleteAccount == "n":
                            break
                        else:
                            print("Not a valid response")
                            continue
                else:
                    print("Not a valid response.")
                    continue

while True:
    
    index = input("Register or Login: ").lower()
    if index == "quit" or index == "q":
        quit()
    
    elif index == "register":

        f_name = input("Name: ")

        m_name = input("Middle name or N/A: ")
        if m_name == "N/A":
            m_name = ""

        l_name = input("Last name: ")

        email = input("Email: ")
        if "@" not in email:
            print("Error")
            continue
            
        while True:
            username = input("Username: ").lower()
            if username == "quit" or username == "q":
                print(f"The username, {username} is not permitted.")
                continue
            else:
                path = os.getcwd()
                path_name = f"data/{username}.json"
                found = False
                for root, dirs, files in os.walk(path):
                    if path_name in files:
                        found = True
                if found == True:
                    print(f"{username} has already been taken, please use a different username.")
                    continue
                if found == False:
                    break

        password = input("Password: would you like one generated for you? (y/n) ")
        if password == "y" or password == "yes":
            password = gen.generatePW()
            pc.copy(password)
            print("Password copied to clipboard")
        elif password == "n" or password == "no":
            password = input("Password: ")
        else:
            print("Error")
            continue
        
        login = Login(username, password)
        login.register(f_name, m_name, l_name, email)
        
    if index == "login":
        while True:
            username = input("Username: ").lower()
            if username == "q" or username == "quit":
                quit()
            else:
                path = os.getcwd()
                path_name = f"{username}.json"
                found = False
                for root, dirs, files in os.walk(path):
                    if path_name in files:
                        found = True
                if found == True:
                    break
                if found == False:
                    print(f"{username} does not exist, please try again or create an account")
                    continue

        while True:
            password = input("Password: ")
            with open(f"data/{username}.json") as file:
                data = json.load(file)
                if password != data["password"]:
                    print("Incorrect password, try again!")
                    continue
                else:
                    break    
        login = Login(username, password)
        login.login()
            

