import random
lst=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9' )
lst2=('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
lst3=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
lst4=('!','#','$','%','&','*','?','@')
st=''
for i in range(3):

    st+=random.choice(lst)
    st+=random.choice(lst2)
    st+=random.choice(lst3)
    st+=random.choice(lst4)
print(st)
b=input("Enter your Captcha\n")
if b==st:
    print("Captcha Verified!!!\n")
else:
    print("Invalid Captcha!!!\n")
