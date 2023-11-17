# Activity Python 3: Task 3
# File: ACT_Python_3p3_Team048.py 
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
import math
n= int(input('Enter a positive number: '))
n1=n
i=1
if n<0:
    print('Number needs to be positive. :)')
elif n==0:
    print('Your answer is 1')
else:
    while n>0:
        i=n*i
        n=n-1
print('{0}!= {1}'.format(n1,i))