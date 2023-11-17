# Activity: 10.2 HW Task 2
# File: HW_10p2_Task2_bhattaen.py 
# Date:    27 October 2023
# By:      Emon Bhattacherjee
# Section: 003
# Team:    048
# 
# ELECTRONIC SIGNATURE
# Emon Bhattacherjee
# work, and I
# have a general understanding of all aspec
# The electronic signature above indicates the script
# submitted for evaluation is my individualts of its
# development and execution.
#
# Computes the Second Velocity when given the first velocity, coefficient of friction, distance traveled, and initial and final elevation

import math
v1 = float((input("Enter the car's speed at position 1, v1: ")))
f = float((input("Enter the friction coefficient, f: ")))
d = int((input("Enter the traveled distance, d: ")))
y1 = int((input("Enter the initial elevation, y1: ")))
y2 = int((input("Enter the final elevation, y2: ")))

v2 = math.sqrt(((v1**2)-(f*d*9.81))+((y1-y2)*9.81*2))

print('\n')
print("The value of v2: {0:.2f} m/s\n" .format(v2))
