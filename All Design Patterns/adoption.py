from pet_adoption_plataform import user_account

class AdoptionProcessBuilder:
    def __init__(self, pet, shelter):
        self.pet = pet
        self.shelter = shelter
        self.valid = False

    def verify_user(self):
        if not user_account.current_user:
            raise ValueError("You need to be logged in to adopt a pet")
        if user_account.current_user.age < 21:
            raise ValueError("You must be an adult (21+ years) to adopt")
        self.valid = True
        return self

    def collect_user_info(self):
        if not self.valid:
            raise Exception("Verify user first")
        
        print(f"\nAdoption process for {user_account.current_user.name}")
        print("User information:")
        user_account.current_user.show_info()
        return self

    def confirm_info(self):
        print("\nIs this information correct? (y/n)")
        if input().lower() != 'y':
            user_account.user.changers()
        return self

    def collect_adoption_details(self):
        input("\nTell us about your home and family routine (press Enter when done): ")
        print("Thank you for the information.")
        return self

    def finalize(self):
        print(f"\nThank you for adopting {self.pet.name}!")
        print(f"We at {self.shelter.name} will review your application")
        print(f"Contact: {self.shelter.phone} | {self.shelter.email}")
        self.pet.adopted = True
        return self

def adoption(pet, shelter):
    try:
        (AdoptionProcessBuilder(pet, shelter)
            .verify_user()
            .collect_user_info()
            .confirm_info()
            .collect_adoption_details()
            .finalize())
        input("\nPress any key to return")
    except Exception as e:
        print(f"Process error: {e}")
        input("Press any key to return")
