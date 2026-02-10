# for i in {1, 2, 3, 4, 5, 5, 5, 5}:
#     print(i, end = ' ')

# i = {1, 2, 3, 4, 5, 5, 5, 5}
# print(i)

# print()
# tot = 0; li = []
# for i in range(1,100):
#     if i%3==0 or i%4 ==0 and i%7 != 0:
#         print(i, end=' ')
#         li.append(i)
#         tot += i
# print(f'건수: {len(li)}')
# print(f"배수의 총합: {tot}")

# *v1, v2, v3 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
# print(v1)
# print(v2)
# print(v3)

# v1 = {1, 1, 2, 3}
# print(v1)

# hap = lambda m,n : m+n*5
# #실행하려면
# print(hap(2,3))

# print(list(range(1, 6, 2)))

# def divide(a,b):
#     return a/b
# try:
#     #실행문(예외 발생 가능 구문)
#     c = divide(5,2)
#     # c = divide(5,0)
#     print(c)

#     aa = [1,2]
#     print(aa[0])
#     # print(aa[3])   # IndexError: list index out of range, 인덱스 에러 처리 함수는 따로 있음

#     open("c:/work/abc.txt")
# except ZeroDivisionError:  # 예외 종류 관련 클래스 
#     print('두번째 값은 0을 주면 안돼요')  # 예외 발생


# try: 
#     aa = int(input())
#     bb = 10 / aa
#     print(bb)
# except ZeroDivisionError:
#     print('Error: 0은 입력하면 안돼요.')

# except Exception as e:  # 모든 에러들을 Exception으로 모두 처리할 수 있음. 근데 만약 특정 에러들만 처리하고 싶다면 위처럼 해야함
#     print('에러: ', e)

# i=10
# msg  = ' '
# while 1 <= i <= 10:
#     j = 1
#     while j <= i:
#         print('*', end='')
#         j +=1
#     print()
#     print(msg, end= '')
#     msg += ' '
#     i-=1

# i = 0
# while True:
#     if i%10 != 3:
#         i += 1
#         continue 
#     if i > 100: break   
#     print(i, end=' ')
#     i+=1


i=2; j=1
while i <10:
    if i%2==1:
        print(f'{i}*{j}={j*i}', end=' ')
    j += 1
    if j==10:
        j=1
        i += 1
        print()

print()
class Bicycle:
    name = ' '
    wheel = 0
    price = 0
    def __init__(self, name, wheel, price):
        self.name = name
        self.wheel = wheel
        self.price = price
    def pay(self):
        amount = self.wheel*self.price
        return amount
    def display(self):
        print(f'{self.name}님 자전거 바퀴 가격 총액은 ', end='')
        print(str(self.pay()) + '원 입니다.')

gildong = Bicycle('길동', 2, 50000)
gildong.display()

print()
def Process():
    a = int(input('연도 입력: '))
    if a %4 ==0 and a%100 != 0 or a%400 ==0:
        print(f'{a}년은 윤년')
    else:
        print(f'{a}년은 평년')

Process()
