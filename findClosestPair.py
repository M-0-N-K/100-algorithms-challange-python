'''
Given an array of integers numbers, we'd like to find the closest pair of elements that add up to sum. Return the distance between the closest pair (absolute difference between the two indices). If there isn't a pair that adds up to sum, return -1.

Example

For numbers = [1, 0, 2, 4, 3, 0] and sum = 5 the output should be findClosestPair(numbers, sum) = 2. 1 and 4 have a sum of 5, but 2 and 3 are closer.

For numbers = [2, 3, 7] and sum = 8 the output should be findClosestPair(numbers, sum) = -1. There are no pairs that have a sum of 8.

Hints

Math.abs()
Input/Output

[execution time limit] 5 seconds (ts)

[input] array.integer numbers

An array of integers.

Guaranteed constraints:

2 ≤ numbers.length ≤ 3 · 105 -1000 ≤ numbers[i] ≤ 1000

[input] integer sum
An integer representing the sum of the pair we're looking for.

Guaranteed constraints:

-2000 ≤ sum ≤ 2000

[output] integer
An integer representing the difference between the indices of the closest pair of elements that add up to sum (or -1 if there isn't one).
'''
def findClosestPair(numbers,summ):
    closestPair=-1
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i]+numbers[j]==summ and i!=j:
                if closestPair==-1:
                    closestPair=[i,j]
                elif abs(closestPair[0]-closestPair[1])>abs(i-j):
                    closestPair=sorted([i,j])
    if closestPair==-1:
        return -1
    else:
        return [numbers[closestPair[0]],numbers[closestPair[1]]]

print(findClosestPair(numbers = [1, 0, 2, 4, 3, 0] ,summ = 5 ))
print(findClosestPair(numbers = [2, 3, 7] , summ = 8))