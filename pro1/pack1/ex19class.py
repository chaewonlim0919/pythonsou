#oop(객체 중심 프로그래밍 기능) : 새로운 타입 생성, 포함, 상속, 다형성 등을 구사
#class(설계도)로 인스턴스 해서 객체를 생성(별도의 이름 공간을 갖음)
#객체는 멤버필드(변수)와 메소드로 구성
#자바와 달리 접근 지정자가 없다. 메소드 오버로딩 없다.
#모듈의 멤버 : 변수, 명령문, 함수, 모듈, 클래스

print('뭔가를 하다가 객체 만들기')

class TestClass:
    aa=1 #멤버필드(변수). 현재 클래스 내에서 전역

    def __init__(self): #특별한 메소드 (초기화할게 없으면 안적어도 됨)
        print('생성자: 객체 생성시 가장 먼저 1회만 호출 - 초기화 담당') 
    
    def __del__(self): #소멸자 안적어도 됨. 필요시에만!
        print('소멸자 : 프로그램 종료시 자동실행. 마무리 작업')

    def printMsg(self): #일반 메소드 (메소드는 반드시 argument, 즉 self를 가지고 다녀야함)
        name = '한국인' #지역변수: printMsg에서만 유효
        print(name)

print(TestClass) #just Type만
test = TestClass() #객체 생성 한 개
print('test객체의 멤버 aa: ', test.aa) #클래스의 멤버는 객체변수에 .을 찍어주면 쭉 나옴

print()
# method call
test.printMsg() # 1. Bound Method call, self에 들어갈 객체가 없음
#TestClass.printMsg() #self에 들어갈 객체가 없음
TestClass.printMsg(test) #2. UnBound Method call, 메서드를 클래스에서 직접 호출


print(type(1)) #<class 'int'>
print(type(1.0)) #<class 'int'>
print(type(test)) #<class '__main__.TestClass'>
print(id(test)) 
print(id(TestClass))

print()
test2 = TestClass() #객체 생성 한 개 더
#test2 = TestClass() 를 실행하면 새로운 객체(test2)가 하나 더 생성되고, 기존에 test가 가리키던 객체는 그대로 살아 있다.
#이후 프로그램이 종료될 때 test와 test2가 가리키던 객체 두 개가 각각 소멸되어 소멸자가 두 번 호출된다.
#print(id(test2))