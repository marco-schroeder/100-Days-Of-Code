import art
import os


def add(p_1, p_2):
    return p_1 + p_2


def subtract(p_1, p_2):
    return p_1 - p_2


def multiply(p_1, p_2):
    return p_1 * p_2


def divide(p_1, p_2):
    if p_2 != 0.0:
        return p_1 / p_2
    else:
        return "Divided by 0 error"


def calculator():
    keep_calculating = True
    math_operator = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    print(art.logo)
    first_number = float(input("What's the first number?:\n"))
    for m_o in math_operator:
        print(m_o)
    while keep_calculating:
        math_operator_choice = input("Pick an operator:\n")
        next_number = float(input("What's the next number:\n"))
        calculate = math_operator[math_operator_choice]
        result = calculate(first_number, next_number)
        print(result)
        next_step = input(f"Type \"y\" to continue calculating with {result}, type \"n\" to start a new calculation, "
                          f"type \"exit\" to shut down the calculator:\n")
        if next_step == "y":
            first_number = result
        elif next_step == "n":
            keep_calculating = False
            os.system("clear")
            calculator()
        elif next_step == "exit":
            exit()


if __name__ == "__main__":
    calculator()
