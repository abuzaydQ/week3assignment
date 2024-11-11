# 1 Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. 
# The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, 
# return the original price.

# 2 Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. 
# Print the final price after applying the discount, or if no discount was applied, print the original price.

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:

        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    
    else:
        return price
    

try:
    price =float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage "))


    final_price = calculate_discount(price, discount_percent)

    if final_price < price:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${price:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount percentage.")