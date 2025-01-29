# Make a random pet.
import random
# Choose:
# Type of animal (at least 3 choices, string)
animal = ["otter", "beaver", "seal", "shark", "orca", "pirhana", "seahorse", "whale", "dolphin", "turtle", "jellyfish", "octopus", "squid",]
animal_choice = random.choice(animal)
# Age (integer)
age = random.randint(0, 1000)
# Color (at least 3 choices, string)
color = ["a red", "an orange", "a yellow", "a green", "a blue", "a purple"]
color_choice = random.choice(color)
# Weight (float)
weight = random.randint(0, 1000)

# Print a summary of your pet using an f-string
print(f"Your pet is {color_choice} {animal_choice}, it is {age} years old, and it weighs {weight} lbs.")