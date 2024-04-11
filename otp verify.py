CODE 4:
INTRO: This code is to create an interface , which gives success when correct otp is entered and fails to login when a wrong otp is entered

import random
gen=random.randint(000000,1000000)
username=input('enter username:')
print('hi',username)
print('here is your otp:',gen)
password=input("enter otp to login:")
if password==str(gen):
    print("login success")
else:
    print("login failed")


