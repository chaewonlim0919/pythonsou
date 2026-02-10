#function:여러 개의 수행문을 하나의 이름으로 묶은 실행 단위
# 함수 고유의 실행 공간을 가짐
#자원의 재활용

#내장의 일부 체험
print(sum({1,2,3})) #6
print(bin(8)) #0b1000
print(eval('4+5')) #9
print(round(1.2), round(1.6)) #반올림

import math 
print(math.ceil(1.2), ' ', math.ceil(1.2)) #x보다 크거나 같은 가장 작은 정수
print(math.floor(1.2), ' ', math.floor(1.2)) #x보다 작거나 같은 가장 큰 정수

b_list= [True, 1, False]
print(all(b_list)) #False. 리스트(또는 튜플) 안의 값이 전부 True면 True.하나라도 False가 있으면 False
print(any(b_list)) #True. 하나라도 True면 True

data1=[10,20,30]
data2=['a','b']
for i in zip(data1, data2):
    print(i)
#(10, 'a')
#(20, 'b')

print()
data1=[10,20,30]
data2=['a','b']
for i in [data1, data2]:
    print(i)
#[10, 20, 30]
#['a', 'b']