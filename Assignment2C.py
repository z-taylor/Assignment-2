# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Assignment2C.py
day = int(input("Enter a number from 1 to 7: "))
if 1<=day<=7:
    match day:
        case 1 if day==1:
            print("The day is Sunday")
        case 2 if day==2:
            print("The day is Monday")
        case 3 if day==3:
            print("The day is Tuesday")
        case 4 if day==4:
            print("The day is Wednesday")
        case 5 if day==5:
            print("The day is Thursday")
        case 6 if day==6:
            print("The day is Friday")
        case 7 if day==7:
            print("The day is Saturday")
else:
    print("Invalid number")