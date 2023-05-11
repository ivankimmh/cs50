// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <stdio.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
// default = 26, to two to the power of sixteen
// just a reasonale large number as an assumption ...
const unsigned int N = 65536;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    // get the hash index for the word
    unsigned int index = hash(word);
    // set the cursor to the first node in the linked list
    node *cursor = table[index];

    // traverse the linked list
    while (cursor != NULL)
    {
        // compare the word and dont care about whether it is capital or small
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    // initialise hash value
    unsigned int hash_value = 0;
    // interate through characters in the word
    for (int i = 0; word[i] != '\0'; i++)
    {
        // update hash value with the product of the previous value
        // a constant, and the current character
        hash_value = (hash_value * 31 + tolower(word[i])) % N;
    }
    return hash_value;
    // return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // open file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    char buffer[LENGTH + 1];
    // read words from the dictionart file
    while (fscanf(file, "%s", buffer) != EOF)
    {
        // allocate memory for new node,
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            fclose(file);
            return false;
        }
        // copy the word into the new node
        strcpy(new_node->word, buffer);
        // get the hash index for the word
        unsigned int index = hash(new_node->word);
        // point the new node to the first node in the linked list
        new_node->next = table[index];
        // update the hash table entry to point to the new node
        table[index] = new_node;
    }
    // close the dictionay file
    fclose(file);
    // successfully loaded the dictionary
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    unsigned int count = 0;
    // interate through each bucket in the hash table
    for (int i = 0; i < N; i++)
    {
        // set cursor to the first node in the linked list
        node *cursor = table[i];
        while (cursor != NULL)
        {
            count++;
            // move to the next node in the linked list
            cursor = cursor->next;
        }
    }
    // return the total word count
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    // interate through the hash table
    for (int i = 0; i < N; i++)
    {
        // set a cursor to the head of the linked list at the index
        node *cursor = table[i];
        // free the nodes in the likend list
        while (cursor != NULL)
        {
            // set a temporary pointer to the current node
            node *temp = cursor;
            // move the cursor to the next node
            cursor = cursor->next;
            // free the memory the current node
            free(temp);
        }
    }
    // return true after unloading all nodes in the hash table
    return true;
}
