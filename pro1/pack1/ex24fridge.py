#클래스의 포함 관계 연습 - 냉장고 객체에 음식 객체 담기 
class Fridge:
    isOpened = False #냉장고 열렸는지 확인하는 변수
    foods = []
    def open(self):
        self.isOpened = True
        print("냉장고 문을 열기")

    def close(self):
        self.isOpened = False
        print("냉장고 문을 닫기")

    def foodsList(self):
        for f in self.foods:
            print(f'-{f.name} {f.expiry_date}')
        print()
    
    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print(f'냉장고에 {thing.name} 넣음')
            self.foodsList()
        else:
            print('냉장고 문이 닫혀있음')

class FoodData:
    def __init__(self, name, expiry_date):
        self.name = name
        self.expiry_date = expiry_date

fobj = Fridge()


apple = FoodData('사과', '2026-8-1')
fobj.put(apple) #냉장고 문이 닫혀있음

fobj.open()
fobj.put(apple)
fobj.close()

cola = FoodData('콜라', '2027-11-1')
fobj.open()
fobj.put(cola)
fobj.close()