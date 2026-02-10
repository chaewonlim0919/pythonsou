# 참도, 왜도가 큰 (편차가 큰 데이터 ...) 데이터를 로그변환하면 
# 분포 개선, 범위 차이 축소 등으로 인해 모델을 안정적으로 수행 가능 

import math

class LogTrans:
    def __init__(self, offset:float=1.0):
        self.offset = offset

    def transform(self, x_list:list[float]): #로그 변환
        return [math.log(x + self.offset) for x in x_list]

    def inverse_trans(self, x_list:list[float]): #역 변환
        return [math.exp(x_log) - self.offset for x_log in x_list]
        

        