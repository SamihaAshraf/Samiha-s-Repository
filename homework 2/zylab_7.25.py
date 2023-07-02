#Samiha Ashraf
#1884227
def exact_change(user_total):
    num_coins = [0, 0, 0, 0, 0]  # [dollars, quarters, dimes, nickels, pennies]
    coin_values = [100, 25, 10, 5, 1]

    for i in range(len(coin_values)):
        num_coins[i] = user_total // coin_values[i]
        user_total %= coin_values[i]

    return tuple(num_coins)  # Corrected the return statement to return a tuple

if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    if input_val <= 0:
        print("no change")
    else:
        if num_dollars > 0:
            if num_dollars == 1:
                print("1 dollar")
            else:
                print(num_dollars, "dollars")

        if num_quarters > 0:
            if num_quarters == 1:
                print("1 quarter")
            else:
                print(num_quarters, "quarters")

        if num_dimes > 0:
            if num_dimes == 1:
                print("1 dime")
            else:
                print(num_dimes, "dimes")

        if num_nickels > 0:
            if num_nickels == 1:
                print("1 nickel")
            else:
                print(num_nickels, "nickels")

        if num_pennies > 0:
            if num_pennies == 1:
                print("1 penny")
            else:
                print(num_pennies, "pennies")
                