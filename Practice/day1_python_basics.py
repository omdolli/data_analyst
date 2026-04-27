# Q1: Greeting Program
# Taking user input (name) and printing greeting
name = input("Enter your name: ")
print("Hello,", name)


# Q2: Simple Calculator
# Taking two numbers and performing basic operations
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)


# Q3: Square and Cube
# Calculating square and cube of a number
num = int(input("Enter a number: "))
print("Square:", num ** 2)
print("Cube:", num ** 3)


# Q4: Even or Odd
# Checking if number is even or odd using modulus operator
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Q5: Largest of Two Numbers
# Comparing two numbers to find the largest
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest is:", a)
else:
    print("Largest is:", b)


# Q6: Voting Eligibility
# Checking if user is eligible to vote (age >= 18)
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# Q7: Total Bill
# Calculating total bill using price and quantity
product = input("Enter product name: ")
price = int(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("Product:", product)
print("Total Bill:", total)


# Q8: String Length
# Finding length of input string
name = input("Enter your name: ")
print("Length of name:", len(name))


# Q9: Swap Two Numbers
# Swapping values using Python's multiple assignment
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

num1, num2 = num2, num1

print("After swapping:")
print("num1 =", num1)
print("num2 =", num2)


# Q10: Average of 3 Numbers
# Calculating average = sum / count
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average:", average)