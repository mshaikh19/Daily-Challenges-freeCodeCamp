# Free Shipping
# Given an array of strings representing items in your shopping cart, and a number for the minimum order amount to qualify for free shipping, determine if the items in your shopping cart qualify for free shipping.

# The given array will contain items from the list below:

# Item	    Price
# "shirt"	34.25
# "jeans"	48.50
# "shoes"	75.00
# "hat"	    19.95
# "socks"	15.00
# "jacket"	109.95


def gets_free_shipping(cart, minimum):
    price = 0.0
    for i in cart:
        match i:
            case "shirt":
                price += 34.25
            
            case "jeans":
                price += 48.50
            
            case "shoes":
                price += 75.00
            
            case "hat":
                price += 19.95

            case "socks":
                price += 15.00

            case "jacket":
                price += 109.95
        
    if price < minimum:
        return False
    return True

print(gets_free_shipping(["shoes"], 50))
print(gets_free_shipping(["hat", "socks"], 50))
print(gets_free_shipping(["jeans", "shirt", "jacket"], 75))
print(gets_free_shipping(["socks", "socks", "hat"], 75)) 
print(gets_free_shipping(["shirt", "shirt", "jeans", "socks"], 100))
print(gets_free_shipping(["hat", "socks", "hat", "jeans", "shoes", "hat"], 200))
