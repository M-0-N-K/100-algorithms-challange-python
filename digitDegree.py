'''
Let's define digit degree of some positive integer as the 
number of times we need to replace this number with the sum of its
 digits until we get to a one digit number.

Given an integer, find its digit degree.

Example

For n = 5, the output should be digitDegree(n) = 0;
For n = 100, the output should be digitDegree(n) = 1. 1 + 0 + 0 = 1.
For n = 91, the output should be digitDegree(n) = 2. 9 + 1 = 10 -> 1 + 0 = 1.
Hints

toString()
parseInt()
split()
reduce()
Input/Output

[time limit] 4000ms (js)

[input] integer n

Guaranteed constraints:

5 ≤ n ≤ 109.

[output] integer
'''
def digitDegree(n):
    count=0
    s=n
    while(s>=10):
        s=sum([int(i) for i in str(s)])
        count+=1
    return count
print(digitDegree(n=5))
print(digitDegree(n=100))
print(digitDegree(n=91))
