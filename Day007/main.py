import random
import hangman_art
import hangman_words


def hangman():
    game_word = random.choice(hangman_words.word_list)
    solution_word = []
    guessed_letters = []
    game_over = False
    print(hangman_art.logo, "\n")
    print("Welcome to the Hangman Game!\n")
    print("Let's go!\n")
    for _ in range(len(game_word)):
        solution_word.append("_")
    lives = 6
    print(hangman_art.stages[lives], "\n")
    print(" ".join(map(str, solution_word)), "\n")
    print(f"Psst, the solution is \"{game_word}\".\n")
    while not game_over:
        if "_" in solution_word and lives == 0:
            print(f"Sorry. Game Over. The solution would've been \"{game_word}\".\n")
            game_over = True
        elif "_" not in solution_word and lives > 0:
            print("Congratulations. You've won!\n")
            game_over = True
        else:
            letter = input("Please guess a letter:\n").lower()
            if letter in guessed_letters:
                print("You already tried this letter.\n")
            else:
                guessed_letters.append(letter)
                for i, character in enumerate(game_word):
                    if letter in character:
                        solution_word[i] = character
                        print("Success. This letter is part of the solution.\n")
                        print(" ".join(map(str, solution_word)), "\n")
                if letter not in game_word:
                    lives -= 1
                    print(hangman_art.stages[lives])
                    if lives == 1:
                        print(f"Failure. This letter is not part of the solution. {lives} try left.\n")
                    elif lives == 0:
                        pass
                    else:
                        print(f"Failure. This letter is not part of the solution. {lives} tries left.\n")
                    print(" ".join(map(str, solution_word)), "\n")
    play_again = input("Do you want to play again? (Y/N)\n").lower()
    if play_again == "y":
        hangman()


if __name__ == "__main__":
    hangman()
