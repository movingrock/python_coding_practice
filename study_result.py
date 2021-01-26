# 출력
print("ABC")
print("ABC"[0:2])
print(len("ABC"))
print(type("123"))

# format
print("{}{}{}".format("A","B","C"))
print("{0}{1}{2}".format("A","B","C"))
print("{name} / {day} / {height}".format(day=10, name = "lds", height = 178))

print("{:5d}".format(123))          
print("{:05d}".format(123))
print("{:+5d}".format(123))
print("{:=+5d}".format(123))
print("{:+05d}".format(123))

print("{:f}".format(12.345))
print("{:15f}".format(12.345))
print("{:+15f}".format(12.345))
print("{:+015f}".format(12.345))
print("{:05.3f}".format(12.345))
print("{:.1f}".format(12.345))

print("{:g}".format(5.0))


#함수
print("abcdef".upper())
print("ABCDEF".lower())

print("  ABC  ".strip())
print("  ABC  ".lstrip())
print("  ABC  ".rstrip())

print("ABCDE".isupper())   # is함수 === 문자열이 무엇으로'만' 구성되었는지 확인 // True, False로 출력 /// isalnum() / isalpha() / isidentifier() / isdecimal() / isdigit() / isspace() / islower() / isupper()

print("ABCABCABCABC".find("CA"))
print("ABCABCABCABC".rfind("CA"))
print("AB" in "ABCABC")


print("10,20,30,40,50".split(','))  #split() 안의 문자를 기준으로 나눠, 리스트에 넣음


#시간 활용
import datetime   # 모듈이라고 함
now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)


# if 문
if True:
    pass # 나중에 구현하기 위해 잠시 둠. 에러를 띄우지 않는다.
elif True:
    pass
else:
    raise NotImplementedError  # 나중에 구현하기 위해 잠시 둠. 에러를 띄움



# 입력
# a = input()
# b = input("입력:")
# c = int(input())
# d,e,f = input().split()
# g,h,i = map(int, input().split())
# j = list(input()) #리스트 입력 받기, 입력할때 공백을 입력하면 공백도 요소로 들어감. 공백없이 연속해서 넣어야됨.











# ord( ) 유니코드변환

# while(조건식): 조건식이 참인동안 반복한다. 거짓인 상황이 나와야 반복이 멈춤

# 출력 형태 2가지
# 1. format : print('{}{}{}'.format(ㅁ,ㅅ,ㅇ))
# 2. % : print('%d' %ㅁㅁㅁ)
#     print('%04d' %)

# 16진수 8진수등으로 입력 받는 법 / 출력하는 법
# a = int(input(), 16)
# print('%o' %a)

# a = int(input(), 16);
# for i in range(1,16):
#     print("{:X}*{:X}={:X}".format(a,i,a*i))