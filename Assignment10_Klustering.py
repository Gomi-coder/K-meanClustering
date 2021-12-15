# 모듈 호출
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import random as rd
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

f.close()

#해당 기록내에서 K-mean Clustering을 통해서 분류하는 코드

df = pd.read_csv('student_health_3_change.csv', encoding = "cp949")
#df.head()로 읽은 거 확인

#수축기, 이완기, 키, 몸무게
X = df.iloc[:, [23,24,15,16]].values

#배열 집합 개수(m), 특징 개수(n)
m=X.shape[0]
n=X.shape[1]

plt.scatter(X[:,0],X[:,1],c='black',label='Class')
plt.xlabel('Class1')
plt.ylabel('Class2')
plt.legend()
plt.title('Class')
plt.show()
