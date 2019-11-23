'''
Given an array of 2k integers (for some integer k), perform the following operations until the array contains only one element:

On the 1st, 3rd, 5th, etc. iterations (1-based) replace each pair of consecutive elements with their sum;
On the 2nd, 4th, 6th, etc. iterations replace each pair of consecutive elements with their product. After the algorithm has finished, there will be a single element left in the array. Return that element.
Example

For inputArray = [1, 2, 3, 4, 5, 6, 7, 8], the output should be arrayConversion(inputArray) = 186.

We have [1, 2, 3, 4, 5, 6, 7, 8] -> [3, 7, 11, 15] -> [21, 165] -> [186], so the answer is 186.

Hints

push()
Input/Output

[execution time limit] 5 seconds (ts)
[input] array.integer inputArray
Guaranteed constraints:

1 ≤ inputArray.length ≤ 20,

-9 ≤ inputArray[i] ≤ 99.

[output] integer


'''

def arrayConversion(arr,iteration=0):
    #since there is not given what will be done with odd sized array, I am skipping it.
    if len(arr)==1:
        return arr[0]
    elif iteration==0:
        res=[]
        for i in range(0,len(arr)-1,2):
            res.append(arr[i]+arr[i+1])
        return arrayConversion(res,iteration=1)
    else:
        res=[]
        for i in range(0,len(arr)-1,2):
            res.append(arr[i]*arr[i+1])
        return arrayConversion(res,iteration=0)
        
print(arrayConversion([1, 2, 3, 4, 5, 6, 7, 8]))