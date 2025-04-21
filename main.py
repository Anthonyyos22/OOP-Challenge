class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.energy = 100
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 10)
        print(f"{self.name} has eaten and feels less hungry.")

    def sleep(self):
        self.energy = min(100, self.energy + 20)
        print(f"{self.name} has taken a nap and feels more energetic.")

    def play(self):
        if self.energy >= 10:
            self.energy -= 10
            self.hunger += 5
            print(f"{self.name} had fun playing!")
        else:
            print(f"{self.name} is too tired to play.")

    def get_status(self):
        print(f"{self.name}'s status: Hunger = {self.hunger}, Energy = {self.energy}")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} has learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows the trick: {trick}.")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")

def main():
    # Create a new pet
    pet_name = input("What would you like to name your pet? ")
    my_pet = Pet(pet_name)
    
    print(f"\nWelcome, {my_pet.name}! Let's take care of your new digital pet.")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet")
        print("2. Let your pet sleep")
        print("3. Play with your pet")
        print("4. Check pet's status")
        print("5. Teach your pet a trick")
        print("6. See tricks your pet knows")
        print("7. Quit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            my_pet.eat()
        elif choice == "2":
            my_pet.sleep()
        elif choice == "3":
            my_pet.play()
        elif choice == "4":
            my_pet.get_status()
        elif choice == "5":
            trick = input("What trick would you like to teach? ")
            my_pet.train(trick)
        elif choice == "6":
            my_pet.show_tricks()
        elif choice == "7":
            print(f"Goodbye! {my_pet.name} will miss you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()