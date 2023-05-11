#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Get the name from the user
    string name = get_string("what's your name? ");
    // And print it out
    printf("hello, %s\n", name);

}