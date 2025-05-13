import os
helps = {
    "adoption" : "To adopt a dog online, you need to access the ""Adoptions"" tab and choose a friend. After choosing, it is necessary to send a form with questions about the adopter's residence and personal data",
    "tips" : "To care for a pet, you need to give it attention, affection and care, in addition to ensuring its health and well-being. \nSome tips for caring for a pet are:\nVaccination: Ensure that your pet is always vaccinated \\nExams: Take exams regularly \nOral hygiene: Brush your pet's teeth with toothpaste suitable for dogs or cats \nFood: Provide adequate nutrition \nHydration: Keep your pet always hydrated with clean, fresh water \nOutings: Set aside time during the day for outings and games \nDeworming: Deworm the pet according to its age and veterinarian’s recommendations \nParasite Prevention: Prevent ticks, fleas and other parasites \nRest space: Set aside a quiet, cool corner for your pet to rest \nBeware of poisonous plants: Prevent your pet from having access to poisonous plants \nIt is also important to be monitored by a veterinarian, as he or she will be able to evaluate the pet in the ideal way."
}

def showhelp():
    global helps
    while True:
        for help in helps.keys():
            print(f"--{help.capitalize()}")

        choice_help = input("What topic you want help?\n").lower()


        if not helps.get(choice_help):
            continue
        os.system("cls")
        print(helps[choice_help])

        choice = input("--Return (1)\n--Exit (2)\n")

        if choice == "1":
            continue
        if choice == "2":
            break