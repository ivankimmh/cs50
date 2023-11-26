#include "helpers.h"
#include "math.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // going to check all height
    for (int i = 0; i < height; i++)
    {
        // going to check all width
        for (int j = 0; j < width; j++)
        {
            // define pixel
            RGBTRIPLE pixel = image[i][j];
            // find the avg.
            int average = round((pixel.rgbtRed + pixel.rgbtGreen + pixel.rgbtBlue) / 3.0);
            // replace values to avg.
            image[i][j].rgbtRed = image[i][j].rgbtGreen = image[i][j].rgbtBlue = average;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE pixel = image[i][j];
            // declare variables to use
            int originalRed = pixel.rgbtRed;
            int originalGreen = pixel.rgbtGreen;
            int originalBlue = pixel.rgbtBlue;

            // replace values
            image[i][j].rgbtRed = fmin(round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue), 255);
            image[i][j].rgbtGreen = fmin(round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue), 255);
            image[i][j].rgbtBlue = fmin(round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue), 255);
        }
    }
}


// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        // filter two pixel at a time (mirroring)
        // j = 0 should go to the last, and j = width -1 should go to the first
        for (int j = 0; j < width / 2; j++)
        {
            // use a temp variable to replace the reflected pixel
            RGBTRIPLE temp = image[i][j];
            // I start with i = 0, j = 0
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // make copy to save it somewhere else
    RGBTRIPLE copy[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // declare variables to save avg values
            int sumRed = 0;
            int sumGreen = 0;
            int sumBlue = 0;
            int count = 0;

            // -1 -1, 0 -1, 1 -1
            // -1 0, 0 0, 1 0
            // -1 1, 0 1, 1 1
            for (int k = -1; k <= 1; k++)
            {
                for (int l = -1; l <= 1; l++)
                {
                    // find surrounded pixels to sum
                    int newRow = i + k;
                    int newCol = j + l;

                    if (newRow >= 0 && newRow < height && newCol >= 0 && newCol < width)
                    {
                        sumRed += copy[newRow][newCol].rgbtRed;
                        sumGreen += copy[newRow][newCol].rgbtGreen;
                        sumBlue += copy[newRow][newCol].rgbtBlue;

                        // i was so confused whilst gettinfg the count....
                        count++;
                    }
                }
            }

            image[i][j].rgbtRed = round((float)sumRed / count);
            image[i][j].rgbtGreen = round((float)sumGreen / count);
            image[i][j].rgbtBlue = round((float)sumBlue / count);
        }
    }
}
