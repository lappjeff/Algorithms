#!/usr/bin/python

import sys

# Write a function rock_paper_scissors to generate all of the possible plays that can be made in a game of "Rock Paper Scissors", given some input n, which represents the number of plays per round.


#rock_paper_scissors(1)
#Options
#rock
#paper
#scissors

#rock_paper_scissors(2)
#Options
# rock, rock - added rock to rock
# rock, paper - added paper to rock
# rock, scissors - added scissors to rock
# paper, rock - added rock to paper
# paper, paper - added paper to paper
# paper, scissors - added scissors to paper
# scissors, rock - added rock to scissors
# scissors, paper - added paper to scissors
# scissors, scissors - added scissors to scissors

#rock_paper_scissors(3)
# rock, rock, rock - added rock to rock, rock
# rock, rock, paper - added paper to rock, rock
# rock, rock, scissors - added scissors to rock, rock
# rock, paper, rock - added rock to rock, paper
# rock, paper, paper - added paper to rock, paper
# rock, paper, scissors - added scissors to rock, paper



def rock_paper_scissors(n):
    #list of all possible plays - rock, paper, scissors
    possible_plays = ["rock", "paper", "scissors"]

    result = []

    def handle_list(arr, n):

        if n == 0:
            return result.append(arr)


        print(f"Current array: {arr}")

        for play in possible_plays:
            handle_list(arr + [play], n - 1)


    #recursive function

        #run recursion until count = n

    #call recursive function with starting data
    handle_list([], n)
    return result


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')


# Another problem that asks you to generate a bunch of permutations, so we're probably going to want to opt for using recursion again. Since we're building up a list of results, we'll have to pass the list we're constructing around to multiple recursive calls so that each recursive call can add to the overall result. However, the tests only give our function n as input. To get around this, we could define an inner recursive helper function that will perform the recursion for us, while allowing us to preserve the outer function's function signature.

# In Python, you can concatenate two lists with the + operator. However, you'll want to make sure that both operands are lists!

# If you opt to define an inner recursive helper function, don't forget to make an initial call to the recursive helper function to kick off the recursion.

# You'll want to define a list with all of the possible Rock Paper Scissors plays.
# rock
# paper
# scissors
