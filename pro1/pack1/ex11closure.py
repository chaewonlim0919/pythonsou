#Closure : Scope에 제약을 받지 않는 변수들을 포함하고 있는 코드블럭이다.
#내부 함수의 주소를 반환해 함수 밖에서 함수 내의 멤버를 참조하기

def funcTimes(a,b):
    c = a*b
    return c
print(funcTimes(2,3))
#print(c) #Error

kbs=funcTimes(2,3)
print(kbs) #6

kbs=funcTimes
print(kbs) #<function funcTimes at 0x00000151E645F920> 
print(kbs(2,3)) #6
print(id(kbs),  id(funcTimes)) #1451267324192 1451267324192
mbc=sbs=kbs
del funcTimes #funcTimes 변수 삭제
#print(funcTimes(2,3)) #NameError: name 'funcTimes' is not defined
print(mbc(2,3)) #6. 주소를 가지고 있으므로 참조가 가능함.

print('\n----------클로저를 사용하지 않는 경우-------------')
def out():
    count=0
    def inn():
        nonlocal count #inn에서 선언된 것이 아닌 out에서 선언된것. nonlocal 안쓰면 에러뜸. 
        count += 1
        return count
    print(inn()) 
#print(count) #err
out() #1
out() #1

print('\n----------클로저를 사용하는 경우-------------')
#클로저: 함수가 종료된 이후에도, 그 함수 안에서 사용하던 지역 변수를 기억하고 있는 함수
def outer():
    count=0
    def inner():
        nonlocal count #inn에서 선언된 것이 아닌 out에서 선언된것. nonlocal 안쓰면 에러뜸. 가장 가까운 바깥 함수(outer)의 지역 변수
        count += 1
        return count
    return inner # <==요게 클로저 : 내부 함수의 주소를 반환 #count 값은 inner가 기억중

var1 = outer() #내부 함수의 주소를 변수에 저장
print('var1: 주소', var1) #var1: 주소 <function outer.<locals>.inner at 0x00000261A99A1080>
print(var1()) #1
print(var1()) #2
myvar = var1() 
print(myvar) #3
print()
var2=outer()  # 새로운 객체(inner) 생성
print(var2()) # 1
print(var2()) # 2
print(var1,var2)

print('수량*단가*세금 한 결과를 출력하는 함수 작성')
def outer2(tax): #tax는 지역 변수 (함수 안에서 정의되므로)
    def inner2(su, dan):
        amount = su*dan*tax
        return amount
    return inner2 # <== 요게 클로저! 내부함수 반환 outer2(0.1)  →  inner2 (함수)

#1분기에는 su*dan에 대한 tax는 0.1부과
q1=outer2(0.1) #inner2의 주소 기억 . q1 = outer2(0.1), q1 = inner2
result = q1(5, 50000) #inner2(5, 50000)
print('result: ', result) 
result2 = q1(2, 10000) 
print('result2: ', result2)

#2분기에는 su*dan에 대한 tax는 0.05부과
q2=outer2(0.05) #inner2의 주소 기억
result3 = q2(5, 50000)
print('result3: ', result3)
result4 = q2(2, 10000)
print('result4: ', result4)


print()
print('\n일급함수 : 함수 안의 함수, 인자로 함수 전달, 반환값이 함수')
def func1(a,b):
    return a + b 

func2 = func1
print(func1(3,4))
print(func2(3,4))
print()

def func3(fu): #인자로 함수 전달
    def func4(): #함수 안의 함수
        print('나는 내부함수야~~')
    func4()
    return fu #반환값이 함수

mbc = func3(func1) #mbc = func1
print(mbc(3,4))

print()
print('\n축약함수(Lamda function) : 이름이 없는 한 줄짜리 함수')
#형식 : lamda 매개변수들,,,: 반환식 <=return 없이 결과 반환
def hapFunc(x,y):
    return x+y
print(hapFunc(1,2))
# 람다로 표현
print((lambda x,y : x+y)(1,2)) #람다로 한줄로 표현
gg = lambda x,y : x+y
print(gg(1,2))

kbs = lambda a, su=10: a+su
print(kbs(5)) #15
print(kbs(5,6)) #11

sbs= lambda a, *tu, **di : print(a, tu, di)
sbs(1,2,3,var1=4,var2=5) #1 (2, 3) {'var1': 4, 'var2': 5}

li = [lambda a,b : a+b,lambda a,b : a*b]
print(li[0](3,4))
print(li[1](3,4))

print('\n 다른 함수에서 람다 사용하기')
#filter(함수, 반복가능한 객체)
print(list(filter(lambda a:a<5, range(10)))) #0~9숫자들 중 5보다 작은 수만 걸러서 list 형태로 반환해줘. [0, 1, 2, 3, 4]
print(list(filter(lambda a:a%2, range(10)))) #0이면 False, 1이면 True. 참이 반환되므로 [1, 3, 5, 7, 9]

#문제) 1~100 사이의 정수 중 5의 배수이거나 7의 배수만 출력
print(list(filter(lambda a:a%5==0 or a%7==0, range(1,101))))



