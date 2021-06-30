import sys
import os
sys.path.append(".")

from PyCalcu.Methods import Meth

def Main():
    print("Welcome user! Please Choose an Option!")
    print("[1]Addition \n[2]Subtraction \n[3]Multiplication \n[4]Division \n[5]Exit")
    user_choice = int(input("Enter number of choice:"))
    if user_choice == 1:
        print("You have chosen Addition!")
        n1 = int(input("Enter N1:"))
        n2 = int(input("Enter N2:"))
        print("Answer: {}".format(Meth.Add(n1,n2)))
    elif user_choice == 2:
        print("You have chosen Subtraction!")
        n1 = int(input("Enter N1:"))
        n2 = int(input("Enter N2:"))
        print("Answer: {}".format(Meth.Sub(n1,n2)))
    elif user_choice == 3:
        print("You have chosen Multiplication!")
        n1 = int(input("Enter N1:"))
        n2 = int(input("Enter N2:"))
        print("Answer: {}".format(Meth.Multi(n1,n2)))
    elif user_choice == 4:
        print("You have chosen Division!")
        n1 = int(input("Enter N1:"))
        n2 = int(input("Enter N2:"))
        print("Answer: {}".format(Meth.Division(n1,n2)))
    elif user_choice == 5:
        print("Thank you!")
        exit()


        
Main()