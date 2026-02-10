class Car:
    handle = 1
    speed = 0

    def __init__(self, name, speed): # 현재객체의 name에게 name(지역변수) 인자값 치환
        self.name = name
        self.speed = speed

    def showData(self):
        km = '킬로미터'
        msg = '속도:' + str(self.speed)
        return msg
    
    def printHandle(self):
        return self.handle #클래스의 멤버를 찾기 위해 self를 써줘야만 함.
    
print(Car.handle) #원형(prototype) 클래스의 멤버 호출 
car1 = Car('tom', 10) #생성자 호출 후 객체 생성 (인스턴스화)/ car1은 주소를 가지고 있음
#tom,10은 self에 저장되고, car1이라는 지역변수에 저장됨. Car는 오히려 전역느낌. 
print('car1 객체 주소: ',car1)
print('car1: ', car1.name, ' ', car1.speed, car1.handle)
car1.color = '파랑' 
print('car1.color: ', car1.color)
car2 = Car('john', 20) #생성자 호출 후 객체 생성(인스턴스화)
print('car2 객체 주소: ', car2)
print('car2: ', car2.name, ' ', car2.speed, car2.handle)
#print(Car.color, car2.color) #상관없음
print(id(Car), id(car1), id(car2)) #주소 전부 다 다름
print(car1.__dict__)
print(car2.__dict__) #멤버들 확인. 

print('--메소드---------------')
print('car1 speed: ', car1.showData()) #인터프리터가 car1의 값을 들고 showData()의 self로 넘어감
print('car1 speed: ', car2.showData())
car1.speed = 80
car2.speed = 110
print('car1 speed: ', car1.showData()) #인터프리터가 car1의 값을 들고 showData()의 self로 넘어감
print('car1 speed: ', car2.showData())

print('car1 handle: ', car1.printHandle()) #우선 먼저 car1 메모리 가서 찾고, 안보이면 공유자원 클래스의 멤버변수쪽으로 가서 뒤짐.
print('car2 handle: ', car2.printHandle())