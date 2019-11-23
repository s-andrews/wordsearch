# Word Search
This is a little program I wrote to automatically create word search grids.

It takes in a file of words (one per line) to place in a 30x30 grid and writes the output, along with the words it sucessfully placed into a new text file.

The command line is:

```
word_search.py [file of input words] [output file to write to]
```

The program places words in all possible orientations

* Left to right
* Right to left
* Top to bottom
* Bottom to top
* Bottom left to top right
* Top left to bottom right
* Bottom right to top left
* Top right to bottom left

Words are placed in the order in which they were found in the file.  The program will heavily (10X) favour placements which cause a new word to intersect with a previous word.  Any words which can't be placed will generate a warning message and will not be written into the final list of placed words.  Since placement involves a random element it's possible that re-running the program will cause previously unplaced words to be included.

After all words have been placed the remainder of the grid is filled with random letters.  These letters are drawn from the letters of the words which were placed so the composition will match between real and random letters.

Upon completion the program will write out the newly encoded word grid as well as a list of the successully placed words in alphabetical order.

