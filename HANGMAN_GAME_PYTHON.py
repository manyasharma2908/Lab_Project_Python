from random import choice

def print_man(i,correct,letter):
    global lst
    global right_word
    lst.append(letter)
    h = chr(0x203E)*3
    man = {0: f" +---+\n O   |\n     |\n     |\n    ___\n    {h}",
        1: f" +---+\n O   |\n |   |\n     |\n    ___\n    {h}",
        2: f" +---+\n O   |\n/|   |\n     |\n    ___\n    {h}",
        3: f" +---+\n O   |\n/|\  |\n     |\n    ___\n    {h}",
        4: f" +---+\n O   |\n/|\  |\n/    |\n    ___\n    {h}",
        5: f" +---+\n O   |\n/|\  |\n/ \  |\n    ___\n    {h}"
    }
    print(man[i])
    print("Missed letters:",*lst)
    a=""
    if i==5:
        print(f"You are ran out of guesses\nAfter 6 missed guesses and {correct} correct guesses, right word is {right_word}")
        a = input("Would you like to play again (y)es or (n)o:\n")
        if a == "y":
            return 0,0
        else:
            return 6,correct
    else:
        return i+1,correct

def choose_word():
    word_s = ["fox","mouse","watch","chain","earth","ear"]
    word_dsp = {"fox":["f","_","x"],"mouse":["m","_","u","_","e"],"watch":["w","_","t","_","h"],
                "chain":["c","_","a","_","n"],"earth":["e","_","r","_","h"],"ear":["e","_","r"]}
    word = "".join(choice(word_s))
    return word,word_dsp[word]

def right_guess(b):
    global right_word
    global dsp_guess
    ct=0
    for i in range (len(right_word)):
        if b==right_word[i]:
            ct=i
            dsp_guess[ct]=right_word[ct]

lst=[]
w_try = 0
r_try = 0
right_word,dsp_guess = choose_word()
while w_try<6:
    
    print(*dsp_guess)
    user = input("Guess the letter: ")
    print()
    if user in right_word:
        r_try+=1
        right_guess(user)
    else:
        w_try,r_try = print_man(w_try,r_try,user)
        right_word,dsp_guess=choose_word()
        lst.clear()
    if dsp_guess == list(right_word):
        print(f"You guessed the word {right_word} correctly After {w_try} missed guesses and {r_try} correct guesses")
        if input("Would you like to play again (y)es or (n)o:\n").lower() == "y":
            w_try,r_try=0,0
            right_word,dsp_guess = choose_word()
        else: 
            break