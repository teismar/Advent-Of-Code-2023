# Part 2
One original list for all possible games.

A new list is created for each card that is won.

`[("GameID" , [game]), ...]`


Iterate over the original list, and for each card add the won cards to the list of won cards.

Rekursion:

function(list, counter)
    if won:
        add won cards to list
        remove current card from list
        function(list, counter + 1)
    else:
        remove current card from list
        function(list, cou`nter + 1)