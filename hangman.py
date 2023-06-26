import random
import sys

def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()

def get_user_input():
    return input('Guess the missing letter: ')

def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name

def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word

#Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    new_word = list()
    answer_word = ""
    char = random.choice(word)
    results = word.find(char)

    for counter in range(0, len(word)):
        if counter == results:
            new_word += char
        else:
            new_word += "_"
    
    for counter in new_word:
        answer_word += counter 
    
    return answer_word

#Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    if (char in original_word) and (char not in answer_word):
        return True
    else:
       return False

#Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    # make a list to keep track of indexes
    new_list = list(answer_word)
    indexes = list()
    new_string = ""

    for counter in range(0, len(original_word)):
        if original_word[counter] == char:
            indexes.append(counter)
    
    # for counter in range(0, len(original_word)):
    #     if counter in indexes:
    #         new_list[counter] = char
    for index in indexes:
        new_list[index] = char

    for counter in new_list:
        new_string += counter 
    
    return new_string

def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)

    return answer


#Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    if number_guesses > 0:
        print(f"Wrong! Number of guesses left: {number_guesses}")
        draw_figure(number_guesses)
    else:
        draw_figure(number_guesses)


#Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    # create a list
    stages = [
    """
/----
|
|
|
|
_______
    """,
    """
/----
|   0
|
|
|
_______
    """,
    """
/----
|   0
|  /|\      
|
|
_______
    """,
    """
/----
|   0
|  /|\\
|   |
|
_______
    """,
    """
/----
|   0
|  /|\\
|   |
|  / \\
_______
    """
    ]

    if number_guesses == 4:
        print(stages[0])
    elif number_guesses == 3:
        print(stages[1])
    elif number_guesses == 2:
        print(stages[2])
    elif number_guesses == 1:
        print(stages[3])
    elif number_guesses == 0:
        print(stages[4])

#Step 2 - update to loop over getting input and checking until whole word guessed
#Step 3 - update loop to exit game if user types `exit` or `quit`
#Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):
    print("Guess the word: "+answer)
    number_of_tries = 5
    while True:
        guess = get_user_input()
        if guess == "exit" or guess == "quit":
            print("Bye!")
            break

        if is_missing_char(word, answer, guess) == True:
            answer = do_correct_answer(word, answer, guess)

            if word == answer:
                break     
            
        elif is_missing_char(word, answer, guess) == False:
            number_of_tries -= 1
            do_wrong_answer(answer, number_of_tries)
            
            if number_of_tries == 0:
                print(f"Sorry, you are out of guesses. The word was: {word}")
                break

        # if user input == exit or quit, breaks out pf the loop
       
        # if the user guesses a random letter, checks if the input is in the word 
        # if that returns True, fills in the answer word and returns a more i
        


#Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)

