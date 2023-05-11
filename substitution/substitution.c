#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    // very first place, program will check whether user provides right information
    // If the user inputs right information, the argument will be 2. (./substitution key)
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // Check the input data whether it is suitable for Key
    string key = argv[1];
    int key_length = strlen(key);

    // input data must contain 26 characters
    if (key_length != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    // check each letter
    for (int i = 0; i < key_length; i++)
    {
        // input data must contain only alphabetic characters
        if (!isalpha(key[i]))
        {
            printf("Key must contain only alphabetic characters.\n");
            return 1;
        }

        // input data must contain each letter exactly once
        for (int j = i + 1; j < key_length; j++)
        {
            // duplication check
            if (tolower(key[i]) == tolower(key[j]))
            {
                printf("Key must contain each letter exactly once.\n");
                return 1;
            }
        }
    }

    // get a text which is going to be encoded
    string plaintext = get_string("plaintext: ");
    printf("ciphertext: ");

    // check each letter
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        // If the letter is alphabetic character,
        if (isalpha(plaintext[i]))
        {
            // do this,
            // check upper or lower
            char base = isupper(plaintext[i]) ? 'A' : 'a';
            int index = plaintext[i] - base;
            char cipher_char = isupper(plaintext[i]) ? toupper(key[index]) : tolower(key[index]);
            printf("%c", cipher_char);
        }
        else
        {
            printf("%c", plaintext[i]);
        }
    }

    printf("\n");
    return 0;
}