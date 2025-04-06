def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount)

if discount >= 20:
    print(f"Final price after {discount}% discount: ${final_price:.2f}")
else:
    print(f"No discount applied. Original price: ${original_price:.2f}")