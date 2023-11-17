# Activity Python 2: Task 4
# File: ACT_Python_2p4_Team048_bhattaen.py 
# Date:    1 November 2023
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
# Gives a state of the Pressurized water reactor based on a temperature and pressure

temp= float(input('Enter a Temperature'))
press= float(input('Enter a Pressure'))

if temp > 355 or press > 0.1:
    print('Melt Down')
elif 355 > temp > 345 or 0.1 > press > 0.095:
    print('Very Severe')
elif 345 > temp > 335 or 0.095 > press > 0.09:
    print('Severe')
elif 335 > temp > 325 or 0.09 > press > 0.085:
    print('Moderate')
else:
    print('Normal')