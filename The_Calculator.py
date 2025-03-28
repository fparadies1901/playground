import Art

def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def subtract(n1, n2):
    return n1 - n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(Art.logo)
    continue_calculation = True
    f_number = float(input("What's the first number?:     "))

    while continue_calculation:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation:     ")
        s_number = float(input("What's the second number?:    "))

        result = round(float(operations[operation_symbol](f_number, s_number)),1)
        print(f"{f_number} {operation_symbol} {s_number} = {float(result)}")

        choice = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation:    ")

        if choice == "y":
            f_number = result
        elif choice == 'n':
            continue_calculation = False
            print("\n" * 20)
            calculator() # gleich einer Schleife zu verstehen

calculator()


