from pet_adoption_plataform import pet_profile 
from pet_adoption_plataform import user_account
from pet_adoption_plataform import shelter_profile
from pet_adoption_plataform import forum
import os

while True:
    os.system("cls")

    if user_account.current_user != None:
        if user_account.current_user.getlogin() == True:
            print(f"Welcome {user_account.current_user.name} to our Pet Adoption Platform!!!")
        else:
            print(f"Welcome quest to our Pet Adoption Platform!!!")
    else:
        print(f"Welcome quest to our Pet Adoption Platform!!!")
    print("--View and adopt our pets type (1)\n--View your profile type (2)\n--See shelters and rescue information type (3)\n--Forum (4)\n--Exit (5)")
    choice = input()
    if choice == "1":
        pet_profile.showpets()
    if choice == "2":
        user_account.user_profile()
    if choice == "3":
        shelter_profile.showshelter()
    if choice == "4":
        forum.menu()
    if choice == "5":
        os.system("cls")
        break