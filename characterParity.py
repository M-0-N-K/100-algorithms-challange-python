'''
Given a character, check if it represents an odd digit, 
an even digit or not a digit at all.

Example

For symbol = '5', the output should be characterParity(symbol) = "odd";
For symbol = '8', the output should be characterParity(symbol) = "even";
For symbol = 'q', the output should be characterParity(symbol) = "not a digit".
Hints

isNaN()
parseInt()
Input/Output

[execution time limit] 5 seconds (ts)
[input] char symbol
[output] string
'''
def characterParity(char):
    try:
        if int(char)%2==0:
            return 'even'
        else:
            return 'odd'
    except:
        return 'not a digit'
print(characterParity('5'))
print(characterParity('8'))
print(characterParity('q'))