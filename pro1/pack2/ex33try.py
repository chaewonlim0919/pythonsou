# 예외처리 : 파일, 네트워크,DB작업, 실행에러 등의 에러 대처

def divide(a,b):
    return a/b

print('이런 저런 작업 진행')
# c = divide(5,2)
# c = divide(5,0)
# print(c)


# 에러가 날 것 같을 때 
try:
    #실행문(예외 발생 가능 구문)
    c = divide(5,2)
    # c = divide(5,0)
    print(c)

    aa = [1,2]
    print(aa[0])
    # print(aa[3])   # IndexError: list index out of range, 인덱스 에러 처리 함수는 따로 있음

    open("c:/work/abc.txt")
except ZeroDivisionError:  # 예외 종류 관련 클래스 
    print('두번째 값은 0을 주면 안돼요')  # 예외 발생

except IndexError:
    print('참조 범위 오류')

except Exception as e:  # 모든 에러들을 Exception으로 모두 처리할 수 있음. 근데 만약 특정 에러들만 처리하고 싶다면 위처럼 해야함
    print('에러: ', e)

finally:
    print('에러 유무에 상관없이 반드시 수행됨.')
print('end')
print()