#문제 ) 커피머신 자판기
class CoinIn:
    coin = 0
    change = 0

    def calc(self, cupCount):
        price = cupCount * 200
        if self.coin < price:
            return False
        self.change = self.coin - price
        return True





class Machine:
    cupCount = 1
    def __init__(self):
        self.coinin = CoinIn()     #Machine 클래스가 CoinIn 클래스 포함

    def showData(self):
        self.coinin.coin = int(input('동전을 입력하세요: '))
        self.cupCount = int(input('몇 잔을 원하세요: '))

        if not self.coinin.calc(self.cupCount):
            print('요금 부족')
        else:
            print(f'커피 {self.cupCount}잔과 잔돈 {self.coinin.change}원')

machine = Machine()
machine.showData()


# class Engine:
#     def start(self):
#         print("엔진 시동")

# class Car:
#     def __init__(self):
#         self.engine = Engine()  # has-a

#     def drive(self):
#         self.engine.start()
#         print("차가 달린다")


# car = Car()
# car.drive()