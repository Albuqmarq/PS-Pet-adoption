import os
from pet_adoption_plataform import adoption

class Base:
    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def search_name_in_list(nome, lista):
        for i in lista:
            if i.name.lower() == nome.lower():
                return i
        return None

    @staticmethod
    def showlist(lista):
        for i in lista:
            print(f"{i.name}")
    
    @staticmethod
    def search():
        pass

    @staticmethod
    def filters(list, fltrs, sps):
        #cria um dicionario novo para armazenar os itens selecionados
        newlist = []

        for i in list:
            if str(getattr(i, fltrs)).lower() == sps.lower():
                newlist.append(i)

        print(f"{len(newlist)} pets available!")
        
        #retorna o novo dicionario
        return newlist

class PetFactory:
    @staticmethod
    def create_pet(pet_type, shelter):
        """Factory method para criação de pets com validações"""
        name = input("Name: ")
        age = input("Age: ")
        gender = input("Gender: ")
        color = input("Color: ")
        size = input("Size: ")
        
        # Validações básicas
        if not name or not age.isdigit() or int(age) <= 0:
            raise ValueError("Invalid pet data")
            
        # Poderíamos ter lógica específica para diferentes tipos de pets
        if pet_type.lower() == "exotic":
            print("Special care instructions for exotic pets:")
            special_care = input("Enter special care requirements: ")
        
        return Pet(name, age, gender, color, size, pet_type, shelter, adopted=False)


class Shelter(Base):
    def __init__(self, name, local, email, phone, pets, us):
     self.name = name
     self.local = local
     self.email = email
     self.phone = phone
     self.pets = int(pets)
     self.us = us   

    def show_info(self):
        print(f"Name:{self.name}")
        print(f"Local:{self.local}")
        print(f"Email:{self.email}")
        print(f"Phone:{self.phone}")
        print(f"Pets:{self.pets}")
        print(f"Us:{self.us}\n")
class User(Base):
    def __init__(self, name, password, age, address, email):
        super().__init__(name)
        self.__password = password
        self.age = int(age)
        self.address = address
        self.email = email
        self.__logged = False

    
    def getpassword(self):
        return self.__password
    
    def changepassword(self, new):
        self.__password = new

    def getlogin(self):
        return self.__logged

    def login(self, name, password):
        if (name != self.name) | (password != self.getpassword()):
            self.__logged == False
            print("Wrong username or password")
        else:
            self.__logged = True

    def search_name_in_list(name, list):
        for i in list:
            if i.name == name:
                return i
        return None

    def show_info(self):
        if self.__logged == True:
            print(f"Name:{self.name}")
            print(f"Age: {self.age}")
            print(f"Email: {self.email}")
            print(f"Address: {self.address}")
    
    @classmethod
    def creat(cls):
        name = input("Type your name: ").capitalize()
        password = input("Type your password: ")
        age = int(input("Type your age: "))
        while age == 0 or age > 99:
            age = int(input("Type a valid age: "))
        address = input("Type your adress: ")
        email = input("Type your email: ")

        return cls(name, password, age, address, email)
    
    def adoption_process(self, pets):
        while True:
            
            os.system("cls")

            filter_pets = Pet.filters(pets, "adopted", "False")

            filter_pets = Pet.search(filter_pets)

            os.system("cls")

            Pet.showlist(filter_pets)

            print("See more informations? y/n")
            info = input().lower()

            if info == "y":
                print("Enter the name of the pet you want to see: ")
                pet_choiced = input().lower().capitalize()
                paw_info = Pet.search_name_in_list(pet_choiced, pets)
                
                if paw_info == None:
                    input("Pet dont found")
                    continue
                
                os.system("cls")

                paw_info.show_info()

                print("--Want to adopt this pet? (1)\n--Return (2)\n--Exit (3)")
                
                choice = input()
                
                if choice == "2":
                    continue

                elif choice == "1":
                    adoption.adoption(paw_info, paw_info.shelter)
                    break
                elif choice == "3":
                    break
            elif info != "n":
                continue
            else:
                break

    def changers(self):
        if input("Change your name? y/n: ").lower() == "y":
            self.name = input("Type your name: ").capitalize()
        if input("Change your password? y/n").lower() == "y":
            new_password = input("Type your password")
            self.changepassword(new_password)
        if input("Change your age? y/n: ").lower() == "y":
            self.age = int(input("Type your age: "))
            while self.age == 0 or self.age > 99:
                    self.age = int(input("Type a valid age: "))
        if input("Change adress? y/n: ").lower() == "y":
            self.address = input("Type your adress:")
        if input("Change email? y/n: ").lower() == "y":
            self.email = input("Type your email: ")

class Shelter_user(User):
    def __init__(self, name, password, address, email, shelter):
        super().__init__(name, password, age = 0, email=email, address=address)
        del self.age
        self.shelter = shelter

    def show_info(self):
        if self.getlogin() == True:
            print(f"Name:{self.name}")
            print(f"Email: {self.email}")
            print(f"Address: {self.address}")

    def adoption_process(self, pets):
        while True:
            print("--Add pet(1)\n--Remove pet(2)\n--Return (3)")
            choice = input()
            
            if choice == '1':
                print("Select pet type (dog/cat/exotic): ")
                pet_type = input().lower()
                try:
                    new_pet = PetFactory.create_pet(pet_type, self.shelter)
                    pets.append(new_pet)
                except ValueError as e:
                    print(f"Error creating pet: {e}")
                    input("Press any key to continue")

    

