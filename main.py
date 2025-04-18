from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    should_continue = True
    first_number = float(input("What's the first number?: "))
    while should_continue:
        for symbols in operations:
            print(symbols)
        pick_operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        answer = operations[pick_operation](first_number, second_number)
        print(f"{first_number} {pick_operation} {second_number} = {answer}")

        yes_or_no = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if yes_or_no == 'n':
            print("\n" * 100)
            calculator() #recursion
        else:
            first_number = answer
calculator()