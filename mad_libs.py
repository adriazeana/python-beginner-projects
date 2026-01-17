# Mad Libs Game Title
print("=" * 50)
print("        ✨ MAD LIBS STORY GENERATOR ✨")
print("=" * 50)
print()

# Introduction where user can type their name
name = input("What's your name? ").strip().title()
print(f"Welcome to Mad Libs Game, {name}!")
print("This is where you can create a story by filling in the blank spaces.")
print()

## List down variables
weather = input("What's the weather? (cold/hot/rainy) ")
season = input("What's the season? (winter/summer/spring/autumn) ")
noun = input("What's the animal? ")
adjective = input("What's an adjective? ")
verb = input("What's the animal doing? (includes -ing) ")
place = input("Where is it? ")

## Make sentences with variables
print()
print("=" * 50)
print("           📖 HERE'S YOUR STORY: 📖")
print("=" * 50)
print()
print(f"One {weather} {season} day, a {adjective} {noun} was {verb} to the {place}.")
print(f"The {noun} decided to go to the {place} because it was so {weather} and all the ponds and rivers had dried up.")
print(f"When the {adjective} {noun} finally reached the {place}, it was empty!")
print(f"What a {weather} day it had been!")