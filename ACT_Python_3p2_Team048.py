# Activity Python 3: Task 3
# File: ACT_Python_3p2_Team048.py 
# Date:    15 November 2023
# By:      Emon Bhattacherjee
# Section: 003
# Team:    048
# 
# ELECTRONIC SIGNATURE
# Emon Bhattacherjee
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# This script is a header template that will be used for 
# all your python files the rest of the semester.

import random
n = int(input("How many times do you want to flip a coin? "))
Heads=0
Tails=0
for i in range(n):
    flip = random.randint(0,1)
    if flip == 1:
        Heads+=1
    elif flip == 0:
        Tails+=1
print("The heads is {0} and tails is {1}." .format(Heads,Tails))
