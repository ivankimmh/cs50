#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;

    do
    {
        // Prompt user for height until the user inputs a valid number.
        height = get_int("Height : ");
    }
    while (height < 1 || height > 8);

    // Print the pyramids
    for (int i = 0; i < height; i++)
    {
        // Space
        for (int j = height - i - 1; j > 0; j--)
        {
            printf(" ");
        }
        // Hash
        for (int k = 0; k <= i; k++)
        {
            printf("#");
        }
        // the middle
        printf("  ");

        // Hash
        for (int n = 0; n <= i; n++)
        {
            printf("#");
        }
        printf("\n");
    }
}