# Activity: 10.2 HW Task 3
# File: HW_10p2_Task3_bhattaen.py 
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
# Computes the wave angle

import math
Eio = float(input("Enter the amplitude of the incident wave, Eio (V/m): "))
n1 = float(input("Enter the intrinsic impedance of material 1, n1 (ohms): "))
n2 = float(input("Enter the intrinsic impedance of material 2, n2 (ohms): "))
Theta_i = float(input("Enter the angle of incidence, Theta_i: "))
i1 = float(input("Enter an index of medium 1: "))
i2 = float(input("Enter an indeyx of medium 2: "))

Theta_i = Theta_i * (math.pi/180)

Theta_t = math.asin((i1*math.sin(Theta_i))/i2)
Et = (2*n2*math.cos(Theta_i))*Eio/((n2*math.cos(Theta_t))+(n1*math.cos(Theta_i)))
Er = ((n2*math.cos(Theta_i))-(n1*math.cos(Theta_t)))*Eio/((n2*math.cos(Theta_i))+(n1*math.cos(Theta_t)))

Theta_t = Theta_t * (180/math.pi)

print('\n')
print("The angle of the transmitted wave is Theta_t: {0:0.2f} Degrees" .format(Theta_t))
print("The amplitude of the reflected wave is Er: {0:0.2f} V/m" .format(Er))
print("The amplitude of the transmitted wave is Et: {0:0.2f} V/m" .format(Et))
