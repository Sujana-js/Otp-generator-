CODE3: #AlphaNumeric otp generator

import math
import random
def gen():
    string='0123456789abcdefghijklmnopqrstuvwxyz'
    varlen=len(string)
    otp=''
    for i in range(6):
        otp+=string[math.floor(random.random()*varlen)]
    return otp
print("your generated otp is",gen())
