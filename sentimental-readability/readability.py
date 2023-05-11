# TODO
import math
import string
from cs50 import get_string


def count_letters(text):
    """Function to count the number of letters in the text"""
    count = 0
    for c in text:
        if c.isalpha():
            count += 1
    return count


def count_words(text):
    """Function to count the number of words in the text"""
    count = 0
    # space, dont need to worry about the number of words
    for word in text.split():
        count += 1
    return count


def count_sentences(text):
    """Function to count the number of sentences in the text"""
    count = 0
    for c in text:
        if c in [".", "!", "?"]:
            count += 1
    return count


def main():
    """Main function"""
    # Get input text from the user
    text = get_string("Text: ")

    # Calculate the number of letters, words, and sentences
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Calculate the averages per 100 words
    L = (letters / words) * 100
    S = (sentences / words) * 100

    # Calculate the Coleman-Liau index
    index = round(0.0588 * L - 0.296 * S - 15.8)

    # Output the grade level
    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


main()