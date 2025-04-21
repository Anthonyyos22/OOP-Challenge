# Digital Pet Simulator 🐾

A Python-based virtual pet simulation using Object-Oriented Programming principles.

![Pet Simulation Screenshot](screenshot.png) *(Replace with your actual screenshot)*

## Features ✨

- **Pet Attributes**:
  - Hunger, energy, and happiness levels (0-10 scale)
  - Name and list of learned tricks
- **Interactive Methods**:
  - `eat()`: Reduces hunger
  - `sleep()`: Restores energy
  - `play()`: Increases happiness
  - `train()`: Teaches new tricks
  - `get_status()`: Shows current stats
- **Visual Feedback**: Star ratings for each attribute
- **Bonus Features**:
  - Trick training system
  - Input validation
  - Clean status display

## How to Run 🚀

1. Clone the repository:
   ```bash
   git clone https://github.com/Anthonyyos22/OOP-Challenge.git
   cd OOP-Challenge
   python main.py
   OOP-Challenge/
├── pet.py             # Pet class implementation
├── main.py            # Main program and testing
├── README.md          # This file
└── screenshot.png     # Example output screenshot
from pet import Pet

# Create a new pet
my_pet = Pet("Fluffy")

# Interact with your pet
my_pet.eat()
my_pet.play()
my_pet.train("roll over")

# Check status
print(my_pet.get_status())
Fluffy's Status:
- Hunger: ★★★☆☆☆☆☆☆☆ (3/10)
- Energy: ★★★★★★☆☆☆☆ (6/10)
- Happiness: ★★★★★★★★☆☆ (8/10)
- Tricks: roll over