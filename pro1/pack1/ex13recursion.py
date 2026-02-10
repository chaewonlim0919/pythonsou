#메모리 사용 측면에서, for/while문은 적고 (스택 증가 없음), 재귀는 많아서 (콜 스택 사용) 오버 헤드 존재한다.
# 재귀는 수학적/논리적 표현이 직관적이며 츠리, 분할 정복이 가능하다는 장점이 있다. 
#재귀함수 : 함수가 자기 자신을 호출 - 반복처리 (호출이 많을 때 재귀 쓰면 안됨.)
def countDown(n):
    if n == 0:
        print('완료')
    else:
        print(n, end=' ')
        countDown(n-1) #재귀. 선 호출 후 연산
countDown(5)

print('--1부터 n까지 합---------')
def totFunc(n):
    if n == 0:
        print('탈출')
        return 0
    return n + totFunc(n-1) #재귀 . 계산 결과를 “다음 계산에 쓰려면” return이 필수
result = totFunc(5)
print('result: ', result)


print('--5 factorial ---------')
def factFunc(n):
    if n==0:
        print('탈출')
        return 1
    return n*factFunc(n-1)
result = factFunc(5)
print('result', result)


#  재귀문제 :  리스트 자료 v = [7, 9, 15, 43, 32, 21] 에서 최대값 구하기 - 재귀 호출 사용 
v = [7, 9, 15, 43, 32, 21]
def find_max(v,n):
    if n==1:
        return v[0] #리스트의 첫 번째 값을 반환하고 재귀 종료
    prev_max = find_max(v, n-1) #앞의 n-1개 원소 중 최대값을 구함. 이 호출이 끝나면 아래 코드로 내려감
    if v[n-1]>prev_max: #현재 단계에서 마지막 원소 v[n-1]과 이전 단계에서 구한 최대값 비교
        return v[n-1] #마지막 값이 더 크면 그 값을 최대값으로 반환
    else:
        return prev_max
v = [7, 9, 15, 43, 32, 21]
print(find_max(v,len(v)))