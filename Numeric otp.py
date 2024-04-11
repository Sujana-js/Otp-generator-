CODE 1: #Numeric otp generator
import random
import math
def otp():
    string='0123456789'
    otp=''
    for i in range(6):
        otp+=string[math.floor(random.random()*10)]
    return otp
print("your otp:",otp())


