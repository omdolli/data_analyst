product = input("Enter the product name :");
price = int(input("Enter the price of the product :"));
quantity = int(input("Enter the quantity"));

total = price * quantity;

print("product",product)
print("Total revenue generated",total)

if total > 1000:
    print("High value sale")
else:
    print("Normal sale")