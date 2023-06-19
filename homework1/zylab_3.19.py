#Samiha Ashraf
#1884227

# code 1
height = int(input('Enter wall height (feet):\n'))
width = int(input('Enter wall width (feet):\n'))

area = height * width
print('Wall area:', area, 'square feet')

# code 2
area = height * width
needed_paint = area / 350
print('Paint needed: {} gallons'.format('%.2f'% needed_paint))
# print('Wall area: {} square feet'.format(area))

#code 3
cans_needed = int(needed_paint + 0.99)
print("Cans needed:", cans_needed, "can(s)\n")

#code 4
red = 35
blue = 25
green =  23
color = input ("Choose a color to paint the wall:\n")
cost = {'red': 35, 'blue': 25, 'green': 23}
if color in cost:
   total = cost[color]*cans_needed
print("Cost of purchasing", color, "paint: $", end='')
print(total)