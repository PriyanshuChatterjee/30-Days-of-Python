import math
lst = [1,2,3,4,5,6,7,8,9,10]

res = [(val, pow(val,0), pow(val,1), pow(val,2), pow(val,3), pow(val,4), pow(val,5),) for val in lst]

print(res)