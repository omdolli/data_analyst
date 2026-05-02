def calculate_total(price, quantity):
    return price * quantity


def check_sale(total):
    if total > 1000:
        return "High Value Sale"
    else:
        return "Low Value Sale"


totals = []
products = []

while True:
    product = input("Enter product name: ").strip().lower()
    
    price_input = input("Enter the price: ")
    price = int(price_input.replace("₹", "").replace("$", "").strip())
    
    quantity = int(input("Enter the quantity: "))

    total = calculate_total(price, quantity)
    
    totals.append(total)
    products.append(product)

    print("Product:", product)
    print("Total:", total)
    print(check_sale(total))

    choice = input("Add another product? (yes/no): ").strip().lower()
    if choice == "no":
        break


if totals:
    print("\n--- Sales Summary ---")
    print("Products:", products)
    print("All sales:", totals)
    print("Total Revenue:", sum(totals))
    print("Highest Sale:", max(totals))
    print("Lowest Sale:", min(totals))
else:
    print("No sales data available")