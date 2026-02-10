#연산자

v1=3
v1=v2=v3=5 #치환개념
print(v1,v2,v3) #id모두 동일

print('출력1', end = ',') #end는 출력을 이어감 
print('출력2') 
print('출력3') #print는 출력하고 line skip함.

v1, v2 = 10 , 20
print(v1, v2)

v2, v1 = v1, v2 #다른 언어는 서로 값을 맞바꿀 때, 임시기억장치를 만드나, 파이썬은 이 한줄로 값을 바꿀 수 있음
print (v1, v2)

print('값 할당 : packing 연산')
v1 = 1,2,3,4,5 # v1 = (1,2,3,4,5) 파이썬은 이 두개가 동일함. 그룹 개념. 
v1 = [1,2,3,4,5]

*v1, v2 = [1,2,3,4,5] #packing 개념으로 마지막은 v5, 나머지는 v1이 가진다
print(v1,' ',v2) # [1, 2, 3, 4]   5

v1, *v2 = [1,2,3,4,5] #packing 개념으로 마지막은 v5, 나머지는 v1이 가진다
print(v1,' ',v2)  # 1   [2, 3, 4, 5]

*v1, v2, v3 = [1,2,3,4,5] # [1, 2, 3]   4   5
print(v1,' ', v2,' ', v3)


print()
print(format(1.5678, '10.3f'))  # 전체 10칸이고, 소수점 3자리까지. 반올림해야함. 즉 공백 5칸 '     1.568'
print("나는 나이가 %d 이다." % 23) #%d는 정수 
print("나는 나이가 %s 이다." % "스물셋") #%s는 문자열
print("나는 나이가 %d 이고 이름은 %s이다." % (23, '홍길동'))
print("나는 나이가 %s 이고 이름은 %s이다." % (23, '홍길동'))
print("나는 키가 %f이고, 에너지가 %d%%." % (177.7, 100)) #%f : 실수 (기본 소수점 6자리)
print("이름은 {0}, 나이는 {1}".format('홍길이', 33))
print("이름은 {}, 나이는 {}".format('신선해', 33)) # {}는 앞에서부터 자동매치
print("이름은 {1}, 나이는 {0}".format(34, '강나루'))

abc = 123
print(f"abc의 값은 {abc}임")
#print()
print('\n \n본격적 연산 ------------') #\n, \b, \t ... -> line skip
print(5+3, 5-3, 5*3, 5/3, 5//3, 5%3, 3**3 ) #5/3은 실수,  5//3 몫만,  5%3는 나머지만 취함
#8 2 15 1.6666666666666667 1 2 27
print(divmod(5, 3),' ', 5%3) #(1, 2)   2
print(3+4*5+(2+3)/2) #25.5




#() > ** > 단항 > 산술(*,/ >  +,-) > 관계 > 논리 (not )

#논리연산자 
print(5>3, 5==3, 5!=3) #!=는 false
print(5>3 and 4<3, 5>3 or 4<3, not(5>=3))
print(True or False and False) #True
print(True and False or False) #and 연산 후 or 연산 (연산 우선순위)

print(4+5) #산술연산 '9'
print('4'+'5') #문자열 더하기 연산 '45'
print('한'+'국'+'만세')  #한국만세
print('한국'*5)  #한국한국한국한국한국

print('누적')
a=10
a= a+1 #a += 1
a += 1 #연산속도 더 빠름 ( -= , *= , /=)
print(f"a는 {a}")
# print(a++) #++. --: 증감 연산자X (다른언어에서 증감 연산자 있으나 파이썬에서는 없음)
print(--a) #부호 변경 없음 
print(-a) #부호가 바뀜
print(a*-1) #부호가 바뀜

print('1'+'1') #문자 11임
#print(('1'+'1') +1) #TypeError: can only concatenate str (not "int") to str (문자와 숫자는 못 더함)
print(int('1'+'1') +1) #결과 12     int(문자열) -> 정수화
print(float('1'+'1') +1) #결과 12.0
#print((1+1) + '1') #Type error
print(str(1+1) + '1') #결과 21 str(숫자) -> 문자화 
print('boolean 처리: ', bool(True), bool(False))
print(bool(1), bool(12.3), bool('ok'), bool([12])) #True True True True. 데이터가 있으면 True
print(bool(0), bool(0.0), bool([]), bool(None)) #None은 키워드임. False False False False , 0은 무의 제로로 봄.즉 값이 없음. 값이 없으면 False. 

# r 선행문자
print('aa\tbb') #\t는 tap키 
print('aa\nbb') # \n은 skip line
print(r'aa\tbb') #aa\tbb
print(r'aa\ntbb') #aa\ntbb 
#즉 순수하게 문자로 나타내려면 r을 선행하면 됨


