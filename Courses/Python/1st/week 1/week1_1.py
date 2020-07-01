import sys

digit_string = sys.argv[1]
summ = 0
for s in digit_string:
    summ += int(s)
print(summ)
