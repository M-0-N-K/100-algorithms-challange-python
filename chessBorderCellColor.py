'''
Given two cells on the standard chess board, 
determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", 
the output should be chessBoardCellColor(cell1, cell2) = true.
;

For cell1 = "A1" and cell2 = "H3", 
the output should be chessBoardCellColor(cell1, cell2) = false.


Hints

parseInt()
Input/Output

[time limit] 4000ms (js)
[input] string cell1
[input] string cell2
[output] boolean
true if both cells have the same color, false otherwise.
'''
def chessBoardCellColor(cell1,cell2):
    cell1=[int(ord(cell1[0].lower())-96),int(cell1[1])]
    cell2=[int(ord(cell2[0].lower())-96), int(cell2[1])]
    return (cell1[0]-cell2[0])%2==0 and (cell2[1]-cell1[1])%2==0
print(chessBoardCellColor("A1","C3"))
print(chessBoardCellColor("A1","H3"))