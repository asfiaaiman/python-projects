def apply_discount(price, discount):
    # Check if the price is a number
    if not isinstance(price, (int, float)):
        return "The price should be a number."

    # Check if the discount is a number
    if not isinstance(discount, (int, float)):
        return "The discount should be a number."

    # Price must be greater than 0
    if price <= 0:
        return "The price should be greater than 0."

    # Discount must be between 0% and 100%
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100."

    # Calculate the discount amount
    discount_amount = price * discount / 100

    # Subtract the discount from the original price
    return price - discount_amount