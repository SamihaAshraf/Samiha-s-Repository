#Samiha Ashraf
#1884227

def print_roster(roster):
    print("ROSTER")
    for jersey_number in sorted(roster):
        print(f"Jersey number: {jersey_number}, Rating: {roster[jersey_number]}")
    print()


roster = {}

for i in range(5):
    jersey_number = int(input(f"Enter player {i + 1}'s jersey number:\n"))
    rating = int(input(f"Enter player {i + 1}'s rating:\n"))
    roster[jersey_number] = rating
    print()

print_roster(roster)

choice = ""
while choice != "q":
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")

    choice = input("\nChoose an option:\n")

    if choice == "a":
        new_jersey_number = int(input("\nEnter a new player's jersey number:\n"))
        new_rating = int(input("Enter the player's rating:\n"))
        roster[new_jersey_number] = new_rating
    elif choice == "d":
        jersey_number_to_remove = int(input("\nEnter a jersey number:\n"))
        if jersey_number_to_remove in roster:
            del roster[jersey_number_to_remove]
        else:
            print("Jersey number not found in the roster.")
    elif choice == "u":
        jersey_number_to_update = int(input("\nEnter a jersey number:\n"))
        if jersey_number_to_update in roster:
            new_rating = int(input("Enter a new rating for player:\n"))
            roster[jersey_number_to_update] = new_rating
        else:
            print("Jersey number not found in the roster.")
    elif choice == "r":
        rating_threshold = int(input("\nEnter a rating:\n"))
        print("ABOVE", rating_threshold)
        for jersey_number, rating in roster.items():
            if rating > rating_threshold:
                print(f"Jersey number: {jersey_number}, Rating: {rating}\n")
    elif choice == "o":
        print_roster(roster)

