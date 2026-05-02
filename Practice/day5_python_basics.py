# Q1
name = input("Enter name: ")
print(name.strip())

# Q2
text = input("Enter text: ")
print(text.lower())

# Q3
rupee = input("Enter price: ")
clean_price = int(rupee.replace("₹", "").replace("$", "").strip())
print(clean_price)

# Q4
sent = input("Enter sentence: ")
words = sent.split()
print(len(words))

# Q5
fruits = input("Enter fruits: ")
print(fruits.split(","))

# Q6 (IMPORTANT FIX)
fr = input("Enter messy fruits: ")

items = fr.strip().lower().split(",")

clean_list = []
for item in items:
    clean_list.append(item.strip())

print(clean_list)