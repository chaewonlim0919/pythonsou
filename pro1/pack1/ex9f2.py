#사용자 정의 함수
'''
def 함수명(가인수,,,):
    return 반환값 #1개만 반환, return이 없으면 return None

함수명(실인수,,,) #함수 호출
''' 

def doFunc1():
    print('doFunc1 수행')

def doFunc2(name):
    print('name : ', name)
    #return None과 동일 

def doFunc3(arg1, arg2):
    re = arg1 + arg2
    return re
    
def doFunc4(a1,a2):
    imsi =a1+a2
    if imsi%2==1:
        return
    else:
        return imsi
doFunc1() #함수호출 doFunc1 수행

#doFunc2() #TypeError: doFunc2() missing 1 required positional argument: 'name'
doFunc2(7) #function 제작 후 파라미터 처리 
doFunc2('길동') #들어오는 데이터에 따라 타입 결정
#doFunc2('길동','순신') #TypeError: doFunc2() missing 1 required positional argument: 'name'. 갯수를 맞춰줘야 함 

print(doFunc3("대한","민국"))
print(doFunc3(5,6))
result = doFunc3("5","6")
print(result)

print(doFunc4(3,4)) #None
print(doFunc4(3,5)) #8
#자원의 재활용 목적으로 만드는 것이 함수/ class도 잘 알아둬야 함

def triArea(a,b):
    c=a*b/2
    triAreaPrint(c) #다른 함수 호출
def triAreaPrint(cc):
    print('삼각형의 면적은 ', cc)
triArea(20,30)

def passResult(kor, eng):
    ss = kor + eng
    if ss >=50:
        return True #반환값이 Boolean일 수 있음 
    else:
        return False
    
if passResult(20,50):
    print('합격')
else:
    print('불합격')

def swapFunc(a,b):
    return b,a #return(b,a)

a=10; b=20
print(a, ' ', b) #10   20
print(swapFunc(a,b)) #(20, 10)

print()
def funcTest():
    print('funcTest 멤버 처리')
    def funcInner():
        print('내부 함수')
    funcInner()
funcTest()

#if 조건식 안에 함수 사용
def isOdd(para):
    return para%2==1 #홀수이면 True 반환
mydict = {x:x*x for x in range(11) if isOdd(x)} #comprehension. key:value
print(mydict)

print('변수의 생존 범위 (scope rule)-----')
#변수가 저장되는 이름공간은 변수가 어디서 선언되었는가에 따라 생존 시간이 다름
#전역, 지역 변수 
#Local > Enclosing function > Global > Built-in 
player = '전국대표' #전역 변수 (현재 모듈 어디서든 호출 가능)
name = '한국인'
def funSoccer():
    name = '홍길동' #지역 변수 (현재 함수 내에서만 호출 가능)
    #player = '지역대표' 주석처리하면 전역변수 호출
    city = '서울'
    print(f'이름은 {name} 수준은 {player}') #함수수준
    print(f'지역은 {city} ') #함수수준
funSoccer()

print(f'이름은 {name} 수준은 {player}') #모듈수준. 
#print(f'지역은 {city} ') #NameError: name 'city' is not defined. 지역변수는 전역변수로 호출될 수 없음.

print()
a=10; b=20; c=30
def Foo():
    a=7
    b=100
    def Bar(): 
        global c # c라는 변수는 전역변수가 됨. Bar 함수의 멤버가 아니라 모듈(파일)의 멤버가 됨.
        nonlocal b #b는 Foo의 멤버가 됨
        b=8 #지역변수 non local 쓰면서 수준이 Foo 수준이 됨. 
        print(f'Bar 수행 후 a:{a}, b:{b}, c:{c}')
        c=9 # global c가 없었다면 Error. 
        b = 200
    Bar()
    print(f"Foo 수행 후 a:{a}, b:{b}, c:{c}")
Foo()
print(f'함수 수행 후 a:{a}, b:{b}, c:{c}')  


print()
g=1
def func():
    global g
    a=g
    g=2 
    return a
print(func())
print('g: ',g) 