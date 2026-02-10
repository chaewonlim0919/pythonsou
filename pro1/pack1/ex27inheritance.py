# 상속 : 자원의 재활용을 목적으로 특정 클래스의 멤버를 가져다 쓰는 것
# 코드 재사용
# 확장성 - 기존 클래스에 새 기능을 추가한 새로운 클래스 생성
# 구조적 설계 - 공통개념은 부모 클래스, 구체적 내용은 자식 클래스에서 구현
# 다형성 구사 - 메소드 오버라이딩 
# 클래스 강결함 - 상속 / 클래스 약결함 - 포함 (강결합일 경우, 유지 보수 어려움)

class Animal: # 동물들이 가져야할 공통 속성과 행위 선언
    age =1 

    def __init__(self): #부모는 생성자가 이미 수행되어 로그에 'Animal 생성자' 안찍힘. 자식 생성자 로그는 찍힘
        print('Animal 생성자')
        

    def move(self):
        print('움직이는 생물')

class Dog(Animal):  #상속 - Animal: 부모, 조상, super, parent. / Dog: 자식, 자손, 파생, sub, child
    def __init__(self):
        print('Dog 생성자')

    def my(self):
        print('댕댕이라고 해요')
    
dog1 = Dog()
dog1.my()
dog1.move() #로컬(자식)부터 뒤지다가 없으면 글로벌(부모)로 올라감 
print('age: ', dog1.age)
print()
dog2 = Dog()
dog2.my()
dog2.move()

class Horse(Animal):
    pass

horse1 = Horse() 
horse1.move() #Horse(자식) 생성자 수행할 것(명시적으로 적지 않음)이 없으므로 Animal()(부모) 생성자를 수행하여 로그에 'Animal 생성자' 찍힘

#print(Animal.age)