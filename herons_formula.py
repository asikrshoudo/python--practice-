import math

a, b, c = map(float, input("Enter a, b, c: ").split())

if (a+b) > c and (b+c) > a and (c+a) > b:
    S = (a + b + c) / 2
    area = math.sqrt(S * (S-a) * (S-b) * (S-c))
    print("Area =", area)
else:
    print("Triangle is not possible")
