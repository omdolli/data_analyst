
def calculate_total(price,quantity):
    return price * quantity

def check_sale(total):
    if total > 1000:
        return "High value sale"
    else:
        return "Low sales"


total_revenue = 0

while True:
    product = input("Enter the product name : ")
    quantity = int(input("Enter the quantity :"))
    price = int(input("Enter the price :"))

    total = calculate_total(price,quantity)
    total_revenue += total

    print("Product:", product)
    print("Total:", total)
    print(check_sale(total))
        
    choice = input("Add another product ? (yes/no):")

    if choice.lower() == "no":
        break
print("Final Total revenue:" , total_revenue)