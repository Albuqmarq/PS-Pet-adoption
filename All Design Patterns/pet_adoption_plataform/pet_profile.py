from pet_adoption_plataform import adoption
from pet_adoption_plataform import shelter_profile
from pet_adoption_plataform import user_account
from pet_adoption_plataform import clases
import os


pet1 = clases.Pet("Bethoven", 7, "male", "brown and white", "big", "dog", shelter_profile.shelter1, False)
pet2 = clases.Pet("Garfiel", 4, "male", "orange", "medium", "cat", shelter_profile.shelter1, False)
pet3 = clases.Pet("Snoop", 2, "male", "black and white", "small", "dog", shelter_profile.shelter1, False)
pet4 = clases.Pet("Lady", 2, "female", "brown", "small", "dog", shelter_profile.shelter2, False)
pet5 = clases.Pet("Scooby", 10, "male", "brown", "big", "dog", shelter_profile.shelter2, False)
pet6 = clases.Pet("Marrie", 1, "female", "white", "small", "cat", shelter_profile.shelter2, False)
pet7 = clases.Pet("Clebinho", 7462, "male", "Red", "big", "dragon", shelter_profile.shelter3, False)
pet8 = clases.Pet("Jonas", 17, "male", "brown", "big", "pig", shelter_profile.shelter2, False)
pet9 = clases.Pet("Pong", 11, "male", "orange", "small", "orangotango", shelter_profile.shelter4, False)
pet10 = clases.Pet("Perrita", 8, "female", "pink", "small", "spider", shelter_profile.shelter4, False)
pet11 = clases.Pet("Marta", 674, "female", "brown", "big", "terrasque", shelter_profile.shelter3, False)
pet12 = clases.Pet("Jorel", 17, "male", "brown", "big", "anteater", shelter_profile.shelter4, False)
pet13 = clases.Pet("Fernada", 9, "female", "green", "big", "armadillo", shelter_profile.shelter4, False)
pet14 = clases.Pet("Neymar", 33, "male", "yellow and blue", "medium", "canary", shelter_profile.shelter2, False)

pets = [
    pet1, pet2, pet3, pet4, pet5, pet6, pet7,
    pet8, pet9, pet10, pet11, pet12, pet13, pet14
]


class PetAdoption:
    def __init__(self, pets, current_user, adoption_module):
        self.pets = pets
        self.current_user = current_user
        self.adoption_module = adoption_module

    def list_available_pets(self):
        available_pets = clases.Pet.filters(self.pets, "adopted", "False")
        filtered_pets = clases.Pet.search(available_pets)
        clases.Pet.showlist(filtered_pets)
        return filtered_pets

    def show_pet_info(self, name):
        pet = clases.Pet.search_name_in_list(name, self.pets)
        if pet:
            pet.show_info()
        return pet

    def adopt_pet(self, pet):
        if self.current_user:
            print("Usuário logado! Iniciando processo direto...")
            self.current_user.adoption_process([pet])
        else:
            self.adoption_module.adoption(pet, pet.shelter)


def showpets():
    global pets
    os.system("cls")

    facade = PetAdoption(pets, user_account.current_user, adoption)

    if user_account.current_user:
        user_account.current_user.adoption_process(pets)
    else:
        while True:
            os.system("cls")
            facade.list_available_pets()

            print("See more informations? y/n")
            info = input().lower()

            if info == "y":
                print("Enter the name of the pet you want to see: ")
                pet_choiced = input().lower().capitalize()

                os.system("cls")
                pet = facade.show_pet_info(pet_choiced)

                if pet is None:
                    input("Pet not found. Press Enter to continue...")
                    continue

                print("--Want to adopt this pet? (1)\n--Return (2)\n--Exit (3)")
                choice = input()

                if choice == "1":
                    facade.adopt_pet(pet)
                    break
                elif choice == "2":
                    continue
                elif choice == "3":
                    break
            else:
                break
