kor = 100 # 모듈의 전역변수

def abc(): #function
    eng = 0 #함수 내의 지역변수 
    print('모듈의 멤버 함수')

class My:
    kor = 80 #My 멤버 변수(필드)
    def abc(self):
        print('My 멤버 메소드')
    
    def show(self): #method
        #kor = 77 #지역변수 #주석처리하면 100. 지역변수 > 모듈 전역 변수 > class 멤버 변수 (찾기 우선순위)
        print(kor) #77
        print(self.kor) #80
        self.abc() #My 멤버 메소드. class로 감
        abc() #모듈의 멤버 함수. self 안붙이면 모듈 함수로 감

my = My()
my.show() #100
print('----------')
print(My.kor)
tom=My()
print(tom.kor)
tom.kor = 88


print(tom.kor)

oscar = My()
print(oscar.kor)