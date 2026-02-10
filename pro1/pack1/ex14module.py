# Modeule: 소스 코드의 재사용을 가능하게 하며, 소스 코드를 하나의 이름 공간으로 구분하고 관리, 
# 하나의 파일은 하나의 모듈이 된다. 
#표준 모듈, 사용자 작성 모듈, 제 3자 모듈(third party)로 구분할 수 있다.
print(print.__module__) #builtins. print는 'builtins'의 모듈 속 존재. 아주 자주 쓰이는 것들은 import가 이루어져 있음. 
print('뭔가를 하다가...외부 모듈 사용하기')

import sys #sys는 파이썬 설치할 때 같이 들어오는 기본 모듈, 표준 라이브러리(Standard Library) 소속.
print(sys.path) 
a=1
if a > 3:
    sys.exit() #응용 프로그램의 강제 종료

import math
print(math.pi)

import calendar
calendar.setfirstweekday(6)
calendar.prmonth(2026,2)
del calendar

import random #난수 생성
print(random.random())
print(random.randrange(1,10))

from random import random, choice, randrange #from 모듈 import 멤버
#from random import * #추천하지 않음. RAM을 계속 돌려야 하므로
print(random())

print('end') #휘발성 RAM으로 프로그램 종료 후 기억X

