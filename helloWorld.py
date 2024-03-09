# T20 Practical Task 3

a = input("Please enter number 1:")
b = input("Please enter number 2:")

def sum_fn(num1, num2):
    if(a.isnumeric() and b.isnumeric()):
        return str(int(a) + int(b))
    else:
        return "\033[31mInput data error\033[00m"

result = sum_fn(a, b)
if result.isnumeric():
    print(f"The sum of two numbers is {result}")
else:
    print(result)

