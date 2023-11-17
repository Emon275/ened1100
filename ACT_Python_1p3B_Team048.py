# Activity Python 1: Task 3
# File: ACT_Python_HeaderTemplate_TeamXXX_UCusername.py 
# Date:    25 October 2023
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
# Computes the Reynolds Number based on the given inputs
import math
ρ = float(input('Enter a density of fluid kg/m^3: '))
V = float(input('Enter a fluid velocity m/s: '))
L = float(input('Enter a Length m: '))
μ = float(input('Enter a Dynamic Viscosity kg/(m*s): '))

ρ2=ρ*2.237
L2=L*39.37
V2=V/27680
μ2=μ*17.858
Re= (ρ2*V2*L2)/μ2
print('Reynolds Number: {0:.2f}\n' .format(Re))
