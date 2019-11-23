#!python
import random
import sys

words = []
placed_words = []
all_letters = []
rows = 30
cols = 30
grid = []

def main():

    # Check the command line - we should have an input file of words
    # and an output file to write to
    if len(sys.argv) != 3:
        print("Command line is word_search.py [file of words to place] [output file]")
        exit(1)

    # Read the words
    with open(sys.argv[1]) as file:
        for line in file:
            words.append(line.strip().upper())

    # Create a matrix to put the data in
    for _ in range(rows):
        grid.append([None] * cols)

    # Place each individual word
    for word in words:
        place_word(word)

    # Use the same letters as are in the words to fill the blanks
    for letter in "".join(placed_words):
        all_letters.append(letter)

    # Fill the blanks
    fill_grid()

    # Print the result
    print_grid()

def fill_grid ():
    for c in range(cols):
        for r in range(rows):
            if grid[r][c] is None:
                grid[r][c] = random.choice(all_letters)


def place_word(word):
    possible_placements = []

    orientation_functions = [
        # Forward
        lambda x,y: (x+1,y),
        # Backwards
        lambda x,y: (x-1,y),
        # Down
        lambda x,y: (x,y+1),
        # Up
        lambda x,y: (x,y-1),
        # Diag TL - BR
        lambda x,y: (x+1,y+1),
        # Diag BR - TL
        lambda x,y: (x-1,y-1),
        # Diag BL - TR
        lambda x,y: (x+1,y-1),
        # Diag TR - BL
        lambda x,y: (x-1,y+1)
    ]


    for r in range(rows):
        for c in range(cols):
            for orientation in orientation_functions:
                # See if we can put this word at this location using the 
                # current orientation transform

                thisR = r
                thisC = c
                crosses = False
                fail = False

                for letter in word:
                    if thisR >=rows or thisC >= cols or thisR < 0 or thisC < 0:
                        fail = True
                        break

                    # It's OK to place this letter if the space is empty, or has the same
                    # letter there already
                    if grid[thisR][thisC] is not None and grid[thisR][thisC] != letter:
                        fail = True
                        break

                    # We want to prefer positions which cross another word just to make 
                    # things more interesting.
                    if grid[thisR][thisC] is not None and grid[thisR][thisC] == letter:
                        crosses = True


                    thisC,thisR = orientation(thisC, thisR)
                

                if not fail:
                    weight = 1
                    if crosses:
                        weight = 50
                    
                    for _ in range(weight):
                        possible_placements.append([r,c,orientation])



    if len(possible_placements) > 0:
        # Randomly pick a possible placement
        placement = random.choice(possible_placements)
        placed_words.append(word)

        thisR = placement[0]
        thisC = placement[1]

        for letter in word:
            grid[thisR][thisC] = letter
            thisC, thisR = placement[2](thisC, thisR)

    else:
        print("Couldn't place {}".format(word))


def print_grid():
    with open(sys.argv[2],"w") as file:
        for line in grid:
            file.write(" ".join(x if x is not None else "." for x in line))
            file.write("\n")
            #print(" ".join(x if x is not None else "." for x in line))

        file.write("\n\n")
        #print("\n\n")
        placed_words.sort()
        file.write("\n".join(placed_words))
        #print("\n".join(placed_words))


if __name__ == "__main__":
    main()