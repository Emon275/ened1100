# Activity: 11.2 HW Task 2
# File: HW_11p2_Task2_bhattaen.py 
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
# Computes state of public measures

σ = float(input('Enter the coefficient σ (days^-1): '))
μ = float(input('Enter the coefficient μ (days^-1): '))
γ = float(input('Enter the coefficient γ (days^-1): '))
Δ = float(input('Enter the coefficient Δ (days^-1): '))
β1 = float(input('Enter the coefficient β1 (days^-1): '))
β2 = float(input('Enter the coefficient β2 (days^-1): '))
α = float(input('Enter the parameter α (days^-1): '))

F = (Δ*(β1*σ+(γ+μ)*β2))/((σ+μ)*(γ+μ)*μ)
R = (1-α)*F
αc = 1 - 1/F

if R == 1:
    if α < αc:
        print('Endemic State, increase public health measures')
    else:
        print('No change in public health measures')
elif R > 1:
    if α < αc:
        print('Disease Expansion State, Increase Public Health Measures')
    else:
        print('No change in public health measures')
elif α > αc:
    print('Disease Controlled, Decrease Public Health Measures')
else:
    print('No change in public health measures')