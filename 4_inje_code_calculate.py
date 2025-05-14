#생년과 2100 년도의 차이를 초로 출력하세요
#(2100- 생년) * 365일 * 24시간 * 60분 * 60초

year_string = input()
year = int(year_string)

result =  (2100 - year) * 365 * 24 * 60 *60
print(result)