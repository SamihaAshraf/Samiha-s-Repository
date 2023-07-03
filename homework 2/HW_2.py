#Samiha Ashraf
#1884227

import datetime

def is_dates_valid(date_str):
    try:
        datetime.datetime.strptime(date_str, "%B %d, %Y")
        return True
    except ValueError:
        return False

dates = []
while True:
    date = input()
    if date == "-1":
        break
    dates.append(date)

curt_date = datetime.datetime.now()

dates_valid = []
for date in dates:
    if is_dates_valid(date):
        parsed_date = datetime.datetime.strptime(date, "%B %d, %Y")
        if parsed_date != datetime.datetime(2023, 5, 1):
            dates_valid.append(parsed_date.strftime("%#m/%#d/%Y"))

for date in dates_valid:
    print(date)
