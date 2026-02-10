# 여러 개의 부품 객체를 조립해 완성차 생성
# 클래스의 포함 관계 사용 (자원의 재활용)
# 다른 클래스를 마치 자신의 멤버처럼 선언하고 사용
# -> 클래스, 객체, 인스턴스 차이 알기
# class PohamHandle:
#     quantity = 0 #핸들 회전량 (공유자원)

#     def leftTurn(self, quentity):
#         self.quantity = quentity #지역변수로, 지역변수 없으면 공유자원값이 들어감
#         return "좌회전"
    
#     def rightTurn(self, quentity):
#         self.quantity = quentity
#         return "우회전"
from ex23pohamhandle import PohamHandle

class PohamCar:
    turnShowMessage = '정지'

    def __init__(self, ownerName):
        # ownerName = ownerName #이렇게 쓰면 안됨.
        self.ownerName = ownerName
        self.handle = PohamHandle()  # 클래스의 포함관계

    def turnHandle(self, q):
        if q > 0:
            self.turnShowMessage = self.handle.rightTurn(q) #handle이 PohamHandle의 주소를 가지고 있음. ('.'이 두개 이상 있으면 클래스의 포함관계구나 생각하면 됨)
        elif q < 0:
            self.turnShowMessage = self.handle.leftTurn(q)
        elif q == 0:
            self.turnShowMessage = 0

if __name__ == '__main__': #얘가 메인이구나 ~~~
    tom = PohamCar('미스터 톰') 
    tom.turnHandle(10)
    print(tom.ownerName + '의 회전량은' + tom.turnShowMessage + ' ' + str(tom.handle.quantity))

    john = PohamCar('존')
    john.turnHandle(-20)
    print(john.ownerName + '의 회전량은' + john.turnShowMessage + ' ' + str(john.handle.quantity))
