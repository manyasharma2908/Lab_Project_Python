import random
t=int(input("How many times you want to role the dice "))
lst=[]
while t>0:

    a=random.randint(1,6)
    print(a)
    lst.append(a)
    s1=str(" -------\n"+"|       |\n"+"|   0   |\n"+"|       |\n"+" -------")
    s2=str(" -------\n"+"| 0     |\n"+"|       |\n"+"|     0 |\n"+" -------")
    s3=str(" -------\n"+"| 0     |\n"+"|   0   |\n"+"|     0 |\n"+" -------")
    s4=str(" -------\n"+"| 0   0 |\n"+"|       |\n"+"| 0   0 |\n"+" -------")
    s5=str(" -------\n"+"| 0   0 |\n"+"|   0   |\n"+"| 0   0 |\n"+" -------")
    s6=str(" -------\n"+"| 0   0 |\n"+"| 0   0 |\n"+"| 0   0 |\n"+" -------")
    dct={1 : s1 , 2 : s2 , 3 : s3 , 4 : s4 , 5 : s5 , 6 : s6}
    print(dct[a])
    t-=1
print("Your outcomes are: ",lst)
