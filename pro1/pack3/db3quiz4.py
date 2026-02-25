# 문4)직원별 관리 고객 수 출력 (관리 고객이 없으면 출력에서 제외)

# 직원번호 직원명 관리 고객 수
# 1 홍길동 3
# 2 한송이 1

import MySQLdb
import pickle

with open('mydb.dat', mode='rb') as obj:
    config= pickle.load(obj)

def chulbal():
    try:
        conn = MySQLdb.connect(**config)  # dict 자료
        cursor = conn.cursor()
        sql = '''
            select jikwonno as 직원번호, jikwonname as 직원명, count(gogekno) as '관리 고객 수' 
            from jikwon right outer join gogek on jikwonno = gogekdamsano
            group by jikwonno
            '''
        print(sql)
        cursor.execute(sql)                 
        datas = cursor.fetchall()

        for r in datas:
            print(r[0],r[1],r[2])

    except Exception as e:
        print('err: ', e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    chulbal()

