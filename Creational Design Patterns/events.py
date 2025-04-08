import os
from pet_adoption_plataform import clases


event1 = clases.Event('Feira de adoção', 'Parque da cidade', '12/02', '13:00', '17:00', 'adoption')
event2 = clases.Event('Feira de adoção 2', 'Parque da cidade', '13/02', '10:00', '20:00', 'adoption')
event3 = clases.Event('Feira de vacinação', 'Parque da cidade', '15/02', '7:00', '17:00', 'vaccination')
event4 = clases.Event('Feira de vacinação 2', 'Parque da cidade', '12/02', '8:00', '10:00', 'vaccination')

events = [event1, event2, event3, event4]

def show_events():
    global events
    os.system("cls")

    filter_events = clases.Event.search(events)

    clases.Event.showlist(filter_events)

    while True:
        
        os.system("cls")

        for event in events:
            print(f"Name: {event.name}")

        print("See more informations? y/n")
        info = input().lower()

        if info == "y":
            print("Enter the name of the pet you want to see: ")
            event_choiced = input().lower().capitalize()
            event_info = clases.Event.search_name_in_list(event_choiced, events)
            
            if not event_info:
                continue

            os.system("cls")

            event_info.show_info()

            print("--Return (1)\n--Exit (2)")
            
            choice = input()
            
            if choice == "1":
                continue

            elif choice == "2":
                break
        
        else:
            break