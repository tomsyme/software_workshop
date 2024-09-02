"prime"

#!/usr/bin/env python3

NUM = 407

if NUM in (0, 1):
    print(NUM, "is not a prime number")

elif NUM > 1:
    # check for factors
    for i in range(2,NUM):
        if (NUM % i) == 0:
            print(NUM,"is not a prime number")
            print(i,"times",NUM//i,"is",NUM)
            break

else:
    print(NUM,"is a prime number")

# if input number is less than
# or equal to 1, it is not prime
