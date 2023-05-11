#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
// preference 는 2차배열이고, 1x1 은 100 까지  1x2 는 9 까지 인덱스를 가지는 배열
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
}
candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

// will take the arguments from the user
int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        // the argument part must be longer than 2
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    // the first argc is "./runoff"
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }

    // once the input is valid,
    // update the array of candidates along with input data
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    // How many voters are going to be doing this?
    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    // 입력값 만큼 돌면서,
    for (int i = 0; i < voter_count; i++)
    {
        // Query for each rank
        // 출마한 인원들 수 만큼 돌면서,
        for (int j = 0; j < candidate_count; j++)
        {
            // get_string will be shown with rank
            // And, user inputs the name for each rank
            string name = get_string("Rank %i: ", j + 1);

            // execute function vote,
            // Record vote, unless it's invalid
            // i = voter, j = rank, name = name
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }
        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        // function find_min should return min value of min_votes
        int min = find_min();
        bool tie = is_tie(min);

        // If tie is true == none of them has two conditions which are
        // not dead and has more than min_votes
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                // at least alive == not dead but min_vote even if it is under half of votes_count
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        // == if tie still returns false,
        // == can go further
        eliminate(min);

        // Reset vote counts back to zero
        // calculate them all again after elimination
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
// everytime user input the name along with prompted rank,
bool vote(int voter, int rank, string name)
{
    // TODO
    for (int i = 0 ; i < candidate_count; i++)
    {
        if (strcmp(candidates[i].name, name) == 0)
        {
            preferences[voter][rank] = i;
            return true;
        }
    }
    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    // TODO
    // repeat it as many time as the number of voters
    for (int i = 0; i < voter_count; i++)
    {
        // repeat it as many time as the number of candidates
        for (int j = 0; j < candidate_count; j++)
        {
            int index = preferences[i][j];

            // check the ballot from the front of array,
            // if the index is alive, votes++ and end it to go next ballot
            if (!candidates[index].eliminated)
            {
                candidates[index].votes++;
                break;
            }
        }
    }
    return;
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        // only one person
        if (candidates[i].votes > (voter_count / 2))
        {
            printf("%s\n", candidates[i].name);
            return true;
        }
    }
    return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    // TODO
    // initialize min_vote as max so can be replced lower value,
    int min_votes = voter_count;
    for (int i = 0; i < candidate_count; i++)
    {
        if (!candidates[i].eliminated && candidates[i].votes < min_votes)
        {
            min_votes = candidates[i].votes;
        }
    }
    // return min_votes value
    return min_votes;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        // not eliminated candidate, not the same to min votes
        if (!candidates[i].eliminated && candidates[i].votes != min)
        {
            return false;
        }
    }
    return true;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    // TODO
    // have to check all candidates so no return untill it finishes all
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == min)
        {
            candidates[i].eliminated = true;
        }
    }
}