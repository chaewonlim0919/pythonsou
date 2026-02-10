# 추상 클래스(abstract class)
# 추상 메소드를 가진 클래스를 추상 클래스라고 하며 
# 얘는 인스턴스 할 수 없다. 객체 생성 불가.
# 부모 클래스로만 사용됨.

#공통 규칙(설계도)만 정의하고, 실제 구현은 자식 클래스
# 
# 
# 
# 에게 강제로 맡기는 클래스

from abc import *

class AbstractClass(metaclass=ABCMeta):  #추상클래스  #추상 메소드를 하나라도 가지고 있으면 추상 클래스 
    @abstractmethod #장식자를 가지고 있으면 추상 클래스 
    def abcMethod(self):     #추상메소드 .오버라이딩 필수
        pass

    def normalMethod(self):  #일반메소드. 오버라이딩 선택
        print('추상클래스 내의 일반 메소드')


#parent = AbstractClass()    #에러:추상클래스는 객체 생성 불가

class Child1(AbstractClass):   #상속
    name = '난 Child1'

    def abcMethod(self):    #선언 강요 (추상 메소드 오버라이딩 안하면 Error, 오버라이딩 하면 추상의 마법에서 빠져나감. 안할 시 자식도 추상 상태.) 
        print('부모가 가진 abcMethod 재정의 : 강요당함 ㅜㅜ')

c1 = Child1()            #생성된 객체의 주소를 치환
print('name: ', c1.name)
c1.abcMethod()          #Bound Method call
c1.normalMethod()

#추상을 만드는 이유는 다형성이 목적이고, 오버라이딩을 강요하기 위함. 

class Child2(AbstractClass):   #상속
     def abcMethod(self):    #선언 강요
         print('추상 메소드를 Child2에서도 오버라이드함')

     def normalMethod(self):  #일반 메소드 재정의(오버라이딩) , 옵션
         print('일반 메소드 내 맘대로 내용 변경')

print()
c2 = Child2()             #클래스를 치환
c2.abcMethod()        #UnBound Method call
c2.normalMethod()

print()
happy = c1
happy.abcMethod()
happy = c2
happy.abcMethod()

# print('\n다형성 -----')
# parent = AbstractClass   #추상클래스 타입의 변수 선언은 가능
# print(type(parent))
# parent = c1
# parent.abcMethod()
# parent.normalMethod()  #추상클래스의 메소드 수행

# print()
# parent = c2
# parent.abcMethod(parent)
# parent.normalMethod(c2)  #자식클래스의 메소드 수행



