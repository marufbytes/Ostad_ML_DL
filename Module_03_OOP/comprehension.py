dollar_prices=[10,25,30,45,50]
taka_prices = []

for price in dollar_prices:
    taka = price*120
    taka_prices.append(taka)

print(taka_prices)


#list comprehension
taka_prices=[price*120 for price in dollar_prices]
print(taka_prices)