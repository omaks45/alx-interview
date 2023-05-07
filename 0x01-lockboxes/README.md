
You have n number of locked boxes in front of you. Each box is numbered sequentially 
from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False


We have to Iterate through the unlocked box, alongside 
the iteration of the key to each of the box in the boxes and check if 
the key is within the length of the boxes i.e if the key opens a locked box, 
the key is appended to the queue of the unlocked boxes.
when the key is done unlocking we have to check 
if the number of unlocked is equivalent to the length of the boxes
