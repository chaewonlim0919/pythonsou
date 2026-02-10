#기본 자료형 : int, float, bool, complex
#묶음 자료형 : str, list, set, dict

#1) str : 문자열 묶음 자료형, 순서O, 수정X
s = 'sequence'
print(s, id(s)) #id는 문자의 가장 앞 문자('s')의 주소를 기억하고 있음
print('길이 : ', len(s)) #8, 8글자수임
print(s[0], s[2]) #s q, 0번째, 2번째 문자 출력 like 배열
print('길이 : ', s.find('e'), s.find('e', 3), s.rfind('e')) #문자열 관련함수 

#인덱싱 / 슬라이싱
print(s[5]) #인덱싱 - 변수명[순서], index는 0부터 출발 / 결과: n
print(s[2:5]) #슬라이싱 - 변수[이상:미만:step] / 결과: que 
print(s[:], ' ', s[0:len(s)], s[::1]) #문자열 전체 출력 
print(s[0:7:2]) # 결과 sqec
print(s[-1], ' ', s[-4:-1:1]) #-1번째는 뒤에서부터이고 가장 뒤. 즉 e  enc
print(s, id(s))
s= 'sequenc' #수정X, 변경
print(s, id(s))
s= 'bequence'
print(s, id(s))
#stirng 타입은 겉으로는 수정된 것처럼 보이나, 수정 불가능함. sequence 140730959034888. sequenc 2565700652032, bequence 2565700716976

print('-------------'*10)

# 2) List : 다양한 종류의 자료 묶음형, 순서O, 수정O, 중복O
a = [1, 2, 3]
print(a, a[0], a[0:2]) #[1, 2, 3] 1 [1, 2]
b = [10, a, 10, 20.5, True, '문자열']
print(b) #[10, [1, 2, 3], 10, 20.5, True, '문자열']. 즉 중복 허용 가능 
print(b, ' ', b[1], ' ', b[1][0]) #b[1][0]은 [1, 2, 3]중 [0] 즉 1임
#각각이 주소를 가지고 있음, 근데 id(b)는 첫번째 주소를 따라감, but 메모리 많이 차지

print()
family = ['엄마', '아빠', '나', '여동생']
print(id(family))
family.append('남동생') #append는 추가
print(id(family))
family.remove('나') #삭제
family.insert(0, '할머니') #삽입
family.extend(['삼촌', '고모', '조카']) #추가
family += ['이모'] #추가 
print(family)
print(family.index('아빠')) #index는 순서를 알려줌
print('엄마' in family, '나' in family) #True False

family.remove('아빠') # 값에 의한 삭제
del family[2] #순서에 의한 삭제 
print(family)

print()
kbs  = ['123', '34', '234']
kbs.sort() #문자열 정렬 
print(kbs) #['123', '234', '34']

mbc  = [123, 34, 234]
mbc.sort() #숫자 정렬(ascending sot, 오름)
print(mbc) #[34, 123, 234]
mbc.sort(reverse=True) #숫자 정렬(descending sort, 내림)
print(mbc) #[234, 123, 34]

sbs = [123, 34, 234]
ytn = sorted(sbs)
print(sbs) #[123, 34, 234]
print(ytn) #[34, 123, 234]
#sort 와 sorted  차이 
#sort: 원본 변경
#sorted: 원본 유지, 정렬된 새 리스트 반환

print()
name = ['tom', 'james', 'oscar']
name2 = name
print(name, id(name)) #['tom', 'james', 'oscar'] 2672018290048
print(name2, id(name2)) #['tom', 'james', 'oscar'] 2672018290048

import copy
name3 = copy.deepcopy(name)  #name3는 새로운 객체에 복사하는것임. 따라서 주소가 다름
print(name3, id(name3)) #['tom', 'james', 'oscar'] 2672018289728

name[0] = '길동'
print(name) #['길동', 'james', 'oscar']
print(name2) #['길동', 'james', 'oscar']
print(name3) #['tom', 'james', 'oscar']

print('-------------'*10)
# 3) tuple: 리스트와 유사. 읽기 전용 - 수정X
t = (1,2,3,4) #tuple임
t = 1, 2, 3, 4 # 위와 동일 
print(t, type(t))
k= (1) #tuple 아닌 int임
k= (1, ) #tuple임
print(k, type(k)) 
print(t[0],' ', t[0:2])
#t[0] = 77 #TypeError: 'tuple' object does not support item assignment. 즉 수정 불가하며 read only임

imsi = list(t)
imsi[0] = 77 # List로 변경하여 값을 변경 후 
t = tuple(imsi) #튜플로 돌아옴 . 튜플이 탐색이 빠름 
print(t)

# 4)  set: 수정X, 중복X , 수정O
ss = {1,2,1,3}
print(ss) # 중복 제거 
ss2 = {3,4} 
print(ss.union(ss2)) # 합집합
print(ss.intersection(ss2)) # 교집합
print(ss-ss2, ss | ss2, ss & ss2) #차, 합, 교집합
#print(ss[0]) #TypeError: 'set' object is not subscriptable. 순서가 없으므로 인덱스, 슬라이싱 불가 
ss.update({6,7})
print(ss) #수정 됨
ss.discard(7) # 값 삭제
ss.discard(7) # 값 삭제, discard는 있으면 지우고 없으면 skip.
ss.remove(6) # 값 삭제 
#ss.remove(6) # 값 삭제 , remove는 있으면 지우고 없으면 error. KeyError: 6
print(ss)

li = ['aa', 'aa', 'bb', 'cc', 'aa']
print(li)
imsi = set(li)
li = list(imsi)
print(li) #리스트에서 중복 제거하고 싶을 시, set type으로 변경 후 다시 list로 변경 

print('-------------'*10)
# 5) dict : 사전 자료형 {'키':값} 형태
# 방법1
mydic = dict(k1 = 1, k2= 'ok', k3=123.4)
print(mydic, type(mydic)) #{'k1': 1, 'k2': 'ok', 'k3': 123.4} <class 'dict'>
#방법2
dic = {'파이썬':'뱀', '자바':'커피', '인사':'안녕'}
print(dic)
print(len(dic))
print(dic['자바']) #커피. 즉 value 값을 key로 찾는것.
ff = dic.get('자바')
print(ff)

#print(dic['커피']) #KeyError: '커피'. 즉 value로 key를 찾을 수 없음
#print(dic[0]) #인덱싱, 슬라이싱 X
dic['금요일'] = '와우' #추가 (순서X) 
print(dic) #{'파이썬': '뱀', '자바': '커피', '인사': '안녕', '금요일': '와우'}. 
del dic['인사'] #삭제
print(dic) #{'파이썬': '뱀', '자바': '커피', '금요일': '와우'}
print(dic.keys()) #dict_keys(['파이썬', '자바', '금요일'])
print(dic.values()) #dict_values(['뱀', '커피', '와우'])