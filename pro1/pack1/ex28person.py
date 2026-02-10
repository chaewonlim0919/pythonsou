#상속

class Person:
    say = '난 사람이야~~~' # 접근권한: public
    nai = '20'
    __msg = ' good: private 멤버'

    def __init__(self, nai):
        print('Person 생성자')
        self.nai = nai

    def printInfo(self): # 접근권한: public
        print(f'나이: {self.nai}, 이야기: {self.say}')

    def helloMethod(self):
        print('안녕')
        print('hello: ', self.say, self.nai, self.__msg)

print(Person.say, Person.nai)
#Person.printInfo() #이건 안된다고 말했음
per = Person(25)
per.printInfo()
per.helloMethod()

print('---'*10)
class Employee(Person):
    subject = '근로자'
    say = '일하는 동물' #hiding(shadowing)

    def __init__(self):
        print('Employee 생성자')
    
    def printInfo(self): # 접근권한: public  
        print('Employee 클래스의 printInfo 호출됨')

    def ePrintInfo(self):
        print(self.subject, self.say, self.nai) #우선 클래스 멤버변수 뒤지고, 없으면 부모 멤버 변수 가서 뒤짐.
        #print(self.__msg)   #Error. private(이름 앞에 __ 쓰면 됨) 멤버(): Person에서만 유효
        self.helloMethod()
        self.printInfo() # 나이: 20, 이야기: 일하는 동물 -> 결과 이해하기 , #지역이 우선임
        print(super().say) # super 시, 부모의 멤버 (super는 바로 이전 부모에게만 갈 수 있음!!!!!!!!!)
        super().printInfo() #나이: 20, 이야기: 일하는 동물 

emp = Employee() #emp가 가지는 주소를 self가 가지고 돌아댕김
print(emp.subject, emp.nai, emp.say) #부모 잘 만나서 emp.nai, emp.say 쓸 수 있게 됨.
emp.ePrintInfo()


print('---'*10)
class Worker(Person):
    def __init__(self, nai):
        print('Worker 생성자')
        super().__init__(nai) #부모 클래스의 생성자 호출

    def wPrintInfo(self):
       print('Worker - wPrinfInfo 처리')
       #self.printInfo() #Worker에서 뒤지다 없으면 부모에게 감 
       super().printInfo() # 자식이 printInfo()없으므로 그냥 바로 부모에게 가라고 super()붙임

wor = Worker('30')
print(wor.say, wor.nai)
wor.wPrintInfo()

print('==='*10)
class Programmer(Worker):
    def __init__(self, nai):
        print('Programmer 생성자')
        # super().__init__(nai)     # Bound call
        Worker.__init__(self,nai)   # Unbound call
    
    def pPrintInfo(self):
        print('Programmer -pPrintInfo 처리하였음')
    
    def wPrintInfo(self): #부모 메소드와 동일 메소드 선언
        print('Programmer에서 overriding')

pro = Programmer(35)
print(pro.say, pro.nai)
pro.pPrintInfo()
pro.wPrintInfo()


print('\n클래스 타입 확인')
a = 3; print(type(a)) #<class 'int'>
print(type(pro)) #<class '__main__.Programmer'>
print(type(wor)) #<class '__main__.Worker'>
print(Person.__bases__) #(<class 'object'>,) -> 모든 클래스는 object의 자식이었음. 
print(Employee.__bases__) #(<class '__main__.Person'>,)
print(Worker.__bases__) #(<class '__main__.Person'>,)
print(Programmer.__bases__) #(<class '__main__.Worker'>,)