def calculate_total(price, quantity):
    return price * quantity


def check_sale(total):
    if total > 1000:
        return "High Value Sale"
    else:
        return "Low Value Sale"


totals = []

while True:
    product = input("Enter product name: ")
    price = int(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))

    total = calculate_total(price, quantity)
    totals.append(total)

    print("Product:", product)
    print("Total:", total)
    print(check_sale(total))

    choice = input("Add another product? (yes/no): ")
    if choice.lower() == "no":
        break


if totals:
    print("All sales:", totals)
    print("Total Revenue:", sum(totals))
    print("Highest Sale:", max(totals))
    print("Lowest Sale:", min(totals))
else:
    print("No sales data available")