'''
This is homework 1 for kids
'''

import random

SAMPLE_SPACE = tuple([str(i) for i in range(1, 10)])
DIGIT_LENGTH = 3


def get_user_input(msg):
    input_data = ''
    ##################################################
    #TODO: get user's input
    assert False, "Unimplemented!"
    ##################################################
    return input_data


def prompt_message(msg):
    ##################################################
    #TODO: show message to user
    assert False, "Unimplemented!"
    ##################################################


def generate_data(sample_space = SAMPLE_SPACE, digit_length = DIGIT_LENGTH):
    data = ""
    indexes = list(range(0, len(sample_space)))
    ##################################################
    #TODO: random sampling (without replace) from sample space
    assert False, "Unimplemented!"
    ##################################################
    return data


def check_length(input_data, digit_length = DIGIT_LENGTH):
    result = False
    ##################################################
    #TODO: check the length
    assert False, "Unimplemented!"
    ##################################################
    return result


def check_unique(intput_data):
    result = False
    ##################################################
    #TODO: check all elements are unique
    assert False, "Unimplemented!"
    ##################################################
    return result


def check_validity(input_data, sample_space = SAMPLE_SPACE):
    ##################################################
    #TODO: check all elements are in sample space
    assert False, "Unimplemented!"
    ##################################################
    return True


def counts_matches(input_data, true_data):
    assert len(input_data) == len(true_data), "The lenght is not correct"
    counts_A = 0
    counts_B = 0
    ##################################################
    #TODO: count each element of input_data
    #A: the counts of matches at the same index
    #B: the counts of matches at different index
    assert False, "Unimplemented!"
    ##################################################
    return (counts_A, counts_B)


def ask_valid_guess(digit_length = 3):
    while 1:
        msg = "!?"
        input_data = get_user_input("Please input your guess:")

        if check_length(input_data) != True:
            ##################################################
            #TODO: modify message
            pass
            ##################################################
        elif check_validity(input_data) != True:
            ##################################################
            #TODO: modify message
            pass
            ##################################################
        elif check_unique(input_data) != True:
            ##################################################
            #TODO: modify message
            pass
            ##################################################
        else:
            break

        prompt_message(msg)

    return input_data

def play_game():
    ##################################################
    #TODO: Implement this mode
    assert False, "Unimplemented!"
    ##################################################


def play_game_computer_guess():
    ##################################################
    #TODO: Implement this mode
    assert False, "Unimplemented!"
    ##################################################


def play_game_human_guess():
    is_match = False
    history = []

    truth = generate_data()

    while 1:
        input_data = ask_valid_guess(DIGIT_LENGTH)
        A, B = counts_matches(input_data, truth)
        history.append((A, B, input_data))
        msg = "A:{0} B:{1} guess:{2} #trails:{3}".format(A, B, input_data, len(history))
        prompt_message(msg)
        if A == DIGIT_LENGTH:
            msg = "Correct! #trials:{0}".format(len(history))
            prompt_message(msg)
            break

    return history


def play_game_two_players():
    ##################################################
    #TODO: Implement this mode
    assert False, "Unimplemented!"
    ##################################################


if __name__ == "__main__":
    #create a new game
    mode = get_user_input("Please enter the mode: 0)Normal, 1)You Guess, 2)Computer Guess, 3)Two players:")
    if mode == '0':
        play_game()
    elif mode == '1':
        play_game_human_guess()
    elif mode == '2':
        play_game_computer_guess()
    elif mode == '3':
        play_game_two_players()
    else:
        prompt_message("You should enter: {0,1,2,3}")

    
