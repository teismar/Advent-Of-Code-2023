# Part 1
I will parse the input to a matrix of characters.
Then I will iterate over the matrix and for each character I will check if it is a number or not.
If it is a number I will look to the right to get the complete number.

Now I will check for the presence of a symbol around the number to see if it should be added.

# Part 2
I will do the same as part 1 but this time a number is only valid if the symbol is a '*'. Also i first save them in a tuple with the position of the star.
Afterwards I will iterate over the list of tuples and check for numbers with the same symbol position, those will be multiplied and added to the result.