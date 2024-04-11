CODE2: #Alpha otp generator
import random
import math
def otp():
    string='abcdefghijklmnopqrstuvwxyz'
    varlen=len(string)
    otp=''
    for i in range(6):
        otp+=string[math.floor(random.random()*varlen)]
    return otp
print("your otp:",otp())

