products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]
stock = [12, 50, 30, 8, 15]
prices = [120000, 2500, 4500, 45000, 35000]

# stock[0] * prices[0]
# Inventory Value = Stock × Price

for x in range(len(products)):
    inventory_value = stock[x] * prices[x]
    print(products[x], inventory_value)


print("=============== part 2 =======================")

for x in range(len(stock)):  # 0,1,2,3,4
    if stock[x] < 10:
        print(products[x])


range(50,100) # 0,1,2,3,4
len(stock)

cond = True
while cond:
    v = input()