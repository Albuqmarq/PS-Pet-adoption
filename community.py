import os
from pet_adoption_plataform import clases
from pet_adoption_plataform import user_account

topic1 = clases.Topic("Petshops recomendados", "Isabela", "Recomendação de petshop", "Sou nova na cidade e queria recomendações de petshop para comprar ração de gato")
topic1.coment("Matheus", "Eu sempre levo os meus no petshop do shopping")

topics = [topic1]

def showcommunity():
    global topics

    while True:
        clases.Topic.showlist(topics)
        
        choice = input("--Want to participate in the debate? (1)\n--Create a topic (2)\n--Exit (3)\n").lower()
        if choice == "3":
            break
        if choice == "2":
            if user_account.user != None and user_account.user.getlogin() == True:
                topics.append(clases.Topic.create(user_account.user.name))
                os.system("cls")
            else:
                input("You need be logged")
                os.system("cls")
            continue

        if choice == "1":
            choice_topic = input("Choice a topic to participate: ").lower().capitalize()
            topic_find = clases.Topic.search_name_in_list(choice_topic, topics)

            if not topic_find:
                print("Topic dont found")
                continue
            while True:
                os.system("cls")

                topic_find.show_info()

                comment = input("--Read comments (1)\n--Write a comment (2)\n--Return (3)\n")
                if comment == "1":
                    os.system("cls")
                    topic_find.show_comments()
                    input()
                    os.system("cls")
                    continue
                if comment == "2":
                    os.system("cls")
                    if user_account.user == None:
                        print("You need to have a account")
                        input()
                        os.system("cls")
                        continue
                    elif user_account.user.getlogin() == False:
                        print("You need been logged")
                        input()
                        os.system("cls")
                        continue
                    else:
                        user_profile = user_account.user.name
                        user_comment = input("Enter your comment: ")

                        topic_find.coment(user_profile, user_comment)
                        os.system("cls")
                    continue
                if comment == "3":
                    break
                else:
                    print("Try again")
        else:
            break