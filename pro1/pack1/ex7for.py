#반복문 for
#for i in [1,2,3,4,5]
#for i in (1,2,3,4,5)
for i in {1,2,3,4,5}: #for은 묶음형자료에서 하나씩 꺼내씀
    print(i, end='')

print('\n분산/표준편자 ---')
#편차: 원데이터 - 평균
#표준편차: 루트 분산 = (편차)^2의 합/갯수 
#numbers = [1,3,5,7,9] #합은 25, 평균은 5.0, 분산: 8.0, 표준편차: 2.8284271247461903
#numbers = [3,4,5,6,7] #합은 25, 평균은 5.0, 분산: 2.0, 표준편차: 1.4142135623730951
numbers = [-3,4,5,7,12] #합은 25, 평균은 5.0 분산: 23.6, 표준편차: 4.857983120596447
tot=0
for a in numbers:
    tot += a 
print(f"합은 {tot}, 평균은 {tot/len(numbers)}")
avg = tot / len(numbers)
#편차의 합
hap = 0
for i in numbers:
    hap += (i-avg)**2 #편차제곱의 합
print(f'편차 제곱의 합: {hap}')
vari = hap / len(numbers)
print(f'분산: {vari}')
print(f'표준편차: {vari**0.5}')

print()
colors = ['r', 'g', 'b']
for v in colors:
    print(v, end=' ')
print('ier(): 반복 가능한 객체를 하나씩 꺼낼 수 있는 상태로 만들어 주는 함수 ')
iterator = iter(colors)
for v in iterator:
    print(v, end= ',')
for idx, d in enumerate(colors): #enumerate: 인덱스와 값을 반환
    print(idx, ' ', d)

print('\n사전형---')
datas = {'python':'만능언어', 'java':'웹용언어', 'mariadb':' RDBMS' }
for i in datas.items():
    print(i[0], ' ~~ ', i[0])
for k, v in datas.items():
    print(k, ' -- ', v)
for val in datas.values():
    print(val, end= ' ')


print('\n다중 for --------------')
for n in [2,3]:
    print('---{}단---'.format(n))
    for i in [1,2,3,4,5,6,7,8,9]:
        print('{}*{}={}'.format(n,i,n*i)) 

print('continue, break----------') #while문과 비슷
nums = [1,2,3,4,5]
for i in nums:
    if i==2: continue
    if i==4: break
    print(i, end=' ')
else:
    print('정상종료')

print('\n정규 표현식 + for')
str = '''그는 "민주당 내부에서 격렬한 논쟁이 벌어지고 있지만 비전과 정책을 놓고 벌어지는 생산적인 논쟁은 아닌 것 같다"며 "혁신당을 공격한다고 해서 민주당의 내부 문제가 해결되지는 않는다"고 지적했습니다.
그러면서 "높은 정치의식과 오랜 정치 경험이 있는 민주당 당원들의 집단 지성을 믿는다"며 "민주당의 내부 이견이 해소될 때까지 기다리겠다"고 했습니다.'''
import re
str2=re.sub(r'[^가-힣\s]','',str) #r선행. 한글과 공백 이외(^)의 문자는 공백처리
print(str2)
str3 = str2.split(' ') #공백을 구분자로 문자열 분리 
print(str3)
cou = {} #set 아님 dict. 들어오는 데이터 타입에 따라 결정
for i in str3:
    if i in cou:
        cou[i] += 1 #같은 단어가 있으면 누적
    else:
        cou[i] = 1 #최초 단어인 경우는 '단어':1
print(cou)

print('정규표현식 좀 더 연습')
for test_ss in ['111-1234', '일이삼-일이삼사', '222-1234', '333&1234']:
    if re.match(r'^\d{3}-\d{4}$', test_ss): #대괄호안에 있으면 부정이고, 대괄호 밖에 있으면 처음부터를 의미. \d는 숫자를 의미.$는 끝나. 즉, 숫자로 시작하고 숫자로 끝남
        print(test_ss, '전화번호 맞아요')


    else:
        print(test_ss, '전화번호 아니야')

print('comprehension : 반복문 + 조건문 + 값 생성을 한 줄로 표현')
a= [1,2,3,4,5,6,7,8,9,10]
li = []
for i in a:
    if i%2 == 0:
        li.append(i)
print(li)

print(list(i for i in a if i %2 == 0)) #위와 동일. comprehension

datas = {1 , 2, 'a', True, 3.0, 2, 1, 2, 1, 2, 2} #set | 중복X
# datas = [1, 2, 'a', True, 3.0]
li2 = [i*i for i in datas if type(i)==int] #comprehension. 자주씀
print(li2) #[1, 4]

id_name = {1:'tom', 2:'oscar'}
name_id = {val:key for key, val in id_name.items()}
print(name_id)

print()
print([1,2,3])
print(*[1,2,3]) # * : unpack . 1 2 3

aa = [(1,2), (3,4), (5,6)]
for a,b in aa:
    print(a+b)

print([a+b for a, b in aa]) #[3, 7, 11]
print(*[a+b for a, b in aa], sep='\n') 
'''
3
7
11
'''

print('\n수열 생성 : range')
print(list(range(1,6))) #[1, 2, 3, 4, 5]
print(list(range(1,6,1))) #[1, 2, 3, 4, 5]
print(tuple(range(1,6,2))) #(1, 3, 5)
print(list(range(-10,-100,-20))) #[-10, -30, -50, -70, -90]
print(set(range(1,6)))
print()

for i in range(6):
    print(i, end=' ') #0 1 2 3 4 5

for _ in range(6):
    print('반복')

tot=0
for i in range(1,11):
    tot += i #누적
print('tot : ', tot)

for i in range(1,10):
    print(f'2*{i}={2*i}')

#문1 : 2~9 구구단 출력 (단은 행 당위 출력)
print('구구단')
for j in range(2,10):
    for i in range(1,10):
        print(f'{j}*{i}={j*i}', end=' ')
    print()

#문2 : 주사위를 두 번 던져서나온 숫자들의 합이 4의 배수가 되는 경우만 출력
for i in range(6):
    n1=i+1
    for j in range(6):
        n2 = j+1
        n=n1+n2
        if n%4 ==0:
            print(n1,n2)

print()
for i in range(1,7,1):
    for j in range(1,7,1):
        su = i+j
        if su %4 ==0: print(i,j)

print('\nend')