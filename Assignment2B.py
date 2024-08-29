# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Assignment2B.py
animal = input("Please enter the name of an animal: ")
animal = animal.lower()

mammals = ["dog", "cat", "human", "elephant", "whale"]
birds = ["eagle", "parrot", "penguin", "sparrow"]
reptiles = ["snake", "lizard", "crocodile", "turtle"]
fish = ["salmon", "goldfish", "shark", "tuna"]
amphibians = ["frog", "toad", "salamander", "newt"]

if animal in mammals:
    print("Your animal is a mammal")
elif animal in birds:
    print("Your animal is a bird")
elif animal in reptiles:
    print("Your animal is a reptile")
elif animal in fish:
    print("Your animal is a fish")
elif animal in amphibians:
    print("Your animal is a amphibian")
else:
    print("Your animal is unknown")