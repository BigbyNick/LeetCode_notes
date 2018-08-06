prices = [7, 6, 4, 3, 1]
minprice = prices[0]
maxprofit = 0

for i in range(len(prices)):
    if minprice > prices[i]:
        minprice = prices[i]
    if maxprofit < prices[i] - minprice:
        maxprofit = prices[i] - minprice

print(maxprofit)
        
