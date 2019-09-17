import Python3.dataLoader.dataloader as dl

#%% 데이터 불러오기 예제
data = dl.dataLoad(1)
# help(dl.dataLoad) # 함수 정보 확인
# print(data)
#%%

#region 1초 간격의 시간 데이터 만들기
time = dl.timeset(data)
# print(time)
#endregion

# 데이터 자르기
sp_list = dl.datasplit(data.values, 8)
print(sp_list)
#

