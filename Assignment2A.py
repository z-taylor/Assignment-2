# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Assignment2A.py
age = int(input("Please enter your age: "))
member = input("Are you a member of the cinema club? y/n ")
member = member.lower()

if age<12:
    print("Your ticket is $12")
elif 18>age>=12:
    print("Your ticket is $10")
elif 65>age>=18:
    if member == "y" or member == "yes":
        print("Your ticket is $12")
    else:
        print("Your ticket is $15")
else:
    print("Your ticket is $10")