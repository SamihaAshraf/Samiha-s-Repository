# Samiha Ashraf
# 1884227

# Code 1
lemon_juice = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))

servings = float(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields', format(servings, '.2f'), 'servings')
print(format(lemon_juice, '.2f'), 'cup(s) lemon juice')
print(format(water, '.2f'), 'cup(s) water')
print(format(agave_nectar, '.2f'), 'cup(s) agave nectar\n')

#Code 2
desired_servings = float(input('How many servings would you like to make?\n'))

adj_fact = desired_servings / servings
adj_lemon_juice = lemon_juice * adj_fact
adj_water = water * adj_fact
adj_agave_nectar = agave_nectar * adj_fact

print('\nLemonade ingredients - yields', format(desired_servings, '.2f'), 'servings')
print(format(adj_lemon_juice, '.2f'), 'cup(s) lemon juice')
print(format(adj_water, '.2f'), 'cup(s) water')
print(format(adj_agave_nectar, '.2f'), 'cup(s) agave nectar')

#Code 3
gal_change_fact = 1 / 16
gal_lemon_juice = adj_lemon_juice * gal_change_fact
gal_water = adj_water * gal_change_fact
gal_agave_nectar = adj_agave_nectar * gal_change_fact

print('\nLemonade ingredients - yields', format(desired_servings, '.2f'), 'servings')
print(format(gal_lemon_juice, '.2f'), 'gallon(s) lemon juice')
print(format(gal_water, '.2f'), 'gallon(s) water')
print(format(gal_agave_nectar, '.2f'), 'gallon(s) agave nectar')
