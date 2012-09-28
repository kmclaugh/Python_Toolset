# Binomial

p = float(input("probability?"))
n = int(input("total trails?"))
k = int(input("successes?"))

import math


c=math.factorial(n)/(math.factorial(k)*(math.factorial(n-k)))

out=c*((p**k)*(1-p)**(n-k))

print(out)
