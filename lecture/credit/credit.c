#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get the card number from the user
    long card_number = get_long("Number: ");
    // Make num to use it
    long num = card_number;
    int sum = 0;
    int i = 0;
    // The last digit will be apart
    int last_digit = num % 10;
    num /= 10;

    // Make the sum
    while (num != 0)
    {
        int digit = num % 10;
        // Index from 0, 2, 4 ...
        if (i % 2 == 0)
        {
            int doubled = digit * 2;
            if (doubled > 9)
            {
                sum += doubled % 10;
                sum += doubled / 10;
            }
            else
            {
                sum += doubled;
            }
        }
        // Index from 1, 3, 5 ...
        else
        {
            sum += digit;
        }
        i++;
        num /= 10;
    }
    // Add the last digit as well
    sum += last_digit;
    // Check for invalid card numbers
    if (sum % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }
    int value = card_number / 1000000000000000;
    // Check if card is an AMEX, MasterCard, or Visa
    if (i + 1 == 15 && (card_number / 10000000000000 == 34 || card_number / 10000000000000 == 37))
    {
        printf("AMEX\n");
    }
    else if (i + 1 == 16 && (card_number / 100000000000000 == 51 || card_number / 100000000000000 == 52
    || card_number / 100000000000000 == 53 || card_number / 100000000000000 == 54 || card_number / 100000000000000 == 55))
    {
        printf("MASTERCARD\n");
    }
    else if (((i + 1 == 13 && (card_number / 1000000000000 == 4))
    || ((i + 1 == 14) && (card_number / 10000000000000 == 4))
    || ((i + 1 == 15) && (card_number / 100000000000000 == 4))
    || ((i + 1 == 16) && (card_number / 1000000000000000 == 4))))
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
    return 0;
}
