print("도라에몽게임")
print("이슬이와 노진구가 길가다 퉁퉁이를 만났다. 어떡하지? ")
print("1.싸운다 2.도망간다 ")
a = input("선택 :")


if a == "1":
    print("한눈판사이 이슬이는 이미 도망!!도움이필요해....도라에몽!")
    print("도착한 도라에몽..주머니를 뒤적인다")
    import random
    dogu = ['공기포다! 진구야 받아!', '칼이다! 진구야 받아!', '방패망토다!진구야 받아!']
    s = random.choice(dogu)
    print(s)
    
    

    
if a == "2":
    print("--달리기 속도 느려서 사망--")


    print("Game Over")
    print("★...출연...★")
    scores = {"철수": '도라에몽', "퉁퉁이": '노진구' }
 

    keys = scores.keys()
    for k in keys:
        print(k)
    
    
    values = scores.values()
    for v in values:
        print(v)


