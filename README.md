[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

![badge](https://img.shields.io/github/commit-activity/w/Kaintels/rubyPy-study?style=flat) ![badge](https://img.shields.io/badge/launch-binder-579aca.svg?style=flat)




# Python Study for MFS

기본적인 파이썬 문법 및 머신러닝 실습자료

## Getting Started

*Python*



#### 2019.08.25 기준 [머신러닝 실습](#머신러닝-실습)은 주피터 노트북에서 실시간 실습이 가능합니다. 

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

(e.g. : 가상환경 1에는 tensorflow, 가상환경 2에는 pytorch 설치를 해야됩니다. 가상환경 1에 두 딥러닝 라이브러리를 설치하면 오류가 날 수있습니다.)

가상환경 설치 및 관리는 다음 사이트로 가시면 확인하실 수 있습니다. [바로가기](https://niceman.tistory.com/85)

라이브러리 설치는 아래와 같이 설치를 해야합니다.

```
pip install lib
```
또는
```
conda install lib
```

**2020.03.14 기준** ``environment-torch.yml``**을 이용하여 pytorch, hpbandster를 포함한 딥러닝 및 최적화 패키지가 포함된 가상환경을 설치 할 수 있습니다.**



**Python 3.5**

```
conda env create -n 설치이름 --file environment-torch.yml # 가상환경 직접 이름 설정
```
또는
```
conda env create -f environment-torch.yml # default, torchs로 이름 설정
```

**Python 3.7**

```
conda env create -f environment-torch-37.yml # default, torchs로 이름 설정
```

## Python

#### 기본 문법

* [기본 문법 1](https://github.com/Kaintels/rubyPy-study/tree/master/Python3/grammer)

#### 통계학

- [상관관계분석](https://github.com/Kaintels/rubyPy-study/tree/master/Python3/statistics)	

#### 영상처리

- [라인 감지](https://github.com/Kaintels/rubyPy-study/tree/master/Python3/opencv)

#### 딥러닝 라이브러리 파이토치 실습

- [기본 문법 1](https://github.com/Kaintels/rubyPy-study/tree/master/Python3/pytorch)

#### 머신러닝 실습

*선형회귀 기반 혈압 추정*

- [주피터 노트북](https://nbviewer.jupyter.org/github/Kaintels/rubyPy-study/blob/master/Python3/BP_estimation/Py_practice.ipynb)
- [실습해보기](https://mybinder.org/v2/gh/Kaintels/rubyPy-study/master?filepath=Python3/BP_estimation/Py_practice.ipynb)

*Naïve Bayes Classifier 실습*

- 작성중

#### 딥러닝 기반 숫자 분류

- 작성중

#### 강화학습 기반

- 

## Ruby



## Good thing to see together

#### Linear Algebra; Principal Component Analysis(PCA), Linear Discriminant Analysis(LDA)

- [PCA](https://www.youtube.com/watch?v=FhQm2Tc8Kic)
- [PCA 파이썬 구현](https://www.youtube.com/watch?v=DUJ2vwjRQag)
- [LDA](https://www.youtube.com/watch?v=p8Fqt2Qxqro)

#### Basic Deep Learning; Convolutional Neural Network(CNN), Recurrent Neural Network(RNN)

- [CS231n](http://cs231n.stanford.edu/)
- [CS231n 한글 강좌](https://www.youtube.com/watch?v=3QjGtOlIiVI&list=PL1Kb3QTCLIVtyOuMgyVgT-OeW0PYXl3j5)
- [문일철 교수님 강의](http://seslab.kaist.ac.kr/xe2/index.php?mid=page_GBex27)

#### Advanced Deep Learning; AutoEncoder, Variational AutoEncoder(VAE), Generative Adversarial Network(GAN)

- [AE](https://www.youtube.com/watch?v=YxtzQbe2UaE)
- [VAE](https://www.youtube.com/watch?v=0ywpBuWXXWo)
- [Introduction to GANs, NIPS 2016, Ian Goodfellow, OpenAI](https://www.youtube.com/watch?v=9JpdAg6uMXs)
- [GAN 한글 강좌](https://www.youtube.com/watch?v=52r9F05wAl4)

#### Reinforcement Learning;

- [David Sliver's Online lecture](https://www.youtube.com/watch?v=2pWv7GOvuf0&list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ)
- [David Sliver's Silde](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html)
- [팡요랩 강화학습 기초 이론](https://www.youtube.com/watch?v=wYgyiCEkwC8&list=PLpRS2w0xWHTcTZyyX8LMmtbcMXpd3s4TU)
- [Naver D2](https://www.youtube.com/watch?v=soZXAH3leeQ&list=PLsFtzQAC8dDetav3jSCKB_MXwvUn7yfJS)
- [모두의 연구소](http://www.modulabs.co.kr/RL_library/2136)
- [강화학습 Gitbook](https://dnddnjs.gitbooks.io/rl/content/reinforcement_learning.html)

#### Simultaneous Localization and Mapping (SLAM)

- [Cyrill Stachniss's 12/13 lecture](https://www.youtube.com/watch?v=V9qQc5X7O0k&list=PLgnQpQtFTOGQECnBvZSV61oxTrkPut-nc)

- [Cyrill Stachniss's 13/14 lecture](https://www.youtube.com/watch?v=U6vr3iNrwRA&list=PLgnQpQtFTOGQrZ4O5QzbIHgl3b1JHimN_)

#### Hidden Markov Model(HMM), Expectation-Maximization(EM) Algorithms, Kalman Filter

- [HMM 기초](https://www.youtube.com/watch?v=MoH4lcbBakA)

- [EM 기초](https://www.youtube.com/watch?v=U99A8myCwfE)

- [Kalman Filter 기초](https://www.youtube.com/watch?v=Ist-Cs0ZxPc)

#### Deep Learning Paper Review

- [Paper Review 1](https://www.youtube.com/watch?v=L3hz57whyNw&list=PL0oFI08O71gKjGhaWctTPvvM7_cVzsAtK)

- [Paper Review 2](https://www.youtube.com/watch?v=myBzJ0cnHBk)

- [Paper Review 3](https://www.youtube.com/watch?v=Pu_oggjuNxc)

- [딥러닝 추천 논문](http://deeplearningstudy.github.io/doc_deeplearning_paper.html)

- [논문 코드 구현 1](https://paperswithcode.com/)

- [논문 코드 구현 2 (한승우 본인)](https://github.com/Kaintels/paper-review)
