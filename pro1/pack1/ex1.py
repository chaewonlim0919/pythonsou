var1 = "안녕 파이썬"
print(var1)
"""
여러 줄
주석 
"""
# 한줄 주석
# 파이썬은 " , ' 동일

#var1 = 5; var2=6 #; 들어가야 두개의 명령 but 좋지 않음
var1=5
var1=10
var1=5.6
print(var1)

var2=var1
print(var1,var2)

var3=7
print(var1, var2, var3)
print(id(var1), id(var2), id(var3))

Var3=8
print(var3, Var3) # 대소문자 구분 , 숫자/특수문자로 시작하면 안됨, _는 ㄱㅊ

a=5
b=a
c=5
print(a,b,c)
print(a is b, a == b) #is: 주소 비교 연산, ==: 값 비교 연산
print(b is c, b == c) # 새로 만드는 게 아니라, 이미 있는 5를 재사용

aa=[5]
bb=[5]
print(aa,bb)
print(bb is aa, bb == aa) #집합형 변수일 경우, 값은 같으나 주소는 다름/ 값을 비교할 때 '=='으로 비교할 것 

print('----------------') 
import keyword # 키워드 목록 확인용 모듈 읽기
print("예약어 목록", keyword.kwlist) #키워드는 변수명, 클래스명, 모듈명으로 쓸 수 없음, 이미 기능을 가지고 있음


print('type(자료형) 확인')
kbs=9
print(isinstance(kbs,int))
print(isinstance(kbs,float))
print(5, type(5)) #5 <class, 'int'>
print(5.3,type(5.3))
print(3+4j, type(3+4j))
print(True, type(True))
print('good', type('good'))
print((1,), type((1,)))
print([1], type([1]))
print({1}, type({1}))
print({'k':1}, type({'k':1}))

