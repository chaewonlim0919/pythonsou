# 문2) 직원번호와 직원명을 입력(로그인)하여 성공하면 아래의 내용 출력

# 직원번호 입력 : _______
# 직원명 입력 : _______
# 직원번호 직원명 부서명 부서전화 직급 성별
# 1 홍길동 총무부 111-1111 이사 남
# ...

# import MySQLdb

# config = {
#     'host' : '127.0.0.1',
#     'user' : 'root',
#     'password' : '123',
#     'database' : 'test',
#     'port' : 3306,
#     'charset' : 'utf8'
# }

# def chulbal():
#     try:
#         conn = MySQLdb.connect(**config)  # dict 자료
#         cursor = conn.cursor()

#         jikbun = input('직원번호 입력: ')
#         jikmyeong = input('직원명 입력: ')
#         # sql = """
#         #     select jikwonno as 직원번호, jikwonname as 직원명, busername as 부서명,  busertel as 부서전화, jikwonjik as 직급, jikwongen as 성별
#         #     from jikwon 
#         #     inner join buser on busernum=buserno
#         #     where jikwonno = {0} and jikwonname = '{1}' 
#         # """.format(jikbun, jikmyeong)
#         # print(sql)
#         # cursor.execute(sql) 
#         # datas = cursor.fetchall()
#         # print(datas)

#         sql = """
#             select jikwonno as 직원번호, jikwonname as 직원명, busername as 부서명,  busertel as 부서전화, jikwonjik as 직급, jikwongen as 성별
#             from jikwon 
#             inner join buser on busernum=buserno
#             where jikwonno = %s and jikwonname = %s 
#         """
#         cursor.execute(sql, (jikbun, jikmyeong))
#         datas = cursor.fetchall()
        
#         if len(datas) == 0:
#             print("해당 직원은 없어요")
#             return    # sys.exit(0)
        
#         for jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen in datas:
#             print(jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen)

#     except Exception as e:
#         print('err: ', e)
#         conn.rollback()
#     finally:
#         cursor.close()
#         conn.close()


# if __name__ == "__main__":
#     chulbal()

import MySQLdb
import pickle

'''
config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '123',
    'database' : 'test',
    'port' : 3306,
    'charset' : 'utf8'
}
'''

with open('mydb.dat', mode='rb') as obj:
    config= pickle.load(obj)

def chulbal():
    try:
        conn = MySQLdb.connect(**config)  # dict 자료
        cursor = conn.cursor()

        jikbun = input('직원번호 입력: ')
        jikmyeong = input('직원명 입력: ')

        sql = """
            select jikwonno as 직원번호, jikwonname as 직원명, busername as 부서명,  busertel as 부서전화, jikwonjik as 직급, jikwongen as 성별
            from jikwon 
            inner join buser on busernum=buserno
            where jikwonno = %s and jikwonname = %s 
        """
        cursor.execute(sql, (jikbun, jikmyeong))
        datas = cursor.fetchall()
        
        if len(datas) == 0:
            print("해당 직원은 없어요")
            return    # sys.exit(0)
        
        for jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen in datas:
            print(jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen)

    except Exception as e:
        print('err: ', e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    chulbal()



# 문2-1) 직원번호와 직원명을 입력(로그인)하여 성공하면 아래의 내용 출력
# 해당 직원이 근무하는 부서 내의 직원 전부를 직급별 오름차순우로 출력. 직급이 같으면 이름별 오름차순한다.

# 직원번호 입력 : _______
# 직원명 입력 : _______
# 직원번호 직원명 부서명 부서전화 직급 성별
# 1 홍길동 총무부 111-1111 이사 남
# ...
# 직원 수 :

# 이어서 로그인한 해당 직원이 관리하는 고객 자료도 출력한다.
# 고객번호 고객명 고객전화 나이
# 1 사오정 555-5555 34
# 관리 고객 수 :

import MySQLdb

config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '123',
    'database' : 'test',
    'port' : 3306,
    'charset' : 'utf8'
}

def chulbal():
    try:
        conn = MySQLdb.connect(**config)  # dict 자료
        cursor = conn.cursor()

        jikbun = input('직원번호 입력: ')
        jikmyeong = input('직원명 입력: ')

        sql1 = """
            select jikwonno as 직원번호, jikwonname as 직원명, busername as 부서명,  busertel as 부서전화, jikwonjik as 직급, jikwongen as 성별
            from jikwon 
            inner join buser on busernum=buserno
            where busername = 
            (select busername from jikwon inner join buser on busernum=buserno where jikwonno = %s and jikwonname = %s)
        """            
        cursor.execute(sql1, (jikbun, jikmyeong))                 
        datas1 = cursor.fetchall()
        
        sql2 = '''
            select gogekno as 고객번호, gogekname as 고객명, gogektel as  고객전화,  2026- (1900 + SUBSTR(gogekjumin, 1, 2)) as 나이
            from jikwon inner join gogek on jikwonno = gogekdamsano
            where jikwonno = {0}
        '''.format(jikbun)

        cursor.execute(sql2)                 
        datas2 = cursor.fetchall()

        if len(datas1) == 0:
            print("해당 직원은 없어요")
            return    # sys.exit(0)
        if len(datas2) == 0:
            print("관리하는 고객이 없어요")
            return    # sys.exit(0)

        for jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen in datas1:
            print(jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen)
        print('직원 수: ', str(len(datas1)))
        
        print()
        for a,b,c,d in datas2:
            print(a,b,c,d)
        print('관리 고객 수: ', str(len(datas2)))

    except Exception as e:
        print('err: ', e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    chulbal()


# 아래와 비교
import MySQLdb

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}

def chulbal():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()

        jikbun = int(input('직원번호 입력: '))
        jikmyeong = input('직원명 입력: ')

        # 1️⃣ 로그인 체크 + 부서 직원 조회
        sql1 = """
            select j.jikwonno, j.jikwonname, b.busername, b.busertel,
                   j.jikwonjik, j.jikwongen
            from jikwon j
            join buser b on j.busernum = b.buserno
            where j.busernum =
                  (select busernum
                   from jikwon
                   where jikwonno = %s and jikwonname = %s)
            order by j.jikwonjik asc, j.jikwonname asc
        """

        cursor.execute(sql1, (jikbun, jikmyeong))
        datas1 = cursor.fetchall()

        if not datas1:
            print("해당 직원은 없어요")
            return

        print("📌 부서 직원 목록")
        for row in datas1:
            print(*row)

        print("직원 수:", len(datas1))
        print()

        # 2️⃣ 관리 고객 조회
        sql2 = """
            select gogekno,
                   gogekname,
                   gogektel,
                   case substr(gogekjumin,8,1)
                        when '1' then 2026 - (1900 + substr(gogekjumin,1,2))
                        when '2' then 2026 - (1900 + substr(gogekjumin,1,2))
                        when '3' then 2026 - (2000 + substr(gogekjumin,1,2))
                        when '4' then 2026 - (2000 + substr(gogekjumin,1,2))
                   end as 나이
            from gogek
            where gogekdamsano = %s
        """

        cursor.execute(sql2, (jikbun,))
        datas2 = cursor.fetchall()

        print("📌 관리 고객 목록")

        if not datas2:
            print("관리 고객이 없습니다")
        else:
            for row in datas2:
                print(*row)
            print("관리 고객 수:", len(datas2))

    except Exception as e:
        print('err:', e)
        conn.rollback()

    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    chulbal()