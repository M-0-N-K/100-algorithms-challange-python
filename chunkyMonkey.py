'''
Write a function that splits an array (first argument) 
into groups the length of size (second argument) and 
returns them as a two-dimensional array.

Example

chunkyMonkey(["a", "b", "c", "d"], 2) should return [["a", "b"], ["c", "d"]].
chunkyMonkey([0, 1, 2, 3, 4, 5], 4) should return [[0, 1, 2, 3], [4, 5]].
Hints

slice()
'''
def chunkyMonkey(arr,size):
    res=[]
    for index in range(0,len(arr),size):
        res.append(arr[index:index+size])
    return res

print(chunkyMonkey([0, 1, 2, 3, 4, 5], 4))
print(chunkyMonkey(["a", "b", "c", "d"], 2))