# In bowling, the player starts with 10 pins in a row at the far end of a lane. 
# The goal is to knock all the pins down. For this assignment, the number of pins and balls will vary. 
# Given the number of pins N and then the number of balls K to be rolled, followed by K pairs of numbers (one for each ball rolled), 
# determine which pins remain standing after all the balls have been rolled.

# The balls are numbered from 1 to N for this situation. 
# The subsequent number pairs, one for each K represent the first and last (inclusive) positions of the pins that were knocked down with each roll. 
# Print a sequence of N characters, where "I" represents a pin left standing and "." represents a pin knocked down.
pins,balls = [int(x) for x in input().split()]
pinStart,pinEnd,res = [],[],[]
for i in range(pins):
    res.append('I')
for i in range(balls):
    x,y = [int(s) for s in input().split()]
    pinStart.append(x)
    pinEnd.append(y)
for i in range(balls):
    for j in range(pinStart[i]-1,pinEnd[i]):
        res[j] = '.'
print(''.join(res))

