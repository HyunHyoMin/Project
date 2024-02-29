import random

my_number = float(input('1~100 사이의 숫자를 입력해주세요 : '))
random_number = random.randint(1,100)
count = 1

while (1):
    if my_number % 1 != 0:
        my_number = float(input('잘못된 숫자입니다. 정수를 입력해주세요 : '))
    elif  my_number < 1 or my_number >100:
        my_number = float(input('잘못된 숫자입니다. 1 ~ 100 사이의 숫자를 입력해주세요 : '))
    elif my_number < random_number:
        print("Up")
        my_number = float(input('더 큰 숫자입니다. 다시 입력해주세요 : '))
        count += 1
    elif my_number > random_number:
        print("down")
        my_number = float(input('더 작은 숫자입니다. 다시 입력해주세요 : '))
        count += 1
    elif my_number == random_number:
        break
print("정답입니다!!", count, "번만에 맞히셨습니다.")
