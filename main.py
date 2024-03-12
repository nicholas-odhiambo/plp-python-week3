# prompt the user to enter the original price of an item and the discount percentage.
  

price = float(input('Enter the original price: '))
discount_percent = float(input('Enter the discount: '))


# function  that calculates the final price after applying a discount.

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price    

#calculate thefinal price
final_price = calculate_discount(price, discount_percent)


#Print the final price after applying the discount, or if no discount was applied, print the original price

if final_price != price:
    print('Final price: ', final_price)
else:
    print('Original price:', price)

