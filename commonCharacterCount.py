'''
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

Hints

split()
hasOwnProperty()
Input/Output

[time limit] 4000ms (js)
[input] string s1
A string consisting of lowercase latin letters a-z.

Guaranteed constraints:

1 ≤ s1.length ≤ 15.

[input] string s2
A string consisting of lowercase latin letters a-z.

Guaranteed constraints:

1 ≤ s2.length ≤ 15.

[output] integer
'''
def commonCharacterCount(s1,s2):
    counts=0
    for i in s1:
        if i in s2:
            counts+=1
            index=s2.index(i)
            s2=s2[:index]+s2[index+1:]
    return counts
print(commonCharacterCount(s1 = "aabcc" , s2 = "adcaa"))
