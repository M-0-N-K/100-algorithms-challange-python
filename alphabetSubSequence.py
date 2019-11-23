'''
Check whether the given string is a subsequence of the plaintext alphabet.

Example

For s = "effg" or s = "cdce", the output should be alphabetSubsequence(s) = false

For s = "ace" or s = "bxz", the output should be alphabetSubsequence(s) = true.

Hints

size property
charCodeAt()
Input/Output

[execution time limit] 5 seconds (ts)
[input] string s
Guaranteed constraints:

2 ≤ s.length ≤ 15.

[output] boolean

true if the given string is a subsequence of the alphabet, false otherwise.
'''
def alphabetSubsequence(sequence):
    alphabetSequence= 'abcdefghijklmnopqrstuvwxyz'
    index=0
    for i in range(len(sequence)):
        if(sequence[i] in alphabetSequence[index:]):
            index=alphabetSequence.find(sequence[i])+1
        else:
            return False
    return True

    
print(alphabetSubsequence("bxz"))
print(alphabetSubsequence("effg"))