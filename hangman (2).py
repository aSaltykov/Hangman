# Problem Set 2, hangman.py
# Name: Andrey Saltykov
# Collaborators:
# Time spent: 14 hours

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


from string import ascii_lowercase
# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    return all([True if (j in letters_guessed) else False for j in secret_word])


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.

    '''

    nothing = ""
    for j in range(len(secret_word)):
        if secret_word[j] in letters_guessed:
            nothing += secret_word[j]
        else:
            nothing += "_ "
    return nothing


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters = string.ascii_lowercase
    for i in range(len(letters)):
        if letters[i] in letters_guessed:
            letters = letters.replace(letters[i], " ")
    return letters


def user_letters(secret_word):
    return len(set(secret_word))


def check_vallue(input_data: str, letters_guessed: list):
    if input_data == "*":
        return True, ""

    if input_data.isalpha():
        if len(input_data) == 1:
            if input_data not in letters_guessed:
                return True, ""
            else:
                error = "You've already guessed that letter"
        else:
            error = "enter one letter!"
    else:
        error = "It's not a valid !"
    return False, error


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("\nWelcome to the game Hangman!\n")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    attempts = 6
    all_warnings = 3
    score_user = 0
    letters_guessed = []
    print("You have {} warnings left.".format(all_warnings))
    while True:
        print("_ " * 40)
        print("you have guesses left", attempts)
        print("Available letters: " + get_available_letters(letters_guessed))
        input_data = input("please guess a letter: ")
        input_data = input_data.lower()
        all_good, error = check_vallue(input_data, letters_guessed)
        if all_good:
            if input_data in secret_word:

                letters_guessed.append(input_data)
                print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            elif attempts != 0:
                if input_data in ["a", "e", "i", "o", "u"]:
                    attempts -= 2
                else:
                    attempts -= 1
                print("Oops! That letter is not in my word:" + get_guessed_word(secret_word, letters_guessed))
            else:
                print("Sorry, you ran out of guesses.The word was" + str(secret_word))
                break

            if is_word_guessed(secret_word, letters_guessed):
                score_user += (attempts) * user_letters(secret_word)
                print("_ " * 15)

                print("Congratulations, you won!")
                print("Your total score for this game is:" + str(score_user))
                break



        elif all_warnings > 0:

            all_warnings -= 1
            print("Oops! {}. You now have {} warnings: {}".format(error, all_warnings, get_guessed_word(secret_word, letters_guessed)))

        elif attempts > 0:

            attempts -= 1


        else:
            print("-----------")
            print("Sorry, you ran out of guesses. The word was " + secret_word )
            break


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    my_word = my_word.strip()

    if len(my_word) == len(other_word):
        return all(
            [letter == other_word[index] or (letter == '_' and my_word.count(other_word[index]) == 0) for index, letter
             in enumerate(my_word)])

    return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(" ", "")
    suitable = ""

    suitable = " ".join([word for word in wordlist if match_with_gaps(my_word, word)])
    if suitable:
        print(suitable)
    else:
        print("No matches found")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("\nWelcome to the game Hangman with hints!\n")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    attempts = 6
    all_warnings = 3
    score_user = 0
    letters_guessed = []
    print("You have", all_warnings, "warnings left")
    while True:
        print("_ " * 40)
        print("you have guesses left", attempts)
        print("Available letters: " + get_available_letters(letters_guessed))
        input_data = input("please guess a letter: ")
        input_data = input_data.lower()
        all_good, error = check_vallue(input_data, letters_guessed)
        if all_good:
            if input_data in secret_word:

                letters_guessed.append(input_data)
                print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            elif input_data == "*":
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            elif attempts != 0:
                if input_data in ["a", "e", "i", "o", "u"]:
                    attempts -= 2
                else:
                    attempts -= 1
                print("Oops! That letter is not in my word:" + get_guessed_word(secret_word, letters_guessed))
            else:
                print("Sorry, you ran out of guesses.The word was" + str(secret_word))
                break

            if is_word_guessed(secret_word, letters_guessed):
                score_user += (attempts) * user_letters(secret_word)
                print("_ " * 15)

                print("Congratulations, you won!")
                print("Your total score for this game is:" + str(score_user))
                break



        elif all_warnings > 0:

            all_warnings -= 1

            print("Oops! {}. You now have {} warnings: {}".format(error, all_warnings,
                                                                  get_guessed_word(secret_word, letters_guessed)))


        elif attempts > 0:

            attempts -= 1



        else:

            print("-----------")

            print("Sorry, you ran out of guesses. The word was " + secret_word)

            break


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    words = load_words()
    selection = choose_word(words)

    choice = input("Would you like to play with hints ?(ok/no)")
    if choice == "ok":
        hangman_with_hints(selection)
    else:
        hangman(selection)

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.