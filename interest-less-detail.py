print("\nCompound Interest Calculator")

while True:
    print("\n")
    #First, let's gather the information about the investment.
    principal = float(input("What is the initial investment (or \"principal\") amount? "))

    interest_rate = float(input("What is the interest rate? ")) / 100

    compounded = int(input("How often will this be compunded in a year? "))

    time = int(input("How long will this be invested (in years)? "))

    #Data has been gathered, let's do the math:

    print(f"The total future value of the investment is ${(principal * ((1 + (interest_rate / compounded)) ** (compounded * time))):,.2f}.\n")

    try_again = input("Type Y to try again; any other key to exit: ")

    if try_again != "y":
        print("\nGoodbye!\n")
        break