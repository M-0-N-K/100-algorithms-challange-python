'''
Check Out More Algorithms like this at FreeCodeCamp
Return the factorial of the provided integer.

If the integer is represented with the letter n, a factorial is the product of all positive integers less than or equal to n.

Factorials are often represented with the shorthand notation n!

For example: 5! = 1 * 2 * 3 * 4 * 5 = 120

Only integers greater than or equal to zero will be supplied to the function.

Remember to use Read-Search-Ask if you get stuck. Write your own code.

Example

factorializeANumber(5) returns 120;
factorializeANumber(10) returns 3628800;
'''
def factorializeANumber(num):
    if num<=1:
        return 1
    return num*factorializeANumber(num-1)

print(factorializeANumber(5))
print(factorializeANumber(10))
