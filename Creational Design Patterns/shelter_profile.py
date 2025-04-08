import os
from pet_adoption_plataform import pet_profile
from pet_adoption_plataform import user_account
from pet_adoption_plataform import clases

shelter1 = clases.Shelter(
        'Lar dos Peludos',
        'Maceio',
        'adoteme@org.com',
        '4949939052',
        0,
        'O Lar dos Peludos é um abrigo dedicado ao resgate e acolhimento de animais em situação de abandono e maus-tratos. Nosso objetivo é proporcionar um ambiente seguro e acolhedor para cães e gatos que precisam de uma segunda chance.'
    )
shelter2 = clases.Shelter(
        'Esperança Animal',
        'Penedo',
        'adocao@yahoo.com',
        '63348842',
        0,
        'O Abrigo Esperança Animal é um espaço dedicado ao resgate, cuidado e reabilitação de animais abandonados, maltratados ou em situação de risco. Nossa missão é oferecer um lar temporário seguro, repleto de amor e atenção, enquanto trabalhamos para encontrar famílias responsáveis e amorosas para cada um de nossos resgatados.'
    )
shelter3 = clases.Shelter(
        'Casa do hobbit',
        'Gondor',
        'sociedadedoanel@gmail.com',
        '63463322',
        0,
        'Animais miticos de todas as formas e tamanhos.'
    )
shelter4 = clases.Shelter(
        'Zoooo',
        'New York',
        'eumeremxomuito@gmail.com',
        '6342145612',
        0,
        'Animais exoticos.'
    )
shelters = {
    shelter1,
    shelter2,
    shelter3,
    shelter4
}

def showshelter():
    while True:
        
        os.system("cls")

        clases.Shelter.showlist(shelters)

        print("See more about the shelters? y/n")
        choice = input()

        if choice == "y":
            print("Enter the name of the shelter you want to see: ")
            shelter_choiced = input().lower()

            shelter_info = clases.Shelter.search_name_in_list(shelter_choiced, shelters) 

            if shelter_info is None:
                print("Shelter dont found")
                return
            
            if not shelter_info:
                continue

            os.system("cls")
            
            
            shelter_info.show_info()

            print("--See our availabels pets? (1)\n--Send a donation for this shelter? (2)\n--Return (3)\n--Exit (4)")
            
            choice = input()

            os.system("cls")

            if choice == "2":
                if user_account.user == None:
                    print("You need have a account to do a donation")   
                elif user_account.user.age > 18:
                    print("Send your tip")
                    donation = float(input())
                    print(f"Thanks {user_account.user.name}Our pets from {shelter_info.name} are pleased for your contribution of {donation:.2f}$")
                else:
                    print("You need be a adult to do a donation")
                input("\nPress any key to return")
                continue

            elif choice == "1":
                pets_availables = clases.Shelter.filters(pet_profile.pets, "shelter_name", shelter_info.name)

                clases.Base.showlist(pets_availables)

                input("\nPress any key to return")
                continue
            elif choice == "3":
                continue
            elif choice == "4":
                break
        elif choice == "n":
            break