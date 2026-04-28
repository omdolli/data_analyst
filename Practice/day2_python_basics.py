# Q1. Print numbers 1 to 10
i = 1
while i < 11:
    print(i)
    i+=1

# Q2. Print even numbers from 1 to 20
j = 1
while j < 21:
    if j % 2 == 0:
        print(j)
    j+=1

# Q3. Print sum of numbers from 1 to N
n = int(input("Enter a number :"))

total = 0

for i in range(1, n + 1):
    total += i
print("Sum:",total)

# Q4. Multiplication Table
num = int(input("Enter a number:"))

for i in range (1,11):
    print(num,"x",i,"=",num*i)

# Q5. Count Digits
numm = int(input("Enter a number"))

count = 0

while numm > 0:
    numm = numm // 10
    count += 1

print("Digits:", count)

# Q6. Reverse Number
int = int(input("Enter a number:"))
reverse = 0

while int > 0:
    digits = int % 10
    reverse = reverse * 10 + digits
    int = int // 10
print("Reverse : " , reverse)

# Q7. Prime Number
num = int(input("Enter a number :"))
is_prime = True
for i in range(2,num):
    if num%i == 0:
        is_prime = False
        break

if is_prime and num >1:
    print("Prime")
else:
    print("Not prime")

# Q8. Factorial
num = int(input("Enter a number :"))
fact = 1

for i in range(1 , num +1):
    fact = fact * i
print("Factorial", fact)