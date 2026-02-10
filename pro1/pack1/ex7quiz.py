
#1) 1 ~ 100 사이의 정수 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력
# a=0; hap=0
# while a<100:
#     a+=1
#     if a%2==0:
#         continue #아래 문장을 무시하고 while 로 이동 
#     if a%3==0:
#         continue
#     #print(a)
#     hap += a
# print(hap) 
#해설
i=0
total=0
while i <=100:
    if i%3==0 and i%2 != 0:
        print(i, end=' ')
        total += i
    i += 1
print(f'합은 {total}')




print()
#2) 2 ~ 5 까지의 구구단 출력
i=2
while i <=5:
    print(f'{i}단')
    j=1
    while j < 10:
        print(f'{i}*{j}={j*i}')
        j += 1
    i += 1
else:
    print()

print()


#3) 1 ~ 100 사이의 정수 중 “짝수는 더하고, 홀수는 빼서” 최종 결과 출력
i=1; even=0; odd=0
while i <= 100:
    if i%2==0:
        even += i
        # print(even) 2550
    else:
        odd += i
        #print(odd) 2500
    i += 1
else:
    print('짝수의 합: ', even)
    print('홀수의 합: ', odd)
    print(f'결과는 {even-odd}')

print()
#4) -1, 3, -5, 7, -9, 11 ~ 99 까지의 모두에 대한 합을 출력
i=1; minus=0; plus=0
while i<100:
    if i%4==1:
        #print(i)
        minus -= i
        #print(minus) #-1225
    elif i%4==3:
        #print(i)
        plus += i
        #print(plus) #1275
    i+=1
print(f'-1 + 3 - 5 + 7 - 9 + 11 - ... +  99 = {minus+plus}')


print()
#해설
i=-1
sum=0
while abs(i)<=99: #abs는 절댓값
    sum += i
    if i<0:
        i-=2
    else:
        i+=2
    i*-1
print(sum)

print()
#5) 1 ~ 100 사이의 숫자 중 각 자리 수의 합이 10 이상인 수만 출력 예) 29 → 2 + 9 = 11 (출력)
a=1; b=0
while 0 < 10*a + b <100:
    if a + b >= 10:
        print(f'{10*a + b} → {a} + {b} = {a+b}')
    b+=1
    if b == 10:
        b=0
        a += 1

print()
#해설
num=1
while num <=100:
    temp = num
    digit_sum = 0
    while temp > 0:
        digit_sum += temp%10 #나머지
        temp //= 10 #10의 자리 제거
    if digit_sum >= 10:
        print(num)
    num +=1





#6) 1부터 시작해서 누적합이 처음으로 1000을 넘는 순간의 숫자와 그때의 합을 출력 (힌트: 언제 멈출지 미리 모름 → while 적합)
i=1; su=0
while su < 1000:
    su +=i
    i += 1
print(f'그 때의 숫자: {i-1}, 누적합: {su}')

print()





print()
#7) 구구단을 출력하되 결과가 30을 넘으면 해당 단 중단하고 다음 단으로 이동
i=2; j=1
while i <10:
    if i*j <= 30:
        print(f'{i}X{j}={j*i}')
    j += 1
    if j==10:
        j=1
        i += 1

#해설
dan = 2
while dan <= 9:
    i = 1
    while i <=9:
        result = dan*i
        if result >30:
            break
        print(dan, "*", i, "=", result)
        i+=1
    print()
    dan +=1

#8) 1 ~ 1000 사이의 소수(1보다 크며 1과 자신의 수 이외에는 나눌 수 없는 수)와 그 갯수를 출력(힌트: 이 문제는 반복이 두 단계다. 2부터 1000까지 하나씩 검사한다. 각 숫자마다 소수인지 확인한다.그래서 while 안에 while 구조가 필요하다.)
#해설
num = 2
count = 0
while num <= 1000:
    i=2
    is_prime = True #소수 저장 변수
    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i+=1
    if is_prime:
        print(num, end=' ')
        count += 1
    num +=1
print('\ncount: ', count)   



print()
#continue 연습 문제
#1) 1부터 50까지의 숫자 중 3의 배수는 건너뛰고 나머지 수만 출력하라
i=1
while i<=50:
    if i%3==0: 
        i+=1
    else: 
        print(i)
        i+=1

