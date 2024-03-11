def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price

# Prompting the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percentage)

# Printing the final price after applying the discount, or the original price if no discount was applied
if final_price != original_price:
    print("Final price after applying the discount: Ksh {:.2f}".format(final_price))
else:
    print("No discount applied. Original price: Ksh {:.2f}".format(final_price))

