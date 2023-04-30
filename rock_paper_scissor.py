import random
while True:
    t=("Rock",'Paper','Scissor')
    a=random.choice(t)
    print(a)
    
    dct={"Rock":1,"Paper":2,"Scissor":3}
    
    b=(input("Enter your decision!!!"))
    c=b.title()
    user=dct[c]
    comp=dct[a]
    

    if (c=="Rock" and a=="Scissor"):
       print("You win!!! "+"\U0001F44F"*3)
    elif c=="Scissor" and a=="Rock":
        print("You loose!!! "+"\U0001F92A"*3)
    elif user==comp:
        print("It's a tie!!!")
    elif user>comp:
        print("You win!!! "+"\U0001F44F"*3)
    else:
        print("You Loose!!"+"\U0001F92A"*3)
    d=int(input("Do You Want To Play Again ??\n""Press  2 to continue... and 1 for exit\n"))
    if d==1:
        break



