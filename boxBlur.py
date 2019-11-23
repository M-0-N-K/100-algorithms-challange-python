'''
Last night you had to study, but decided to party instead. 
Now there is a black and white photo of you that is about to go viral. 
You cannot let this ruin your reputation, so you want to apply box blur algorithm 
to the photo to hide its content.

The algorithm works as follows: 
each pixel x in the resulting image has a value equal 
to the average value of the input image pixels' values 
from the 3 × 3 square with the center at x. 
All pixels at the edges are cropped.

As pixel's value is an integer, all fractions should be rounded down.

Example

For

image = [[1, 1, 1], 
        [1, 7, 1], 
        [1, 1, 1]]
the output should be boxBlur(image) = [[1]].

In the given example all boundary pixels were cropped, and the value of the pixel in the middle was obtained as (1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) / 9 = 15 / 9 = rounded down = 1.

Hints

push()
Math.floor()
Input/Output

[time limit] 4000ms (js)
[input] array.array.integer image
An image is stored as a rectangular matrix of non-negative integers.

Guaranteed constraints:

3 ≤ image.length ≤ 10,

3 ≤ image[0].length ≤ 10,

0 ≤ image[i][j] ≤ 255.

[output] array.array.integer
A blurred image.
'''
import math
def boxBlur(pic):
    newPic=[[0]*len(pic[0])]*len(pic)
    print('newPic', newPic)
    for i in range(1,len(pic)-1):
        for j in range(1,len(pic[i])-1):
            box=[[pic[i-1][j-1],pic[i-1][j],pic[i-1][j+1]],
            [pic[i][j-1],pic[i][j],pic[i][j+1]],
            [pic[i+1][j-1],pic[i+1][j],pic[i+1][j+1]]]
            s=sum([sum(row) for row in box])//9
            newPic[i][j]=s
    return [i[1:-1] for i in newPic[1:-1]]

print(boxBlur([[1, 1, 1], 
        [1, 7, 1], 
        [1, 1, 1]]))
        

