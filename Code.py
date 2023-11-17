Income = float(input('Please enter your income: '))
Tax = 0.01*Income
if Income <= 50000:
  Tax = 500+0.02*(Income-50000)
elif Income <= 75000:
  Tax = 1000+0.03*(Income-75000)
elif Income <= 100000:
  Tax = 1750+0.04*(Income-100000)
elif Income <= 250000:
  Tax = 7750+0.05*(Income-250000)
elif Income <= 500000:
  Tax = 20250+0.06*(Income-500000)
else:
  print('Tax owed: ${0:0.2f}'.format(Tax))
input('Press any key to continue.')