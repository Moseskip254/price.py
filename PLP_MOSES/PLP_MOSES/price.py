def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage to be applied.
    
    Returns:
    - float: The final price after applying the discount if it is 20% or higher;
             otherwise, returns the original price.
    """
    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
        return final_price
    else:
        return price

# Prompt the user for the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percent)

# Print the final price or the original price if no discount was applied
if discount_percent >= 20:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${original_price:.2f}")
