class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting at mid-level
        self.energy = 5   # Starting at mid-level
        self.happiness = 5  # Starting at mid-level
        self.tricks = []  # For storing learned tricks
        
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food. Hunger decreased, happiness increased!")
        
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap. Energy restored!")
        
    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} played with you! Energy decreased, but happiness increased and hunger grew a bit.")
        
    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {'★' * self.hunger}{'☆' * (10 - self.hunger)} ({self.hunger}/10)")
        print(f"Energy: {'★' * self.energy}{'☆' * (10 - self.energy)} ({self.energy}/10)")
        print(f"Happiness: {'★' * self.happiness}{'☆' * (10 - self.happiness)} ({self.happiness}/10)")
        
    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows {trick}.")
            
    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} hasn't learned any tricks yet.")
        else:
            print(f"{self.name} knows these tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print("{}. {}".format(i, trick))