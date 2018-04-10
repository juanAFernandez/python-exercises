import random
import sys

n_digits = int(sys.argv[1])

str_integer = ''

for _ in range(n_digits):
    str_integer += str(random.randint(1,9))

final_integer = int(str_integer)

print(final_integer)