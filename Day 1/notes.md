# My Notes for this day

## Part 1
This was a pretty simple problem. I just had to read in the file and then concatenate the first and last integers of each line. I then converted the resulting string to an integer and added it to a running total. I then printed the total.

## Part 2
This was a bit tricky, since the example had the case missing where it would be obvious that one letter could be used by 2 numbers.

My solution was to replace "one" with "1ne" to keep the rest of the letters. Afterward I first searched (without replacing) for all the numbers and saved those with their starting index. Now i can easiley start with the leftmost number and so I fixed the overlapping Problem. Since now I could be sure to, that to the left of my current wordnumber there is no other number that needs letters, I could just replace the wordnumber with the number and continue. I did this until there were no more numbers left.

For the rest of the logic I just imported the function from part 1 and used it to calculate the sum of the numbers.