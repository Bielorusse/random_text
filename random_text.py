"""
Mix the words of a source text to create a random one.

Version 0.2 of the 20181109.
"""

import argparse
import random

def clean_latex_text(input_file):
    """
    Reads text file containing latex text and clears everything linked to latex formatting.

    Input:
    -input_file         string
    Output:
    -output_contents    list of strings
    """

    output_contents = []

    with open(input_file, "r") as file:

        input_contents = file.readlines()

    for row in input_contents:

        for word in row.split():

            if not word.startswith("\\") and not word.startswith("%"):

                output_contents.append(word)

    for i, row in enumerate(output_contents):

        output_contents[i] = row.replace("}", "")

    return output_contents

def remove_uppercase(input_words):
    """
    Remove the uppercase of the beginning of sentences in a list of words.

    Input:
    -input_words    list of strings
    Ouput:
    -output_words   list of strings
    """

    output_words = [input_words[0]]

    for i in range(len(input_words[:-1])):

        if input_words[i].endswith("."):

            output_words.append(input_words[i+1].lower())

        else:

            output_words.append(input_words[i+1])

    return output_words

def add_uppercase(input_words):
    """
    Remove the uppercase of the beginning of sentences in a list of words.

    Input:
    -input_words    list of strings
    Ouput:
    -output_words   list of strings
    """

    output_words = [input_words[0].capitalize()]

    for i in range(len(input_words[:-1])):

        if input_words[i].endswith("."):

            output_words.append(input_words[i+1].capitalize())

        else:

            output_words.append(input_words[i+1])

    output_words[-1] = "{}.".format(output_words[-1])

    return output_words

def randomize_list_of_words(input_words):
    """
    Returns the same list of words in a random order.

    Input:
    -input_words    list of strings
    Output:
    -output_words   list of strings
    """

    output_words = []

    random_order = random.sample(range(len(input_words)), len(input_words))

    for i in random_order:

        output_words.append(input_words[i])

    return output_words

def random_newlines(words_list, nb_of_newlines):
    """
    Distribute randomly a given number of newline characters in a list of words.

    Input:
    -words_list         list of strings
    -nb_of_newlines     integer
    Output:
    -words_list         list of strings
    """

    period_indexes = []

    for i, word in enumerate(words_list):

        if "." in word:

            period_indexes.append(i + 1)

    if nb_of_newlines > len(period_indexes):
        nb_of_newlines = len(period_indexes)

    newline_indexes = random.sample(period_indexes, nb_of_newlines)

    for index in newline_indexes:

        words_list.insert(index, "\n\n")

    return words_list

if __name__ == "__main__":

    parser = argparse.ArgumentParser("Random text.")
    parser.add_argument("-input", help="input text file")
    parser.add_argument("-output", help="output text file")
    args = parser.parse_args()

    source_words = clean_latex_text(args.input)

    source_words_wo_uppercase = remove_uppercase(source_words)

    random_words_wo_uppercase = randomize_list_of_words(source_words_wo_uppercase)

    random_words = add_uppercase(random_words_wo_uppercase)

    with open("{}_1.txt".format(args.output[:-4]), "w") as file:

        for word in random_words:

            file.write(
                "{} ".format(word)
            )

    random_words = random_newlines(random_words, 3)

    with open("{}_2.txt".format(args.output[:-4]), "w") as file:

        for word in random_words:

            file.write(
                "{} ".format(word)
            )
