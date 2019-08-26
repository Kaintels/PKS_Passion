[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![forthebadge made-with-ruby](https://forthebadge.com/images/badges/made-with-ruby.svg)](https://www.ruby-lang.org/) 


![badge](https://img.shields.io/github/commit-activity/w/Kaintels/rubyPy-study?style=flat) ![badge](https://img.shields.io/badge/launch-binder-579aca.svg?style=flat)




# Python 및 Ruby Study

기본적인 파이썬/루비 문법 및 머신러닝 실습자료

## Getting Started

#### 2019.08.25 기준 [머신러닝 기반 혈압 추정](#머신러닝-기반-혈압-추정)은 주피터 노트북에서 실시간 실습이 가능합니다. 머신러닝 기반 실습은 따로 파이썬 설치가 필요 없습니다.

이곳에 있는 자료들을 사용하기 위해서는 파이썬 3.x 버전 이상이 필요합니다.

[Python 홈페이지](https://www.python.org/)에 있는 Python을 사용해도 되나, 되도록이면 가상환경이 가능한 [Anaconda3](https://www.anaconda.com/), 또는 [Miniconda3](https://docs.conda.io/en/latest/miniconda.html) 사용을 권장드립니다.

자료들을 사용하는데 있어서 필요한 라이브러리는 다음과 같습니다.

#### 수치해석

- `numpy` : 수치 및 행렬 계산을 위한 라이브러리
- `scipy` : 수학 및 신호처리 라이브러리
- `pandas` : 데이터 불러오기 및 데이터 처리 라이브러리

#### 그래프

- `matplotlib` : 그래프 도식화 라이브러리
- `seaborn` : 고급 그래프 도식화 라이브러리 (필수x)

#### 머신러닝 및 딥러닝

- `sklearn` : 머신러닝 라이브러리
- `tensorflow` : 구글의 딥러닝 라이브러리
- `keras` : tensorflow의 high-level API
- `pytorch` : 페이스북의 딥러닝 라이브러리

**머신러닝 및 딥러닝 라이브러리는 다른 라이브러리들과 의존성(dependency)을 가지게 되므로, 하나의 가상환경에 하나의 머신 및 딥러닝 라이브러리 설치를 당부드립니다.**

(e.g. : 가상환경 1에는 tensorflow, 가상환경 2에는 pytorch 설치를 해야함. 가상환경 1에 두 딥러닝 라이브러리를 설치하면 오류가 날 수있음)

가상환경 설치 및 관리는 다음 사이트로 가시면 확인하실 수 있습니다. [바로가기](https://niceman.tistory.com/85)

라이브러리 설치는 아래와 같이 설치를 해야합니다.

```
pip install lib
```
또는
```
conda install lib
```

## Python

#### 기본 문법

* [기본 문법 1](https://github.com/Kaintels/rubyPy-study/tree/master/Python3/grammer)

#### 통계학

- [상관관계](https://github.com/Kaintels/rubyPy-study/tree/master/Python3/statistics)	

#### 영상처리

- [라인 감지](https://github.com/Kaintels/rubyPy-study/tree/master/Python3/opencv)

#### 딥러닝 라이브러리 파이토치 실습

- [기본 문법 1](https://github.com/Kaintels/rubyPy-study/tree/master/Python3/pytorch)

#### 머신러닝 기반 혈압 추정

##### 선형회귀 기반 

- [주피터 노트북](https://nbviewer.jupyter.org/github/Kaintels/rubyPy-study/blob/master/Python3/BP_estimation/Py_practice.ipynb)
- [실습해보기](https://mybinder.org/v2/gh/Kaintels/rubyPy-study/master?filepath=Python3/BP_estimation/Py_practice.ipynb)

#### 딥러닝 기반 혈압 추정

- 작성중

## Ruby
