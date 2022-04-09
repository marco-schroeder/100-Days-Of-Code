import random


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the python password generator!")
    amount_letters = int(input("How many letters would you like in your password?\n"))
    amount_symbols = int(input("How many symbols would you like in your password?\n"))
    amount_numbers = int(input("How many numbers would you like in your password?\n"))

    password = []

    for i in range(0, amount_letters):
        password.append(random.choice(letters))

    for i in range(0, amount_symbols):
        password.append(random.choice(symbols))

    for i in range(0, amount_numbers):
        password.append(random.choice(numbers))

    random.shuffle(password)

    final_password = "".join(password)

    print(f"Your generated password is:\n{final_password}")


if __name__ == "__main__":
    password_generator()
