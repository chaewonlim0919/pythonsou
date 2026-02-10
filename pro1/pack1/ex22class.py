#클래스는 새로운 타입을 만들어 자원을 공유 가능 

# class Singer:
#     title_song = "빛나라 대한민국"

#     def sing(self):
#         msg = "노래는"
#         print(msg, self.title_song)
#import ex22singer
from ex22singer import Singer
#bts = ex22singer.Singer() #생성자 호출해 객체를 생성 후 주소를 bts에 치환
bts = Singer()
bts.sing() #노래는 빛나라 대한민국
print(type(bts)) #<class '__main__.SingerType'>
bts.title_song = 'Permission to Dance'
bts.sing()
bts.co = '빅히트 엔터테인먼트' #co는 bts만 가지고 있음
print('소속사: ', bts.co)
print()

ive = Singer()
ive.sing()
print(type(ive))
#print('소속사: ', ive.co) #Error

Singer.title_song = "아 대한민국" #멤버변수를 바꿈
bts.sing() #노래는 Permission to Dance 
ive.sing() #노래는 아 대한민국 

niceGroup = ive #치환
niceGroup.sing() 