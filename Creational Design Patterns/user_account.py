import os
from pet_adoption_plataform import clases
from pet_adoption_plataform import shelter_profile


shelter_user1 = clases.Shelter_user(
        'Lar dos Peludos',
        '1',
        'adoteme@org.com',
        '4949939052',
        shelter_profile.shelter1
    )
shelter_user2 = clases.Shelter_user(
        'Esperança Animal',
        '2',
        'adocao@yahoo.com',
        '63348842',
        shelter_profile.shelter2
    )
shelter_user3 = clases.Shelter_user(
        'Casa do hobbit',
        '3',
        'sociedadedoanel@gmail.com',
        '63463322',
        shelter_profile.shelter3
    )
shelter_user4 = clases.Shelter_user(
        'Zoooo',
        '4',
        'eumeremxomuito@gmail.com',
        '6342145612',
        shelter_profile.shelter4
    )
users = [shelter_user1, shelter_user2, shelter_user3, shelter_user4]
current_user = None

def user_profile():
    while True:
        global current_user

        os.system("cls")

        if users == []:
            print("You need creat a account!")
        else:
            if current_user != None:
                current_user.show_info()

        escolha = input("--Creat account (1)\n--Login (2)\n--Change account information (3)\n--Return (4)\n")

        if escolha == "1":
            new_user = clases.User.creat()
            users.append(new_user)
        if escolha == "2":
            username = input("Your username:").capitalize()
            password = input("Your password: ")
            current_user = clases.User.search_name_in_list(username, users)
            if current_user:
                current_user.login(username, password)
            else:
                print("User not exist")
                input()
        elif escolha == "3":
            if current_user.getlogin():
                current_user.changers()
            else:
                while True:
                    print("You need creat a account!")
                    input("Type enter to continue")
                    break 
        elif escolha == "4":
            break
        print("\n")
    