# Activity Python 1: Task 4
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
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# This script is a header template that will be used for 
# all your python files the rest of the semester.
import math
Pa = float(input('Input Reference Pressure: '))
Pv = float(input('Input Particle Velocity: '))
maxSPL = float(input('Maximum allowed sound: '))
I=(10**(maxSPL/20))*Pa*Pv
print('Maximum Sound intensity in W/m^2: {0:.2f}\n' .format(I))