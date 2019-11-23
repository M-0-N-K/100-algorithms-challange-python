'''
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Example

For sequence = [1, 3, 2, 1], the output should be almostIncreasingSequence(sequence) = false;
There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be almostIncreasingSequence(sequence) = true.
You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

Hints

Nope
Input/Output

[time limit] 4000ms (js)
[input] array.integer sequence
Guaranteed constraints:

2 ≤ sequence.length ≤ 105,

-105 ≤ sequence[i] ≤ 105.

[output] boolean

Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.
'''
def almostIncreasingSequence(arr):
    notIncreasing=0
    i=0
    while notIncreasing<2 and i<len(arr)-1:
        if arr[i]>arr[i+1]:
            notIncreasing+=1
        i+=1
    if notIncreasing<2:
        return True
    else:
        return False
print(almostIncreasingSequence([1, 3, 2, 1]))
print(almostIncreasingSequence([1, 3, 2]))