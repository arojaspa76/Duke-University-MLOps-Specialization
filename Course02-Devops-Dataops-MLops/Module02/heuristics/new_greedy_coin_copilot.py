import click

# build a function that returns the minimun number of coins only using quarters and dimes
""" Greedy Coin Change Algorithm
1. The function greedy_coin takes one argument, the amount of change to be given to the customer.
2. The function prints a statement to tell the customer how much change they are getting.
3. The function initializes a list of coins (quarters and dimes) and a dictionary that maps the coins to their denominations.
4. The function initializes a dictionary that will hold the number of coins of each type.
5. The function goes through the list of coins and initializes the dictionary with a value of 0 for each coin.
6. The function goes through the list of coins.
7. The function subtracts the coin from the amount of change the customer is getting until the amount of change is less than the coin.
8. The function then increments the number of coins of that type by 1.
9. The function prints the number of each coin type the customer is getting.
10. The function returns the dictionary with the number of each coin type. 
"""

def greedy_coin(amount):
    """Greedy Coin Change Algorithm"""
    print(f"Giving change of {amount} cents")
    coins = [0.25, 0.10]  # quarters and dimes
    coin_names = {0.25: "quarters", 0.10: "dimes"}
    coin_count = {}

    for coin in coins:
        coin_count[coin] = 0

    for coin in coins:
        while amount >= coin:
            amount -= coin
            coin_count[coin] += 1

    for coin in coins:
        print(f"{coin_count[coin]} {coin_names[coin]}")

    return coin_count

# build a function that returns the minimun number of coins only using pennies, nickels and dimes
def greedy_coin_2(amount):
    """Greedy Coin Change Algorithm"""
    print(f"Giving change of {amount} cents")
    coins = [0.10, 0.05, 0.01]  # dimes, nickels and pennies
    coin_names = {0.10: "dimes", 0.05: "nickels", 0.01: "pennies"}
    coin_count = {}

    for coin in coins:
        coin_count[coin] = 0

    for coin in coins:
        while amount >= coin:
            amount -= coin
            coin_count[coin] += 1

    for coin in coins:
        print(f"{coin_count[coin]} {coin_names[coin]}")

    return coin_count

# build a click group
@click.group()
def main():
    """Return the minimum number of coins for a given change
    
    example:
    python new_greedy_coin_copilot.py 1.00
    """
    pass

# build a click command that returns only quarters and dimes
@main.command("qd")
@click.argument('amount', type=float)
def quarters_and_dimes(amount):
    """Return the minimum number of coins for a given change using only quarters and 
    
    example:
    python new_greedy_coin_copilot.py qd 1.00
    """
    greedy_coin(amount)

# build a click command that returns only pennies, nickels and dimes
@main.command("pnd")
@click.argument('amount', type=float)
def pennies_nickels_and_dimes(amount):
    """Return the minimum number of coins for a given change using only pennies, nickels and dimes
    
    example:
    python new_greedy_coin_copilot.py pnd 1.00
    """
    greedy_coin_2(amount)

if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
    # run the main function
