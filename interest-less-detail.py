def future_value(principal: float, interest_rate: float, compounded: int, time: int) -> float:
    '''Calculate the future value based on inputs. Set float and int datatypes accordingly.'''
    return principal * ((1 + ((interest_rate / 100) / compounded)) ** (compounded * time))

#Define the input functions
def get_positive_value(prompt: str, value_type: type, strip_chars: list = None):
    '''Validating input: checking for numerals only, removing empty trailing or leading characters, stripping out anticipated characters
    '''
    while True:
        value = input(prompt).strip()
        if strip_chars:
                for char in strip_chars:
                    value = value.replace(char, '')
        if not value:
            print("Please enter a value.")
            continue
        try:
            value = value_type(value)
            if value < 0:
                print("Please enter a number greater than 0.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")

def get_float(prompt: str):
    return get_positive_value(prompt, float, strip_chars=[',', '$', '%'])

def get_integer(prompt: str):
    return get_positive_value(prompt, int)



print("\nCompound Interest Calculator")

while True:
    print("\n")
    principal = get_float("What is the initial investment (or \"principal\") amount? ")

    interest_rate = get_float("What is the interest rate? ")

    compounded = get_integer("How often will this be compounded in a year? ")

    time = get_integer("How long will this be invested (in years)? ")

    print(f"The total future value of the investment is ${future_value(principal, interest_rate, compounded, time):,.2f}.\n")

    try_again = input("Type Y to try again; any other key to exit: ")

    if try_again != "y":
        print("\nGoodbye!\n")
        break