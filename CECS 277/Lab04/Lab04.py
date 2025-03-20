# Thaw Han, Achal Mohandas
# 02/25/2025
# State Capital Quiz: This is a program that quizzes the user on the capitals of the states in the United States. The program reads the states and capitals from a file and asks the user 10 questions. The user is given 4 choices for each question and must select the correct capital. The program keeps track of the number of correct answers and displays the score at the end of the quiz.

import random

def read_file_to_dict(file_name):
    '''
    Reads a file and returns a dictionary with the state as the key and the capital as the value.
    :param file_name: the name of the file to read
    :return: a dictionary with the state as the key and the capital as the value
    '''
    dictionary = {} # create an empty dictionary
    with open(file_name, 'r') as file:  # open the file
        for line in file:
            state, capital = line.strip().split(',') # split the line into state and capital
            dictionary[state] = capital # add the state and capital to the dictionary
    return dictionary

def get_random_state(states):
    '''
    Returns a random state and its capital from the dictionary.
    :param states: the dictionary of states and capitals
    :return: a tuple with the state as the first element and the capital as the second element
    '''
    state_capital_list = list(states.items()) # convert the dictionary to a list of tuples
    return random.choice(state_capital_list) # return a random tuple

def get_random_choices(states, correct_capital):
    '''
    Returns a list of 4 random choices for the user to choose from.
    :param states: the dictionary of states and capitals
    :param correct_capital: the correct capital
    :return: a list of 4 choices
    '''
    capitals = list(states.values()) # get a list of all the capitals
    capitals.remove(correct_capital) # remove the correct capital
    incorrect_choices = random.sample(capitals, 3) # get 3 random incorrect capitals
    choices = incorrect_choices + [correct_capital] # add the correct capital
    random.shuffle(choices) # shuffle the choices
    return choices

def ask_question(correct_state, possible_answers):
    '''
    Asks the user a question and returns the index of the user's choice.
    :param correct_state: the correct state
    :param possible_answers: a list of possible answers
    :return: the index of the user's choice
    '''
    print(f"The capital of {correct_state} is: ")
    options = ['A', 'B', 'C', 'D']
    for i, choice in enumerate(possible_answers): # print the choices
        print(f"    {options[i]}. {choice}", end = " ") # print the choice

    while True: # loop until the user enters a valid choice
        user_input = input("\nEnter selection: ").upper()
        if user_input in options:
            return options.index(user_input)    # return the index of the user's choice 0-3
        else:
            print("Invalid input. Input choice A-D.")
            
def main():
    states = read_file_to_dict("statecapitals.txt")
    print("- State Capital Quiz -")
    score = 0

    for question_number in range(1, 11): # ask 10 questions
        correct_state, correct_capital = get_random_state(states)
        choices = get_random_choices(states, correct_capital)
        correct_index = choices.index(correct_capital)

        print(f"\n{question_number}.", end = " ")
        user_choice = ask_question(correct_state, choices) # ask the user a question

        if user_choice == correct_index:    # check if the user's choice is correct
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_capital}.")

    print(f"\nEnd of test. You got {score} correct.")

if __name__ == "__main__":
    main()
