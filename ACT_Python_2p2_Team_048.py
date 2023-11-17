# Activity Python 2: Task 2
# File: ACT_Python_2p2_Team048_bhattaen.py 
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
# Calculuted the state for a ph value

ph = float(input('Enter a ph value: '))
if ph >= 0 and ph < 7:
    print('Acidic')
elif ph == 7:
    print('Neutral')
elif ph > 7 and ph <= 14:
    print('Basic')
else:
    print('Invalid')