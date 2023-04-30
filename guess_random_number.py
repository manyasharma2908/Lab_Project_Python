import random
a=random.randint(0,100)
print(a)

count=0
score=100
while True:
    count+=1
    b=int(input("Enter the number you guess!!!! "))

    if a==b:
        print("Huraah! You gussed the right nuber.")
        print("Your score is :",score-count)
        break

