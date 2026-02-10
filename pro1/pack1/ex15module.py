#pack1/ex15module - main
print('사용자 정의 모듈 처리하기')
s=20 #뭔가를 하다가...
print('\n경로 지정 방법1: import 모듈명')
import pack1.mymod1 #같은 패키지 안에 있어도 반드시 import 해야함
print(dir(pack1.mymod1))
print(pack1.mymod1.__file__)
print(pack1.mymod1.__name__)
list1 = [1,2]
list2 = [3,4,5]
pack1.mymod1.listHap(list1,list2)
if __name__ == '__main__': print('와우 메일모듈~~~~')

# #pack1/mymod1
# tot = 100 #전역변수

# def listHap(*ar):
#     print(ar)
#     if __name__ == '__main__':
#         print('나는 메일모듈~~~~') #python ex15module.py으로 실행시킬 경우, 조건이 False이므로 출력X

# def kbs():
#     print('대한민국 대표방송')

# def mbc():
#     print('문화방송')

print('\n경로 지정 방법2: from 모듈명 import 함수명 또느 변수')
from pack1.mymod1 import kbs
kbs()

from pack1.mymod1 import mbc, tot
mbc()
print(tot)

from pack1.mymod1 import * # *을 사용해 mymod1 모듈의 모든 메머 로딩 (비권장)
print('tot: ', tot)

from pack1.mymod1 import mbc as 엠비씨만세별명 #별명
엠비씨만세별명()

print('\n경로 지정 방법3: import 하위패키지. 모듈명')
import pack1.subpack.sbs as nickname
nickname.sbsMansae()

print('\n경로 지정 방법4: 현재 package와 동등한 패키지 모듈읽기')  #C:\work\projects\pro1>python -m pack1.ex15module / 이제부터 pack1.을 붙여줘야 함
#import ../pack1_other.mymod2  
from pack1_other import mymod2
mymod2.hapHunc(4,3)

#aaconda3>envs>myproject>Lib 폴더 mymod3.py 붙여넣기
import mymod3
result = mymod3.gopFunc(4,3)
print('path가 설정된 곳의 module 읽기 - result: ', result)

print('end')