#필요 패키지(KMeans, matplotlib, preprocessing)
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
#파일 관련
import pandas as pd
import csv

#df = pd.read_csv("student_health_3.csv", encoding = "cp949")

#1~3학년을 저학년 (Class 1), 4~6학년으로 고학년(Class 2)로 변경
f = open('student_health_3.csv','r')
rdr = csv.reader(f)
 
lines = []
for line in rdr:
       if line[11] == '1' or line[11] == '2' or line[11] == '3':
              line[11] = "Class 1"
       if line[11] == '4' or line[11] == '5' or line[11] == '6':
              line [11] = "Class 2"
       lines.append(line)
f = open('student_health_3_change.csv','w',newline='')
wr = csv.writer(f)
wr.writerows(lines)

data = pd.read_csv('student_health_3_change.csv', encoding ='cp949')
data.head()

# 원본 데이터를 복사해서 전처리하기 (원본 데이터를 가지고 바로 전처리하지 않는다)
processed_data = data.copy()

#데이터 전처리(정규화를 위한 작업)
scaler = preprocessing.MinMaxScaler()

processed_data[['수축기', '이완기', '키', '몸무게']]=\
                       scaler.fit_transform(processed_data[['수축기', '이완기', '키', '몸무게']])

#화면 생성(figure) - 2차원 (참고:https://planharry.tistory.com/43)
plt.figure(figsize = (10, 6))

#K=4로 클러스터링
estimator = KMeans(n_clusters=4)

#클러스터링 생성
cluster_ids = estimator.fit_predict(processed_data[['수축기', '이완기', '키', '몸무게']])

#scatter plot생성
plt.scatter(processed_data['수축기'],processed_data['이완기'],\
           processed_data['키'],processed_data['몸무게'])

#(Customer ID, ItemsBought, ItemsReturned, ZipCode, Product)
#학년과 클러스터 id로 데이터에 범례 달기
for index, c_id,학년,ID in processed_data.itertuples():
       plt.annotate("Clu{} : {}".format(cluster_ids[index], ID),(학년))

#plt.show()로 확
