# Activity: 10.2 HW Task 1
# File: HW_10p2_Task1_bhattaen.py 
# Date:    27 October 2023
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
# Computes the Compound Interest Rate based on a given Interest rate

import math
P = int((input("Enter a principle sum: ")))
x = int((input("Enter interest factor: ")))
n = int((input("Enter a compounding frequency: ")))
t = int((input("Enter the amount of time for interest: ")))

r = (1/n**2)*abs(math.sin(x)/x)
A = P*(1+r)**(n*t)
I = A - P

print('\n')
print("The Principal is: ${0:.2f}\n" .format(P))
print("The interest rate is: {0:.4f}\n" .format(r))
print("The interest Earnings are: ${0:.2f}\n" .format(I))
print("The Final Amount is: ${0:.2f}\n" .format(A))