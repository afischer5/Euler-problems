x = 2520
while x < 10000000000:
    for divisor in range (1, 20):
        
        if x % divisor != 0:
            x += 20
            break
        
        elif divisor > 18:
            print (divisor)
            
            print(x)
            x = 999999999999
        
