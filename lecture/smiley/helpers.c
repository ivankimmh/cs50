#include "helpers.h"

// Function to colorize the image
void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    // Define the new color for black pixels (whatever)
    RGBTRIPLE newColor;

    newColor.rgbtBlue = 255;
    newColor.rgbtGreen = 255;
    newColor.rgbtRed = 100;

    // Loop through each pixel in the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE pixel = image[i][j];

            // Check if the pixel is black (all colors are 0 : RGB black #000000 : rgb(0, 0, 0))
            if (pixel.rgbtBlue == 0 && pixel.rgbtGreen == 0 && pixel.rgbtRed == 0)
            {
                // Change the black pixel to the new color(I've declared above)
                image[i][j] = newColor;
            }
        }
    }
}
