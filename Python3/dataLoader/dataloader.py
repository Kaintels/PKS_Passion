import pandas as pd
import numpy as np
import math

def datasplit(data, want_split_time):
    """데이터를 원하는 값에 맞춰 자르는 함수

    * 원하는 값을 입력하면
      데이터를 자를 수 있음 (신호 및 이미지 처리에 유용)

    .. note::
      딱 떨어지지 않을 시 마지막 나눈 몫에서 반올림하여 나머지까지 포함하여 자름

    Examples::

      >>> dl.datasplit(data, 5)
    :param data: 사용할 데이터
    :param want_split_time: 원하는 값
    :return: 원하는 값만큼 자른 리스트들
    """
    sp =[]
    for i in range(int(math.ceil(len(data) / want_split_time))):
        v = data[want_split_time*i:want_split_time*(i+1)]
        sp.append(v)
    return sp

def dataLoad(numbersubject):
    '''데이터를 로드하는 함수

    * csv 혹은 주석을 지워
      excel 파일을 불러올 수 있음 (기본 : csv)

    .. note::
      함수 수정 시 str을 지울 경우 데이터가 로드가 안됨,
      정수가 아닌 문자열을 받기 떄문에 문자열 '숫자값'으로 읽어야함

    Examples::

      >>> dl.dataLoad(1)

    :param numbersubject: 데이터 번호
    :return: 불러온 데이터
    '''
    data = pd.read_csv("data"+str(numbersubject)+".csv", low_memory=False)
    # data = pd.read_excel("data"+str(numbersubject)+".xlsx", low_memory=False) # excel file case
    return data

def timeset(data):
    '''1초 간격의 시간 데이터 만드는 함수

    * 데이터의 길이만큼
      1초씩 증가하는 시간 데이터를 만들 수 있음

    .. note::
      파이썬은 0부터 시작하는 언어임을 인지


    Examples::

      >>> dl.timeset(data)

    :param data: 사용할 데이터
    :return: 시간
    '''
    time = []
    for t in range(0, len(data), 1):
        time.append(t)
    return np.array(time)