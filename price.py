# 'price' has already been created

# Write your code here

if price >=300:
    price = price - (price * (30/100))
elif price>=200 or price<300:
    price = price - (price * (20/100))
elif price>=100 or price<200:
    price = price - (price * (10/100))
elif price>=0 or price<100:
    price = price - (price * (5/100))
else:
    pass

