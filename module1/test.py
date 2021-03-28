print('Hello world')

def price_item(name, price_in_pennies):
    return price_in_pennies/100

result = price_item('Milk', 80)
print(result)

sq_odd = [x*x for x in range(20) if x%2!=0]
print(sq_odd)