#otp generator
import random  #bcz we want any number random

numbers=list(range(0,10))
OTP=""
for i in range(0,4):
    OTP+=str(random.choice(numbers))
print(OTP)    