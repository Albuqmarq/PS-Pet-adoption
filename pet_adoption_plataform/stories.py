import os
from pet_adoption_plataform import clases
from pet_adoption_plataform import shelter_profile


pet = clases.Pet("Cristal", 1, "cat", "brown", "small", "cat", shelter_profile.shelter1, True)
pet2 = clases.Pet("Marley", 2, "dog", "brown", "big", "dog", shelter_profile.shelter2, True)
pet3 = clases.Pet("Luna", 1, "cat", "white", "small", "cat", shelter_profile.shelter1, True)

stories = [pet, pet3, pet2]

pet.stories("A Cristal foi adotada após o primeiro dia de anúncio. Estamos muito felizes em fazer parte dessa história 🤍")
pet2.stories("A quinta casa depois do abrigo um guerreirinho")
pet3.stories("Um rapaz de bom coração levou ela")

def showstorie():
    global stories
    while True:
        os.system("cls")
        clases.Base.showlist(stories)

        choice_pet = input("Choice one pet to see they story: ").lower().capitalize()

        pet_choiced = clases.Pet.search_name_in_list(choice_pet, stories)

        if not pet_choiced:
            continue

        print(f"Name: {pet_choiced.name}\nAdopt from: {pet_choiced.shelter.name}\nStory: {pet_choiced.storie}")

        choice = input("--Return (1)\n--Exit (2)\n")

        if choice == "1":
            continue
        if choice == "2":
            break