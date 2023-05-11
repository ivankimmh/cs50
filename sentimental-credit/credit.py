# TODO
from cs50 import get_int

def main():

      # get the card number from the user first
     card_number = get_int("Number: ")
     num = card_number
      # initialise variables
     sum = 0
     i = 0
      # last digit
     last_digit = num % 10
      # rest of numbers
     num //= 10

     while num != 0:
          print("num is :", num)
          digit = num % 10
          print("digit is :", digit)
          if i % 2 == 0:
               doubled = digit * 2
               if doubled > 9:
                    # add 나머지 & 몫
                    print("doubled in doubled is :", doubled)
                    sum += doubled % 10
                    print("sum in doubled is :", sum)
                    sum += doubled // 10
                    print("doubled / 10 is :", doubled / 10)
                    print("sum in doubled2 is :", sum)
               else:
                    sum += doubled
                    print("sum in doubled2 is :", sum)
          else:
               sum += digit
               print("sum in else is :", sum)
          i += 1
          num //= 10
     # add the last digit as well
     sum += last_digit
    #  print("sum is :", sum)
     # check for invalid card number
     if sum % 10 != 0:
          print("INVALID")
          return

     length = i + 1
    #  print("length is :", length)
     first_two_digits = card_number // (10 ** (length - 2))
    #  print("first_two_digits is :", first_two_digits)

     if length == 15 and (first_two_digits == 34 or first_two_digits == 37):
        print("AMEX")
     elif length == 16 and (first_two_digits >= 51 and first_two_digits <= 55):
        print("MASTERCARD")
     elif (length == 13 or length == 16) and (first_two_digits // 10 == 4):
        print("VISA")
     else:
        print("INVALID")


main()