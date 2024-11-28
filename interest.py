#Functions for floating and integer inputs; check for valid values and strip unneeded characters
def get_positive_float(prompt):
    while True:
        value = input(prompt)
        value = value.replace(',', '').replace('$', '').replace('%', '')
        try:
            value = float(value)
            if value < 0:
                print("Please enter a number greater than 0.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")
            
def get_positive_int(prompt):
    while True:
        value = input(prompt)
        try:
            value = int(value)
            if value < 0:
                print("Please enter a number greater than 0.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")


print("\nCompound Interest Calculator")

while True:
    print("\n")
    #First, let's gather the information about the investment.
    principal = get_positive_float("What is the initial investment (or \"principal\") amount? ")
    print(f"You entered: ${principal:,.2f}\n")

    interest_rate = get_positive_float("What is the interest rate? ") / 100
    print(f"You entered: {100 * interest_rate}% interest rate.\n")

    compounded = get_positive_int("How often will this be compounded in a year? ")
    print(f"You entered:",compounded,"time(s) a year.\n")

    time = get_positive_int("How long will this be invested (in years)? ")
    print(f"You entered:",time,"years.\n")

    #Data has been gathered, let's do the math next.
    print("Great! Let's walk through the calculation:\n")

    times_compounded = compounded * time
    print(f"This will be compounded {times_compounded} times ({compounded} times over the course of {time} years).\n")

    periodic_interest_rate = interest_rate / compounded
    print(f"The periodic interest rate is {periodic_interest_rate}.\n")

    growth_factor = 1 + periodic_interest_rate
    print(f"The growth factor per compounding period is the periodic interest rate ({periodic_interest_rate}) plus 1, or {growth_factor}.\n")

    compound_growth_factor = growth_factor ** times_compounded
    print(f"The compound growth factor is the growth factor {growth_factor} raised to the power of {times_compounded}, the times compounded, which equals {compound_growth_factor}.\n")

    future_value = round(principal * compound_growth_factor, 2)
    print(f"Finally, we calculate the total future value (including the initial investment) by multiplying the principal of ${principal:,.2f} by the compound growth factor of {compound_growth_factor}.\n")
    print(f"...for a total of ${future_value:,.2f}.\n")

    try_again = input("Would you like to try again (y to try again, any other key to exit)?")

    if try_again != "y":
        print("\nGoodbye!\n")
        break