class Pet(Base):
    def __init__(self, name, age, gender, color, size, type, shelter, adopted: bool):
        super().__init__(name)
        self.age = age
        self.gender = gender
        self.color = color
        self.size = size        
        self.type = type
        self.shelter = shelter
        self.shelter_name = shelter.name
        shelter.pets += 1
        self.adopted = adopted

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"color: {self.color}")
        print(f"type: {self.type}")
        print(f"Size: {self.size}")
        print(f"shelter: {self.shelter.name}\n")
        
    @staticmethod
    def create(shelter):
        name = input("Name:")
        age = input(f"age:")
        gender = input(f"Gender:")
        color = input(f"color:")
        type = input(f"type:")
        size = input(f"Size:")
        return Pet(name, age, gender, color, size, type, shelter, adopted=False)


    @staticmethod
    def search(list):
        print("Apply filters? y/n")
        choice = input().lower()
        while choice != "n" and choice != "y":
            print("Wrong comand try again:")
            choice = input().lower()
        while choice == "y":
            os.system("cls")

            while True:  
            
                print("What kind of filter?\n--Type\n--Color\n--Size\n--Gender")
                fltrs = input()

                if fltrs.lower() == "color":
                    os.system("cls")
                    print("What kind of color?")
                    color = []
                    for i in list:
                        color.append(getattr(i, "color").capitalize())
                        
                    color = set(color)
                    for j in color:
                        print(f"--{j}")

                    
                    spc = input().capitalize()
                    if spc not in color:
                        spc = input("Filter not found, try again!")
                    break

                if fltrs.lower() == "type":
                    os.system("cls")
                    print("What kind of type?")
                    tpe = []
                    for i in list:
                        tpe.append(getattr(i, "type").capitalize())
                        
                    tpe = set(tpe)
                    for j in tpe:
                        print(f"--{j}")

                    
                    spc = input().capitalize()
                    if spc not in tpe:
                        spc = input("Filter not found, try again!")
                    break
                if fltrs.lower() == "size":
                    os.system("cls")
                    print("What kind of Size?")
                    size = []
                    for i in list:
                        size.append(getattr(i, "size").capitalize())
                    size = set(size)
                    for j in size:
                        print(f"--{j}")
                    
                    spc = input().capitalize()
                    while spc not in size:
                        spc = input("Filter not found, try again!")
                    break
                if fltrs.lower() == "gender":
                    os.system("cls")
                    print("What kind of gender?")
                    gender = []
                    for i in list:
                        gender.append(getattr(i, "gender").capitalize())
                        
                    gender = set(gender)
                    for j in gender:
                        print(f"--{j}")
                    
                    spc = input().capitalize()
                    if spc not in gender:
                        spc = input("Filter not found, try again!")
                    break
                else:
                    os.system("cls")
                    print("Filter not found, try again!")

                spc = spc.strip().lower()
                fltrs = fltrs.strip().lower()

            list = Pet.filters(list, fltrs, spc)
            if len(list) > 1:
                print("Apply another filter? y/n")
                choice = input().lower()
                while choice != "n" and choice != "y":
                    print("Wrong comand try again:")
                    choice = input().lower()
            elif len(list) == 0:
                print("No results")
                break
            elif len(list) == 1:
                choice == "n"
                break
        return list
    
    def stories(self, storie):
        self.storie = storie
        
class Event(Base):
    def __init__(self, name, local, date, open, close, type):
        super().__init__(name)
        self.local = local
        self.date = date
        self.open = open
        self.close = close
        self.type = type

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Local: {self.local}")
        print(f"Date: {self.date}")
        print(f"Open: {self.open}")
        print(f"Close: {self.close}")
        print(f"Type: {self.type}")

    @staticmethod
    def search(list):
        print(f"{len(list)} events available!")
        print("Apply filters? y/n")
        choice = input()

        while choice == "y":
        
            os.system("cls")

            while True:  
            
                print("What kind of filter?\n--Type")
                fltrs = input().lower().strip()

                if fltrs.lower() == "type":
                    os.system("cls")
                    print("What kind of type?\n--Adoption\n--Vaccination")
                    spc = input().lower().strip()
                    break
                else:
                    os.system("cls")
                    print("Filter not found, try again!")

            list = Base.filters(list, fltrs, spc)
            list = Pet.filters(list, fltrs, spc)
            if len(list) > 1:
                print("Apply another filter? y/n")
                choice = input().lower()
                while choice != "n" and choice != "y":
                    print("Wrong comand try again:")
                    choice = input().lower()
            elif len(list) == 0:
                print("No results")
        return list
class Message:
    def __init__(self, owner, message):
        self.owner = owner
        self.messages = []
        self.messages.append(message)

    
    def show_comment(self):
        for i in self.messages:
            print(f"Owner: {self.owner}")
            print(f"Mensage: {i}")

    def add(self, comment):
        self.messages.append(comment)
class Topic(Base, Message):
    def __init__(self, name, owner, title, message):
        self.name = name
        self.owner = owner
        self.title = title
        self.message = message
        self.comments = {}

    def create(owner):
        name = input("Topic name:")
        title = input("Post's title:")
        message = input("Decrible your post:")
        name = Topic(name, owner, title, message)
        return name

    def coment(self, owner, coment):
        if owner not in self.comments:
            self.comments[owner] = Message(owner, coment)
        else:
            self.comments[owner].add(coment)
            

    def show_info(self):
        print(f"User: {self.owner}")
        print(f"Title: {self.title}")
        print(f"Message: {self.message}")
        print(f"Coments: {len(self.comments)}")

    def show_comments(self):
        for user in self.comments:
            self.comments[user].show_comment()