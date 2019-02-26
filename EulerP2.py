x = 1
y = 2
sigma = 0
while y <4000000:
    if y % 2 == 0:
        sigma = sigma + y
    
    h = x
    x = y
    y = h + x

    
print(sigma)
