# 사용자에게 숫자를 입력받으면, 해당하는 구구단을 출력하세요

num = int(input("숫자를 입력하세요: "))

i = 1
while i <= 9:
    print(f"{i}*{num}={num*i}")
    i += 1