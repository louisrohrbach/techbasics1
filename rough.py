# a secret_words.txt file with UPPERCASE Words that are written beneath each other
# is needed for the code to properly work. See Feasibilty Report section in essay.

import random
#needed for picking the random word from txt file

# inputting name and saving it to use during the code
name = input("Hey, what's your name? ")
print("\n\n\n\n\n\n\n\nHello " + name + ", this game is called Hang-Person. (Gender-friendly, we're in 2019, you know?)")
print("Do you know how to play this game?\n")

# Ruleset, asking the user if they know hangman
knows_rules = input("Answer 'yes' if you do, answer 'no' if you want to have the rules explained.\n\n\n\n\n\n\n\n")
knows_rules = knows_rules.upper() # so people can write "yes", "Yes" and "YES" (same with no)
if knows_rules == "YES":
    print("\n\n\n\n\nDope. Let's begin:\n\n\n\n")
elif knows_rules == "NO":
    print("\n\n\n\n\n\nReally? Okay. So I choose a word, you have some tries to guess the right letters and figure "
          "out the word. It is important, that you are able to \nguess a letter only one time during the game!"
          "\nDon't duplicate your guesses. If you can't find out the word it you die. lol. You ready? Let's go!\n\n\n")

# if someone does not answer yes or no
else:
    print("\n\n\n\n\nI told you... yes or no... I don't even want to play with you, if you can't even "
          "follow these rules...\n"
          "Just start from the beginning.\n\n\n\n\n\n\n")
    quit()

# choosing the word with the import random function from the txt file
secret_word = (random.choice(open("secret_words.txt").read().split()))

answer = secret_word
print("This is my word. I'll give you 8 tries to guess the letters correctly! \nTry your best.\n")
#this imports the secret word from the secret_words.txt randomly.


# this is for what the user sees: underscores is a list with the number of letters of the chosen random word
# the list is extended with the word, because it was empty before
underscores = []
underscores.extend(answer)

# this replaces the number (length) in the word/list with the underscores
for i in range(len(underscores)):
    underscores[i] = "_"

# and prints them out (joins them) so the user can see them, with a space in between them using the join function
print(' '.join(underscores))
# print(answer) for testing

# this sets the counters to 0, so we can ultimately keep track of our system and tries
correct_letters = 0
number_of_tries = 0
wrong_guesses = 0

# this is a while loop checking if the amount letters guessed is lower than the amount of letters in the word
while correct_letters < len(answer):
    guess = input("\nPlease guess a letter, my person: ")
    guess = guess.upper()# this turns the guessed letter into an UPPERCASE letter, so it matches the words.txt
    number_of_tries +=1 #every turn is a try more

    # this is important to set, so we have a counter of missed attempts, that will decide the outcome of the game
    # duplicate entries will be counted also
    if guess not in answer:
        wrong_guesses += 1

    # every time a guess is made, it checks the user input with the items in the answer list. if there is a guess that
    # matches the answer, it replaces the underscore item with the guessed letter, making it visible to the user
    for i in range(len(answer)):
        if answer[i] == guess:
            underscores[i] = guess
            #arduino board maybe?
            correct_letters += 1# this is important for counting so the program recognizes the win, at the end.
        print("        \n"
        "        \n"
        "        \n"
        "        \n\n")

    # if user wants to guess the whole word
    if guess == secret_word:
        guess
        print("You must be cheating, " + name + "! The word was indeed " + secret_word + ". \nGreat job!")
        print("You only took %d tries, " % number_of_tries + name)
        quit()

    # since this is hang-person and not a simple guessing game the program is
    # drawing for the missed tries, with the 8th missed attempt the game quits and is over
    if wrong_guesses == 1:
        print("        |\n"
              "        |\n"
              "        |\n"
              "        |\n\nYou have 7 wrong guesses left."
              )

    if wrong_guesses == 2:
        print("        _____\n"
              "        |\n"
              "        |\n"
              "        |\n"
              "        |\n\nYou have 6 wrong guesses left."
              )

    if wrong_guesses == 3:
        print("        _____\n"
              "        |   O\n"
              "        |\n"
              "        |\n"
              "        |\n\nYou have 5 wrong guesses left."
              )

    if wrong_guesses == 4:
        print("        _____\n"
              "        |   O\n"
              "        |   |\n"
              "        |\n"
              "        |\n\nYou have 4 wrong guesses left, " + name + ". Use your braincells!"
              )

    if wrong_guesses == 5:
        print("        _____\n"
              "        |   O\n"
              "        |  -|\n"
              "        |\n"
              "        |\n\nYou have 3 wrong guesses left."
              )

    if wrong_guesses == 6:
        print("        _____\n"
              "        |   O\n"
              "        |  -|-\n"
              "        |\n"
              "        |\n\nYou have 2 wrong guesses left."
              )

    if wrong_guesses == 7:
        print("        _____\n"
              "        |   O\n"
              "        |  -|-\n"
              "        |  /\n"
              "        |\n\nThis is your last wrong guess."
              )

    #t his is the final guess that draws the hangperson, reveals the word with the
    if wrong_guesses == 8:
        print("        _____\n"
              "        |   O\n"
              "        |  -|-\n"
              "        |  / \ \n"
              "        |\n"
              )

        # ending message, that quits the game after saying the correct word.
        print("You used all your guesses!\n")
        print("The word was " + secret_word)
        print("That means that you've lost the game, " + name + ", better luck next time!.")
        quit()

    # this checks if the number of letters that are guessed correctly, matches with the length of the answer
    # this does have a design bug, because you can guess correct letters multiple times...
    if correct_letters == len(answer):
        print("\n\nThat only took %d tries, " % number_of_tries + name)
        print("You've won the game.\nThat was extraordinarily smart! The word is indeed:")
    print(' '.join(underscores))


    #this was for testing:
    #print(wrong_guesses)
    #print(number_of_tries)
    #print(correct_letters)