# T20 Practical Task 3

# Input the user data
a = input("Please enter number 1:")
b = input("Please enter number 2:")

# Calculate the sum of two numbers
def sum_fn(num1, num2):
    if(a.isnumeric() and b.isnumeric()):
        return str(int(a) + int(b))
    else:
        return "\033[31mInput data error\033[00m"

# Print the result
result = sum_fn(a, b)
if result.isnumeric():
    print(f"The sum of two numbers is {result}")
else:
    print(result)

