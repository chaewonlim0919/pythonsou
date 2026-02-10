# 매개변수 유형
#위치 매개변수 : 인수와 순서대로 대응
#기본값 매개변수 : 매개변수에 입력값이 없으면 기본값 사용
#키워드 매개변수 : 실인수와 가인수 간 동일 이름으로 대응
#가변 매개변수 : 인수의 갯수가 동적인 경우

def showGugu(start, end=5): #가인수
    for dan in range(start, end +1, 1):
        print(str(dan) + '단 출력')
        for i in range(1,10):
            print(str(dan) + "*" + \
                  str(i) + "=" + str(dan*i), end = ' ')
        print()
showGugu(2,3) #실인수
print()
showGugu(2)
print()
showGugu(start=7, end=9)
print()
showGugu(end=9, start=7) #키워드 매개변수로, 동일한 이름 찾아감
#showGugu(start=7, 9) #SyntaxError: positional argument follows keyword argument

print()
print('가변 매개변수 -------')
def func1(*ar): #* : 여러 개의 인자를 tuple로 묶어서 받겠다
    print(ar)
func1('김밥', '비빔밥', '볶음밥') #('김밥', '비빔밥', '볶음밥')
func1('김밥', '비빔밥', '볶음밥', '공기밥') #('김밥', '비빔밥', '볶음밥', '공기밥')
func1('김밥') #('김밥',) 콤마 중요 !! 튜플 형태로 전달됨!!

print()
def func2(a,*ar):
    print(a)
    print(ar)
func2('김밥', '비빔밥') 
func2('김밥', '비빔밥','볶음밥', '공기밥')

'''
print()
def func3(w,h,*other):
    print(f'몸무게: {w}, 키: {h}')
    print(f'기타: {other}')
func3(80, 100, irum='신기루', nai=23) #dict 타입
#func3(80, 100, {'irum':'신기루','nai':23}) #dict 타입으로 제시하면 Error. 
'''

print()
def func4(a,b,*c,**d): #*c: 남은 위치 인자들을 튜플로 / **d: 남은 키워드 인자들을 딕셔너리로
    print(a,b)  
    print(c) 
    print(d) 
print()
func4(1,2) 
print()
func4(1,2,3,4,5)
print()
func4(1,2,3,4,5,kbs=9, mbc=11)

print()
#type hint : 함수의 인자와 반환값에 type을 적어 가독성 향상
def typeFunc(num:int,data:list[str]): 
#def typeFunc(num,data): #위와 동일
    print(num)
    print(data)
    result = {} #아직 dict인지 set인지 모름
    for idx, item in enumerate(data, start=1): #(1,'일'),(2,'이'),(3,'삼')/ 튜플 생성 후 idx, item 매치, 인덱스 + 값”을 한 쌍으로 같이 꺼내주는 함수
        print(f'idx:{idx}, item:{item}')
        result[item] = idx # dict 결정
    return result

rdata = typeFunc(1,['일','이','삼'])
print(rdata)

rdata = typeFunc("한개", [10,20,30])
print(rdata)