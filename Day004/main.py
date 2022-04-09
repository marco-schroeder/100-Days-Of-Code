import random


def rock_paper_scissors():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    possible_choices = [rock, paper, scissors]
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    print(f"User chose: {possible_choices[user_choice]}")
    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {possible_choices[computer_choice]}")
    if user_choice == computer_choice:
        print("It's a draw.")
    if user_choice == 0 and computer_choice == 1 or user_choice == 1 and computer_choice == 2:
        print(f"Computer wins the match with: {possible_choices[computer_choice]}")
    if user_choice == 0 and computer_choice == 2 or user_choice == 1 and computer_choice == 0 or \
            user_choice == 2 and computer_choice == 1:
        print(f"User wins the match with: {possible_choices[user_choice]}")


if __name__ == "__main__":
    rock_paper_scissors()
