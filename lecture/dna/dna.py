import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        """check if it is not 3 ~"""
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit()

    # TODO: Read database file into a variable
    with open(sys.argv[1], "r") as file:
        """second argument / read mode"""
        reader = csv.reader(file)
        # 2차원 리스트 [[],[],[]]
        database = [row for row in reader]

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as file:
        """Third argument / read mode"""
        sequence = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    # must know what I should look for
    str_list = database[0][1:]
    str_counts = []
    for string in str_list:
        str_counts.append(longest_match(sequence, string))
        # print(str_counts)
    # TODO: Check database for matching profiles
    # compare to the sequence
    for row in database[1:]:
        # print(list(map(int, row[1:])))
        if str_counts == list(map(int, row[1:])):
            # print the name
            print(row[0])
            returnc

    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of onsecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
