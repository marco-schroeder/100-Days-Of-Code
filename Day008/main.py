import caesar_cipher_art


def caesar_cipher(p_direction, p_message, p_shift):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    result = ""
    length_alphabet = len(alphabet)
    if p_direction == "decode":
        p_shift *= -1
        length_alphabet = len(alphabet) * -1

    for letter in p_message:
        if letter in alphabet:
            position = alphabet.index(letter)
            if position + (p_shift % length_alphabet) >= len(alphabet) or position + (p_shift % length_alphabet) < 0:
                new_position = position + (p_shift % length_alphabet) - length_alphabet
            else:
                new_position = position + (p_shift % length_alphabet)
            new_letter = alphabet[new_position]
            result += new_letter
        else:
            result += letter
    print(f"Here is your {p_direction}d result:\n{result}\n")


def main():
    direction = None
    again = None
    shift = ""
    print(caesar_cipher_art.logo, "\n")
    while direction != "encode" and direction != "decode":
        direction = input("Please type in \"encode\" encrypt or \"decode\" to decrypt:\n").lower()
    message = input("Type your message:\n").lower()
    while not shift.isnumeric():
        shift = input("Type the shift number:\n")
    caesar_cipher(direction, message, int(shift))
    while again != "yes" and again != "no":
        again = input("Type \"yes\" if you want to go again. Otherwise type \"no\".\n").lower()
    if again == "yes":
        main()


if __name__ == "__main__":
    main()
