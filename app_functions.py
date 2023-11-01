"""
Functions used by the math education game app.
These functions must be called from the main.py file, as appropriate.
"""

import random


def roll_die():
    """
    Generates a pseudo-random integer between the 1 and 6, inclusive.
    Use the function random.randint() to generate the pseudo-random number.

    :returns: the pseudo-random integer.
    """
    # complete this function below here


def get_question_type():
    """
    Pseudo-randomly decides whether to give an addition question or a subtraction question.
    Use the function random.randint() to generate a pseudo-random number between 1 and 6, inclusive, that is used to determine the question type.

    :returns: "sum" for an addition question, "difference" for a subtraction question.
    """
    # complete this function below here


def print_question(die_1_value, die_2_value, question_type):
    """
    Prints out a math question that asks the user to calculate either the sum or difference of the two numbers rolled on virtual dice.

    Follow the given format for each type of question:
    - "You rolled a 3 and a 5... What is the sum of 3 and 5?"
    - "You rolled a 3 and a 5... What is the difference between 3 and 5?"

    A few notes:
    - You must use the format function to plug in the numbers into the printed text template.

    :param die_1_value: The first integer.
    :param die_2_value: The second integer.
    :param question_type: A string - either "sum" or "difference" - indicating whether the user should calculate the sum or difference of the two integers.
    :returns: None
    """
    # complete this function below here


def input_answer():
    """
    Asks the user to enter their answer to the most recent question.

    A few notes:
    - Remove any leading and trailing whitespace from the user's response.
    - If the user enters a response that is not valid, including empty responses or responses including non-integer characters, return -1.

    :returns: The user's answer, as an int, if valid; or -1 if the user's response was not valid.
    """
    # complete this function below here


def is_correct_answer(die_1_value, die_2_value, question_type, given_answer):
    """
    Determines whether the user's given answer to a question is correct.
    - For difference questions, users are expected to calculate the absolute value of the difference.

    :param die_1_value: The first integer.
    :param die_2_value: The second integer.
    :param question_type: A string - either "sum" or "difference" - indicating whether the user was asked to add or subtract the two integers.
    :returns: True if the user's given answer is correct, False otherwise.
    """
    # complete this function below here


def print_congratulations(question_type):
    """
    Congratules the user for answering a question correctly.

    Follow the given format for each type of question:
    - "Yes! Congratulations on the successful addition!"
    - "Yes! Congratulations on the successful subtraction!"

    :param question_type: A string - either "sum" or "difference" - indicating whether the user was asked to add or subtract the two integers.
    """
    # complete this function below here


def print_correct_answer(die_1_value, die_2_value, question_type):
    """
    Prints the correct answer to the question.

    Follow the given format for each type of question:
    - "No! The sum of 3 and 5 is 8!"
    - "No! The difference between 3 and 5 is 2!"

    :param die_1_value: The first integer.
    :param die_2_value: The second integer.
    :param question_type: A string - either "sum" or "difference" - indicating whether the user was asked to add or subtract the two integers.
    """
    # complete this function below here


def print_error_message():
    """
    Prints an error message indicating that the user has given an invalid response.

    Follow the given format:
    - "Sorry - that is an invalid answer.  Bye Bye!"
    """
    # complete this function below here
