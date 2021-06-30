import os
import sys

class Meth:

    def Add(n1,n2):
        return n1+n2
    
    def Sub(n1,n2):
        if n1 >= n2:
            return n1-n2
        else:
            print("Invalid input. Please Try again!")

    def Multi(n1,n2):
        return n1*n2
    
    def Division(n1,n2):
        if n1 > n2:
            return n1 / n2
        else:
            print("Invalid Input. Please Try again!")

