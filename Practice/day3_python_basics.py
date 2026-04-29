# # Q1. add two numbers
# def function(x,y):
#     return x + y
# print(function(5,8))

# # Q2. even/odd
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# print(is_even(4))  # True
# print(is_even(5))  # False

# # Q3. square
# def square(x):
#     return x ** 2
# print(square(5))

# # Q3 . largest of three
# def largest(a,b,c):
#     if a>b and a>c:
#         return(a)
#     elif b>a and b>c:
#         return(b)
#     else:
#         return(c)
# print(largest(4,8,19))

# # Q4. factorial
# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact * i
#     return fact
# print(factorial(5))

# Q5. prime

# def is_prime(n):
#     if n <=1:
#         return False
    
#     for i in range(2,n):
#         if n % i ==0:
#             return False
        
#     return True
# print(is_prime(5))

# Q6. Reverse a number
def reverse_num(n):
    rev = 0
    while n > 0:
        digit = n%10
        rev = rev *10 +digit 
        n = n//10
    return rev 
print(reverse_num(123456))


