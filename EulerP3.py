#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

x = 2
largest = 2

while x * x < 600851475143:
    if 600851475143 % x == 0:
        #determine if x is prime
        n = 2
        while n < x:
            if x % n == 0:
                
                break
                
            if n == (x - 1):
                largest = x
            n += 1
                
    x+=1
    
print(largest)
                
