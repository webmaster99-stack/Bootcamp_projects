import art
def add(n1, n2):
    return n1 + n2


def subtract(n1:int, n2: int):
    return n1 - n2


def multiply(n1:int, n2:int):
    return n1 * n2


def divide(n1: int, n2: int):
    return n1 / n2

print(art.logo)
operations = {}
Keys = ["+", "-", "*", "/"]
values = [add, subtract, multiply, divide]
for key in range(len(Keys)):
    operations.update({Keys[key]:values[key]})
def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("Enter the first number: \n"))
    while should_accumulate:
        for element in Keys:
            print(element)
        operator = input("Choose an option: \n")
        num2 = float(input("Enter the second number: \n"))
        answer = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer},type 'n' to start a new calculation, or type 'off; to turn off the calculator: \n")
        if choice == "y":
            num1 = answer
        elif choice == "n":
            should_accumulate = False
            print("\n" * 20)
            calculator()
        elif choice == "off":
            break

calculator()