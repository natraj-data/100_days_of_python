# Project: Band Name Generator
# It would help the people who look for the band name for their band.
# It just ask the user to enter their pet name and city where they live in.

print(" Welcome to the Band Name Generator ".center(50, "*"))
city = input("Which city did you grow up in?\n")
pet = input("What's the name of a pet?\n")
print("Your band name could be " + city.title() + " " + pet.title())
