import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']

word_list = ["aardvark","baboon", "camel","sana"]

# Todo-1 - randomly choose a word from the word_list and assign it to a variable called chosen_word. thrn print it.

# todo-6- create a variable called 'lives' to keep track of the number of lives left,
# set 'lives' to equal 6.
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

# todo-04- create a "placeholder" with the same number of blanks as the chosen_word

placeholder = ""
word_lenght = len(chosen_word)
for position in range(word_lenght):
    placeholder += "-"
print(placeholder)

# todo-2- ask the user to guess a letter and assign their answer to a variable called guess. make guess lowercase.

# todo-5- use a whlie loop to let the user guess again
game_over = False
correct_letters = []
while not game_over:
    guess = input("guess a letter: ").lower()


    # todo-3- check if the letter the user guessed (guess) is one of the letter in the  chosen_word. print"right" if it is, "wrong" if it;s not.

    # todo- 03- create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter 
            correct_letters.append(guess) 
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)  
    # todo- 7- if guess is not a letter in thr chosen_word' then reduce 'lives' by 1.
    # todo- 8- if lives goes down to 0 then the game should stopand it should print "you lose"
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you lose.")

    if "_" not in display:
        game_over = True
        print("you win.")    
# todo- 9- print the ACII art from 'stages'
# that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
    