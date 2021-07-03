import os
import sys
sys.path.append(".")

from FinalLabExam.Class import PMethod as PM

class Main:
    def MMethod():
        user_input = input("Enter your name:")
        PM.PlayerName(user_input)
        print("Welcome {}! Please choose a category.".format(PM.PlayerName(user_input)))
        Category = input("[a] Mathemathics \n[b] History \nEnter your choice:")
        if Category =='a' or Category == 'A':
            PM.Math(user_input)
        elif Category == 'b' or Category == 'B':
            PM.Histroy(user_input)
        else:
            print("Invalid Choice!")

Main.MMethod()
