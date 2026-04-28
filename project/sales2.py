total_revenue = 0

while True:
    product = input("Enter product name :")
    price = int(input("Enter price :"))
    quantity = int(input("Enter quantity"))

    total = price * quantity
    total_revenue += total

    print("Product",product)
    print("Total",total)

    if total > 1000:
        print("High value sale")
    else:
        print("Low sales")

    choice = input("Add another product ? (yes/no):")

    if choice.lower() == "no":
        break
print("Final Total revenue:" , total_revenue)