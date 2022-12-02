# Given a temperature in celsius C. You need to convert the given temperature to Fahrenheit.

# Example 1:

# Input:
# C = 32
# Output: 89
# Explanation: Using the conversion
# formula of celsius to farhenheit , it
# can be calculated that, for 32 degree
# C, the temperature in Fahrenheit = 89.

def cToF(self, C):
    # Your code here
    return ((C*(9/5))+32)


if __name__ == '__main__':
    print(cToF(-32))
