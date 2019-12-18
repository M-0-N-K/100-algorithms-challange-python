'''
Flatten a nested array. You must account for varying levels of nesting.

Example

steamrollArray([[["a"]], [["b"]]]) should return ["a", "b"].

steamrollArray([1, [2], [3, [[4]]]]) should return [1, 2, 3, 4]

Hints

isArray()
push(
    '''
def steamrollArray(arr):
    a=[]
    for i in arr:
        if type(i)!=int and type(i)!=str and type(i)!=float:
            a=a+steamrollArray(i)
        else:
            a=a+[i]
    return a
print(steamrollArray([[["a"]], [["b"]]]))
print(steamrollArray([1, [2], [3, [[4]]]]))