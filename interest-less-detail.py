#Function for calculating compounded interest
def future_value(principal, interest_rate, compounded, time):
    return principal * ((1 + ((interest_rate / 100) / compounded)) ** (compounded * time))

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
    principal = get_positive_float("What is the initial investment (or \"principal\") amount? ")

    interest_rate = get_positive_float("What is the interest rate? ")

    compounded = get_positive_int("How often will this be compounded in a year? ")

    time = get_positive_int("How long will this be invested (in years)? ")

    print(f"The total future value of the investment is ${future_value(principal, interest_rate, compounded, time):,.2f}.\n")

    try_again = input("Type Y to try again; any other key to exit: ")

    if try_again != "y":
        print("\nGoodbye!\n")
        break