a=1 #초기값
while a <= 5:
    print(a) #참이면 수행(무한반복)이고, 거짓이면 조건문 빠져나감.
    #a=6 # 이 줄 추가하면 거짓이므로 조건문 빠져나감  
    a= a+1 #변수 변화 (while문의 특징)

else: #else구문은 보통 continue, break와 함께 쓰임
    print('수행성공')

print()
i=1
while i <=3:
    j=1
    while j <=4:
        print('i=' + str(i) + '/j=' + str(j))
        j=j+1
    i=i+1

print('1~100 사이의 정수 중 3의 배수의 합 ---')
su=1; hap=0
while su <= 100:
    #print(su)
    if su % 3 == 0:
        #print(su)
        hap += su # hap = hap + su
    su += 1
print('합은',hap)

print()
colors = ['빨강', '파랑', '노랑', '검정']
#num=0
#print(colors[num])
#print(colors[1])
#print(colors[2])

num=0
#while num <3:
while num < len(colors): #요소 4개라 4임
    print(colors[num])
    num += 1

print('\n별 찍기 ----')
i=1
while i <=10:
    j=1
    msg=''
    while j <= i:
        msg += "*"
        j += 1
    print(msg)
    i += 1
'''
print('if 블럭 내 while 블럭 사용 --- ')
import time
sw = input('폭탄 스위치를 누를까요?[y/n]')
print("sw: ", sw)
if sw == 'Y' or sw == 'y':
    #pass
    count = 5
    while 1 <= count:
        print('%d초 남았습니다'%count)
        time.sleep(1) #1초 후 다음 문장 실행
        count -=1
    print('폭발')
elif sw == 'N' or sw == 'n':
    print('작업 취소')
else:
    print('y또는 n을 누르세요.')

print('end') 
'''
#
'''
여러줄 주석을 이용해 각 문장 돌려보기 

'''

print('\ncontinue/break ---')
a=0
while a<10:
    a+=1
    if a==3:
        continue #아래 문장을 무시하고 while 로 이동 
    if a==5:
        continue
    #if a==7:
       # break #while문 무조건 탈출
    print(a)
else:
    print('정상종료')
print('while 수행 후 %d'%a)

print('\n키보드로 숫자를 입력받아 홀수 짝수 확인하기(무한반복) ---')
while True: # True문은 break를 만나지 않는 이상 무한반복이며 못 빠져나감. True, 1, 100. -12, 4.5 모두 'ok' ...
    mysu = int(input('확인할 숫자 입력(예:5): '))
    if mysu == 0:
        print('프로그램 종료')
        break
    elif mysu%2 ==0: #2로 나눈 나머지가 0
        print('%d는 짝수'%mysu)
        continue
    elif mysu%2 == 1:
        print('%d는 홀수'%mysu)


print('end')


