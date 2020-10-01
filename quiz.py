import random
import time

d1={"what is the capital of India":"delhi", "what is the capital of china":"begieng", "what is the capital of england":"london",
    "what is the capital of usa":"washington dc", "what is the capital of australia":"canberra", "what is the capital of mexico":"mexico city"
    , "what is the capital of singapore":"singapore city", "what is the capital of france":"paris", "what is the capital of spain":"madrid"
    ,"what is the capital of denmark":"copenhagen", "what is the capital of japan":"tokyo", "what is the capital of peru":"peru",
    "what is the capital of brazil":"rio de janerio"}

d2={"2+2":"4", "2*3":"6", "45+55":"100", "5!":"120", "6!":"720", "100+299":"399", "0!":"1", "6*6":"36", "5*5*5":"125", "9*9":"81"
    , "100+100-200":"0"}

d3={"who is the ceo of apple":"tim cook", "who is the ceo of tesla":"elon musk", "who is the indian ceo of realme":"madahv seth",
    "who is the indian ceo of xiaomi":"manu jain", "who is the ceo of ola":"bhavesh aggarwal", "who is the ceo of reliance":"mukesh ambani"
    ,"who is the founder of facebook":"mark zuckerberg", "woh is the ceo of prime minister of India":"narendra modi",
    "who is the president of usa":"donald trump", "who is the president of russia":"vladimir putin", "who is the prime minister of japan":"shinzo abe",
    "who is the queen of england":"queen elizabeth"}

d4={"who is the captain of team India":"virat kohli", "who was the captain of India":"ms dhoni", "who is the captain of juventus":"ronaldo"
    , "who is the captain of barcelona":"lionel messi", "who is the best player of golf":"tiger woods", "who is the best player of tennis":"roger fedrer"
    ,"who is the one of the best player of cricket in australia":"david warner"}

print("Trivial Game")
ty=input("enter your name-")
print("=================================================")
print(f"welcome {ty}")
print("=================================================")
time.sleep(2)
print("lets play game")
print("=================================================")
v=0
while v<=6:
    tu=("1.capital challenge", "2.basic math challenge", "3.personality challenge", "4.sports", "5.read rules", "6.exit")
    for cv in tu:
        print(cv)
    print("=================================================")
    v=int(input("enter your choice- "))
    print("=================================================")
    if v==1:
        print("lets play game")
        time.sleep(2)
        t=6
        p=0
        o=0
        while t>0:
            m = random.choice(list(d1.keys()))
            time.sleep(2)
            print(m)
            a=input("enter a your answer- ")
            print("========================================")
            time.sleep(2)
            if a==d1.get(m):
                print("answer is correct")
                print("========================================")
                o+=1
            else:
                print("answer is incorrect")
                print("========================================")
                print("correct answer is ", d1.get(m))
                print("========================================")
                p+=1
            if p==3:
                break
            t-=1
        print(f"you scored {o}/6")
        input()
    elif v==2:
        print("lets play game")
        time.sleep(2)
        t = 6
        p = 0
        o = 0
        while t > 0:
            n = random.choice(list(d2.keys()))
            time.sleep(2)
            print(n)
            a = input("enter a your answer- ")
            print("========================================")
            time.sleep(2)
            if a == d2.get(n):
                print("answer is correct")
                print("========================================")
                o += 1
            else:
                print("answer is incorrect")
                print("========================================")
                print("correct answer is ", d2.get(n))
                print("========================================")
                p += 1
            if p == 3:
                break
            t -= 1
        print(f"you scored {o}/6")
        input()
    elif v==3:
        print("lets play game")
        time.sleep(2)
        t = 6
        p = 0
        o = 0
        while t > 0:
            n = random.choice(list(d3.keys()))
            time.sleep(2)
            print(n)
            a = input("enter a your answer- ")
            print("========================================")
            time.sleep(2)
            if a == d3.get(n):
                print("answer is correct")
                print("========================================")
                o += 1
            else:
                print("answer is incorrect")
                print("========================================")
                print("correct answer is ", d3.get(n))
                print("========================================")
                p += 1
            if p == 3:
                break
            t -= 1
        print(f"you scored {o}/6")
        input()
    elif v==5:
        time.sleep(2)
        print("this is a trivial contest application")
        print("you have 6 chances to play")
        print("if you answer is wrong 3 times\n game will get over")
        print("created by Anirudh bishnoi")
        input()
    elif v==4:
        print("lets play game")
        time.sleep(2)
        t = 6
        p = 0
        o = 0
        while t > 0:
            n = random.choice(list(d4.keys()))
            time.sleep(2)
            print(n)
            a = input("enter a your answer- ")
            print("========================================")
            time.sleep(2)
            if a == d4.get(n):
                print("answer is correct")
                print("========================================")
                o += 1
            else:
                print("answer is incorrect")
                print("========================================")
                print("correct answer is ", d4.get(n))
                print("========================================")
                p += 1
            if p == 3:
                break
            t -= 1
        print(f"you scored {o}/6")
        input()
    elif v==6:
        break
print("developed by Anirudh Bishnoi")
print("thanks for playing")
