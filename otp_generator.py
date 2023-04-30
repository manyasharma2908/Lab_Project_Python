import random
a=random.randint(100000,999999)
s=str(a)
str=int(s[-6::])
print(str)
b=int(input("Enter the OTP\n"))
if b==str:
    print("OTP Verified")
'''else:
    print("Invalid OTP")
'''