#Resturaunt selector
#Ask user if anyone is vegiterian, vegan, and gluten free

#List or resturaunts
#Joes Gourmet Burgers - vegetarian: no , vegan: no , gluten free: no
#Main street Pizza Company - vegetarian: yes , vegan: no , gluten free: yes
#Corner Cafe - vegetarian: yes , vegan: yes , gluten free: yes
#Mamas Fine Italian- vegetarian: yes , vegan: no , gluten free: no 
#The Chefs Kitchen- vegetarian: yes , vegan: yes , gluten free: yes 

#Ask about dietary restrictions
Vegetarian = input('Is anyone in the party vegetarian?')
Vegan = input('Is anyone in the party vegan?')
Gluten_free = input('Is anyone in the party gluten free?')

#Options
print('Your resturaunt choices are:')

#The shit in the middle
if Vegetarian == 'yes' and Vegan == 'yes' and Gluten_free == 'yes':
    print('Corner Cafe')
    print('The Chefs Kitchen')
elif Vegetarian =='yes' and Vegan == 'yes' and Gluten_free == 'no':
    print('Corner Cafe')
    print('The Chefs Kitchen')
elif Vegetarian == 'yes' and Vegan == 'no' and Gluten_free == 'yes':
    print('Corner Cafe')
    print('The Chefs Kitchen')
    print('Main street Pizza Co.')
elif Vegetarian == 'no' and Vegan =='yes' and Gluten_free == 'yes':
    print('Corner Cafe')
    print('The Chefs Kitchen')
elif Vegetarian == 'no' and Vegan == 'no' and Gluten_free == 'yes':
    print('Main street Pizza Co.')
    print('Corner Cafe')
    print('The Chefs Kitchen')
elif Vegetarian == 'yes' and Vegan == 'no' and Gluten_free == 'no':
    print('Main street Pizza Co.')
    print('Corner Cafe')
    print('Mamas Fine Italian')
    print('The Chefs Kitchen')
elif Vegetarian == 'no' and Vegan == 'yes' and Gluten_free == 'no':
    print('Corner Cafe')
    print('The Chefs Kitchen')
elif Vegetarian == 'no' and Vegan == 'no' and Gluten_free == 'no':
    print('Joes Gourmet Burgers')
    print('Main street Pizza Co.')
    print('The Chefs Kitchen')
    print('Corner Cafe')
    print('Mamas Fine Italian')
else:
    print('')

#Print the options for there stupid ass allergies 
print('Enjoy your Resturaunt choices!')


