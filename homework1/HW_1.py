# Samiha Ashraf
# 1884227

current_mth = int(input('Current day\nMonth:'))
current_day = int(input('Day: '))
current_yr = int(input('Year: '))

b_day_mth = int(input('Birthday\nMonth:'))
b_day_day = int(input('Day: '))
b_day_yr = int(input('Year: '))

age = current_yr - b_day_yr

is_birthday = (current_mth == b_day_mth) and (current_day == b_day_day)

print('Birthday Calculator')
print('Current day')
print(f'Month: {current_mth}')
print(f'Day: {current_day}')
print(f'Year: {current_yr}')
print('Birthday')
print(f'Month: {b_day_mth}')
print(f'Day: {b_day_day}')
print(f'Year: {b_day_yr}')
print(f'You are {age} years old.')

