# Python 308 
# Assignment 1 Exercise 2-10
# Program ask for user input for a recipe then adjust the ingredient to fit the users desired volume


# define variables for recipe 
RECIPE = 48 
cupsSugar = 1.5
cupsButter = 1 
cupsFlower = 2.75


# Prompt user 
userCookies = int (input('How many cookies do you want to make? '))


# Calculate new value for recipe 
cupAdjust = userCookies/RECIPE 
cupsSugar = cupsSugar*cupAdjust 
cupsButter = cupsButter*cupAdjust 
cupsFlower = cupsFlower*cupAdjust  


#Output data to the user
print('To make', userCookies, 'cookies you need:')
print(format(cupsSugar, '.2f'), 'cups sugar.')
print(format(cupsButter, '.2f'), 'cups butter.')
print(format(cupsFlower, '.2f'), 'cups flower.')

