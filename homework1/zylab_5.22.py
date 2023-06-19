# Samiha Ashraf
# 1884227

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")

# Prompt the user to select the first service
print("\nSelect first service:")
first_service = input()

# Prompt the user to select the second service
print("Select second service:")
second_service = input()

# Output an invoice for the services selected
service_cost = {
    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7,
    "Car wax": 12
}

# Calculate the total cost
total_cost = service_cost.get(first_service, 0) + service_cost.get(second_service, 0)

# Extend the program to allow the user to enter a dash (-), which indicates no service.
print("\nDavy's auto shop invoice\n")
if first_service == "-":
    print("Service 1: No service")
else:
    print("Service 1: {}, ${}".format(first_service, service_cost.get(first_service, 0)))

if second_service == "-":
    print("Service 2: No service")
else:
    print("Service 2: {}, ${}".format(second_service, service_cost.get(second_service, 0)))

print("\nTotal: ${}".format(total_cost))
