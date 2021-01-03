"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    while True:
        print("Cannot divide by zero!")
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
print("Finished.")
# 1. When will a ValueError occur?
# Ans. When numerator or deniminator are not integer.
# 2. When will a ZeroDivisionError occur?
# Ans.when denominator is zero.
# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Ans. if denominator  is not equal to zero
