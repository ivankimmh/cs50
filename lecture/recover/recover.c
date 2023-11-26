#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // firstly, check input
    if (argc != 2)
    {
        printf("It is unavailable, Usage: ./recover card.raw\n");
        return 1;
    }

    // check raw file
    FILE *raw_file = fopen(argv[1], "r");

    // check the pointer
    if (raw_file == NULL)
    {
        printf("Could not open file, please try again\n");
        return 2;
    }

    // declare unsigned variable
    unsigned char buffer[512];

    // the number of image
    int countImage = 0;

    FILE *output = NULL;

    // going to save the filename
    char *filename = malloc(8 * sizeof(char));

    // reach to the end of file
    while (fread(buffer, sizeof(char), 512, raw_file))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (output != NULL)
            {
                fclose(output);
            }
            sprintf(filename, "%03i.jpg", countImage);
            output = fopen(filename, "w");
            countImage++;
        }

        if (output != NULL)
        {
            fwrite(buffer, sizeof(char), 512, output);
        }
    }

    free(filename);

    if (output != NULL)
    {
        fclose(output);
    }

    fclose(raw_file);

    return 0;
}
