import random

def cpu(): 
    cpu_number = random.randint(1, 3)
    if cpu_number == 1:
        cpu_number = "가위"
    elif cpu_number == 2:
        cpu_number = "바위"
    elif cpu_number == 3:
        cpu_number = "보"
    return cpu_number

while(1) :
    cpu_rps=cpu()
    user_rps = input("가위바위보 : ")
    
    if (user_rps == "가위" or user_rps ==  "바위" or user_rps == "보") == False:
        print("가위, 바위, 보 중에 입력하세요")
        continue
    if user_rps == cpu_rps:
        print("사용자 :",user_rps,"/ 컴퓨터 :",cpu_rps)
        print("무승부!")
        break
    elif (user_rps=="가위" and cpu_rps=="바위") or user_rps==("바위" and cpu_rps=="보") or (user_rps=="보" and cpu_rps=="가위"):
        print("사용자 :",user_rps,"/ 컴퓨터 :",cpu_rps)
        print('컴퓨터 승리!')
        break
    elif (user_rps=="가위" and cpu_rps=="보") or (user_rps=="바위" and cpu_rps=="가위") or (user_rps=="보" and cpu_rps=="바위"):
        print("사용자 :",user_rps,"/ 컴퓨터 :",cpu_rps)
        print('사용자 승리!')
        break
while(1):
    stop = input("다시하시겠습니까? (y/n): ").lower()
    while (stop == "y" or stop == "n") == False:
            stop = input("유효한 입력이 아닙니다. (y/n): ").lower()
    if stop == "y":
        continue
    elif stop == "n":
        print("게임 끝!")
        break