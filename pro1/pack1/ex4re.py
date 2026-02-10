##정규표현식 p374
import re

ss = "1234 abc 가나다abcABC_123555집에가나요_6'Python is fun'"
print(ss)
print(re.findall(r'123',ss)) #정규표현식 쓸 때 r을 선행하라
print(re.findall(r'가나',ss))
print(re.findall(r'[0-9]',ss)) #['1', '2', '3', '4', '1', '2', '3', '5', '5', '5', '6']
print(re.findall(r'[0-9]+',ss)) #['1234', '123555', '6']
print(re.findall(r'[0-9]{2}',ss)) #['12', '34', '12', '35', '55']
print(re.findall(r'[0-9]{2,3}',ss)) #['123', '123', '555']
print(re.findall(r'[a-zA-Z]+',ss)) #['abc', 'abcABC', 'Python', 'is', 'fun']
print(re.findall(r'[가-힣]+',ss)) #['가나다', '집에가나요']
print(re.findall(r'\d+',ss)) #['1234', '123555', '6']
print(re.findall(r'\D+',ss)) #[' abc 가나다abcABC_', '집에가나요_', "'Python is fun'"]