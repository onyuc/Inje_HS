# 사용자로부터 총 5개의 문자열을 입력받으세요.
# 입력받은 문자열은 모두 리스트에 넣으세요.
# 이후 입력받은 문자열들을 입력받은 역순으로 출력하세요.

words = []  # 빈 리스트 생성

# 입력받은 문자열 리스트에 추가
for i in range(5):
    word = input()
    words.append(word)

# for 문과 list

reversed_words = reversed(words) # 역 list

for word in reversed_words:
    print(words)