print()
#해설
while i <= 50:
    if i%3==0: 
        i+=1
        continue
    print(i, end=' ')
    i+=1

print()
#2) 1부터 100까지 출력하되 4의 배수, 6의 배수는 건너뛴다. 그 외의 수 중 5의 배수만 출력하고 그들의 합도 출력하라
i=1
while i<=100:
    i+=1
    if i%4==0: continue
    elif i%6==0: continue
    elif i%5==0:
        print(i)
        continue


#해설
i=1
total=0
while i <= 100:
    if i%4==0 or i%6==0 or i%5!=0:
        i+=1
        continue
    print(i)
    total += i
    i += 1
print('total: ', total)

#함수처리 --------------
#연습문제1) 리스트를 통해 직원 자료를 입력받아 가공 후 출력하기
# 연습문제1) 리스트를 통해 직원 자료를 입력받아 가공 후 출력하기

# 입력 함수 : [사번, 이름, 기본급, 입사년도]
def inputfunc():
    datas = [
        [1, '강나루', 1500000, 2010],
        [2, '이바다', 2200000, 2018],
        [3, '박하늘', 3200000, 2005]
    ]
    return datas


# 처리 함수 : 급여 계산 및 출력
def processfunc(datas):
    print('\n출력 결과:')
    print('사번  이름   기본급   근무년수   근속수당   공제액   수령액')
    print('-' * 60)

    for emp in datas:
        sabun, name, pay, year = emp
        work_year = 2026 - year

        # 근속수당 계산
        if 0 <= work_year <= 3:
            bonus = 150000
        elif 4 <= work_year <= 8:
            bonus = 450000
        else:
            bonus = 1000000

        wage = pay + bonus

        # 공제율 계산
        if wage < 2000000:
            tax_rate = 0.15
        elif wage < 3000000:
            tax_rate = 0.3
        else:
            tax_rate = 0.5

        tax = int(wage * tax_rate)
        real_pay = wage - tax

        print(f'{sabun:<4} {name:<6} {pay:<8} {work_year:<6} {bonus:<8} {tax:<8} {real_pay}')

    print('-' * 60)
    print(f'처리 건수: {len(datas)}건')


# 실행부
processfunc(inputfunc())

#연습문제2) 리스트를 통해 상품 자료를 입력받아 가공 후 출력하기
#split(): 문자열을 특정 기준(구분자)으로 나누어 리스트로 만들어 주는 함수
def inputfunc():
    datas = [
        "새우깡,15",
        "감자깡,20",
        "양파깡,10",
        "새우깡,30",
        "감자깡,25",
        "양파깡,40",
        "새우깡,40",
        "감자깡,10",
        "양파깡,35",
        "새우깡,50",
        "감자깡,60",
        "양파깡,20",
    ]
    return datas

def processfunc(datas):
    price_table = {
        "새우깡": 450,
        "감자깡": 300,
        "양파깡": 350
    }

    # 소계용 누적 변수
    subtotal_qty = {"새우깡": 0, "감자깡": 0, "양파깡": 0}
    subtotal_amt = {"새우깡": 0, "감자깡": 0, "양파깡": 0}

    total_qty = 0
    total_amt = 0

    # 헤더 출력
    print("상품명   수량   단가   금액")
    print("-" * 35)

    # 데이터 처리
    for data in datas:
        name, qty = data.split(",")   # 문자열 나누기
        qty = int(qty)
        price = price_table[name] #딕셔너리에서 key가 "새우깡"인 값을 찾는 것. # 문자열 key
        amount = qty * price

        # 한 줄 출력
        print(f"{name:<6} {qty:>4} {price:>6} {amount:>7}")

        # 소계 누적
        subtotal_qty[name] += qty
        subtotal_amt[name] += amount

        # 총계 누적
        total_qty += qty
        total_amt += amount

    # 소계 출력
    print("\n소계")
    for name in price_table:
        print(f"{name} : {subtotal_qty[name]}건   소계액 : {subtotal_amt[name]}원")

    # 총계 출력
    print("총계")
    print(f"총 건수 : {total_qty}")
    print(f"총 액  : {total_amt}원")


# 실행
datas = inputfunc()
processfunc(datas)
