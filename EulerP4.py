x = 100
y = 100
largest = 1

while x != 1000:
    y = 100
    while y != 1000:

        s =  str( x * y)
        if s[::-1] == s:
            if (x * y) > largest:
                largest = (x * y)

        y += 1
    x += 1


print(largest)
