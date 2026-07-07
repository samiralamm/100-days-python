import random
# Todo - 1 - update the word list to use the 'word_list' from hangman_words.py

from hangman_words import word_list

# todo - 2- import the  hangman_art and logo from hangman_art.py and print it at the start of the game.

from hangman_art import stages,logo

lives = 6 
print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_lenght = len(chosen_word)
for position in range(word_lenght):
    placeholder += "-"

print("word to guess:" + placeholder)

game_over = False
correct_letters = []

while not game_over:
# todo- 5- update the code below to tell the user how many lives they have left.
    print(f"**********{lives}/6 lives left**************")
    guess = input("guess a letter: ").lower()


# Todo-3- if the user has entered a letter they've already guessed, print the letter and let them know.

    if guess in correct_letters:
        print(f"you've already guessed{guess}") 

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter 
            correct_letters.append(guess) 
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("word to guess:" +  display)  
# todo-4- if the letter is not in the chosen_word, print out the letter and let them known it's not in the word.
# e.g. you guessed d, that's not in the word. you lose a life.

    if guess not in chosen_word:
        lives -= 1
        print(f"you guessed {guess},   that's not in the word. you lose a life.")
        if lives == 0:
            game_over = True
# update the print statement below to give the user the correct word
            print("*************IT WAS {chosen_word}!YOU LOSE*********************.")

    if "_" not in display:
        game_over = True
        print("****************YOU WIN**********************.")
    print(stages[lives])

