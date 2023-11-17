# Activity: 11.2 HW Task 1
# File: HW_11p2_Task1_bhattaen.py 
# Date:    4 November 2023
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
# Computes the calories burnt for a specific person and the type of machine used

import math

machine_type = input('Enter the type of machine: ')
weight = int(input('Enter a weight in lbs: '))
age = int(input('Enter your age: '))
heart_rate = int(input('Enter your heart rate in beats/minutes: '))

if machine_type == 'Automatic':
    mhr = 206-0.88*age
elif machine_type == 'Manual':
    mhr = 205.8-0.685*age
if heart_rate < 0.6*mhr:
    al = 'Below Level'
elif 0.6*mhr <= heart_rate < 0.7*mhr:
    al = 'Weight Loss'
elif 0.7*mhr <= heart_rate < 0.8*mhr:
    al = 'Cardio'
elif 0.8*mhr <= heart_rate < 0.9*mhr:
    al = 'Anaerobic (Hardcore)'
else:
    al = 'Above Level'

if machine_type == 'Automatic':
    c = 60*((age * 0.2017 + weight * 0.09036 + heart_rate * 0.6309 - 55.0969)/4.184)
elif machine_type == 'Manual':
    c = 60*((age * 0.074 - weight * 0.05741 + heart_rate * 0.4472 - 20.4022)/4.184)

print('Calories burnt per hour is {0:0.2f} ' .format(c) + 'for an activity level of: ' + al)