# TODO
from cs50 import get_int


# make the # as requested
def main():
    height = get_height()
    for i in range(height):
        for j in range(height - i - 1):
            print(" ", end="")

        for k in range(i + 1):
            print("#", end="")

        print("  ", end="")

        for l in range(i + 1):
            print("#", end="")
        print("")


# get height from user
def get_height():
    while True:
        n = get_int("Height: ")
        if 0 < n < 9:
            return n


main()