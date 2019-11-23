'''
Given the positions of a white bishop and a black pawn on the standard chess board, 
determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited 
to diagonal movement. Check out the example below to see how it can move:
Example

For bishop = "a1" and pawn = "c3", the output should be bishopAndPawn(bishop, pawn) = true.


Hint

parseInt()
Input/Output

[time limit] 4000ms (js)
[input] string bishop
Coordinates of the white bishop in the chess notation.

[input] string pawn
Coordinates of the black pawn in the same notation.

[output] boolean
true if the bishop can capture the pawn, false otherwise.
'''
def bishopAndPawn(bishop,pawn):
    bishop=[int(ord(bishop[0])-96),int(bishop[1])]
    pawn=[int(ord(pawn[0])-96), int(pawn[1])]
    return abs(bishop[0]-pawn[0])==abs(bishop[1]-pawn[1])
print(bishopAndPawn("a1","c3"))
print(bishopAndPawn("a8","h1"))