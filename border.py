'''
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
       "ded"]
the output should be

addBorder(picture) = ["*****",
                  "*abc*",
                  "*ded*",
                  "*****"]
Hints

concat()
unshift()
push()
Input/Output

[time limit] 4000ms (js)
[input] array.string picture
A non-empty array of non-empty equal-length strings.

Guaranteed constraints:

1 ≤ picture.length ≤ 5,

1 ≤ picture[i].length ≤ 5.

[output] array.string
The same matrix of characters, framed with a border of asterisks of width 1.
'''
def addBorder(lists):
    lists=['*'+i+'*' for i in lists]
    lists.insert(0,'*'*(len(lists[0])))
    lists.append('*'*len(lists[0]))
    return lists

    
print(addBorder(["abc",
       "ded"]))