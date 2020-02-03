import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import seaborn as sns
# import missingno as msno
# import random
# import datetime
# import pytz
import warnings
warnings.filterwarnings('ignore')
sns.set(font_scale=1.3)
plt.style.use('seaborn-pastel')
fontpath = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
font = fm.FontProperties(fname=fontpath, size=9)
plt.rc('font', family='NanumBarunGothic')
mpl.font_manager._rebuild()

# csv데이터 읽기
df = pd.read_csv('D:\작업\Python\dont_starve.csv')

# 결과값 O, X에서 0, 1로 변환
df['result'] = df['result'].map({'O': 1, 'X': 0})

# 식사 데이터 시각화
f, ax = plt.subplots(2, 3, figsize=(18,10))
sns.countplot('breakfast', data=df, ax=ax[0,0], order=['먹음', '안먹음'])
ax[0,0].set_title('아침 식사 여부')
ax[0,0].set_xlabel('')
ax[0,0].set_ylim([0,75])

sns.barplot('breakfast','result',data=df, ax=ax[1,0], order=['먹음', '안먹음'])
ax[1,0].set_title('아침 식사 - result')
ax[1,0].set_xlabel('')
ax[1,0].set_ylim([0,1])

sns.countplot('lunch', data=df, ax=ax[0,1])
ax[0,1].set_title('점심 식사 여부')
ax[0,1].set_xlabel('')
ax[0,1].set_ylim([0,75])

sns.barplot('lunch','result',data=df, ax=ax[1,1])
ax[1,1].set_title('점심 식사 - result')
ax[1,1].set_xlabel('')
ax[1,1].set_ylim([0,1])

sns.countplot('dinner', data=df, ax=ax[0,2])
ax[0,2].set_title('저녁 식사 여부')
ax[0,2].set_xlabel('')
ax[0,2].set_ylim([0,75])


sns.barplot('dinner','result',data=df, ax=ax[1,2])
ax[1,2].set_title('저녁 식사 - result')
ax[1,2].set_xlabel('')
ax[1,2].set_ylim([0,1])


# 운동 데이터 시각화
f, ax=plt.subplots(1,2, figsize=(15,7))
sns.countplot('workout', data=df, ax=ax[0])
ax[0].set_title('아침 운동 여부')
ax[0].set_ylim(0,50)
ax[0].set_xlabel('')

sns.barplot('workout', 'result', data=df,ax=ax[1])
ax[1].set_title('아침 운동 시 배고픔 유무')
ax[1].set_ylim(0,1)
ax[1].set_xlabel('')

# 외부 활동 데이터 시각화
f, ax = plt.subplots(1, 2, figsize=(15, 7))
sns.countplot('activity', data=df, order = df['activity'].value_counts().index, ax=ax[0])
ax[0].set_title('각 외부 활동 수 비교')
sns.barplot('activity', 'result', data=df, order = df['activity'].value_counts().index, ax=ax[1])
ax[1].set_title('외부 활동 별 배고픔 유무')

# 걸음 수 시각화
df['date'] = pd.to_datetime(df['date'], unit='ns') # dt 형식으로 바꿔주기
df['DoW'] = df['date'].dt.weekday_name # 요일 컬럼 만들기
f, ax = plt.subplots(2,1,figsize=(15,7))
sns.lineplot('date', 'walk', data=df, ax=ax[0])
ax[0].set_title('일자별 걸음 수 추이')
ax[0].set_xlabel('')
sns.barplot(x='DoW',y='walk', order=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'], data=df, ax=ax[1])
ax[1].set_title('요일별 평균 걸음 수')
ax[1].set_xlabel('')

f, ax = plt.subplots(1, 2, figsize=(15, 7))
sns.barplot('result', 'walk',data=df, x=ax[0])
ax[0].set_title('배고픔 유무별 평균 걸음 수')
ax[0].set_xlabel('')
sns.barplot('activity', 'walk', data=df, ax=ax[1])
ax[1].set_title('활동별 평균 걸음 수')
ax[1].set_xlabel('')

# 공부 시간 데이터 시각화
f, ax = plt.subplots(1, 2, figsize=(15,7))
sns.barplot('result', 'study', data=df, order = df['result'].value_counts().index, ax=ax[0])
ax[0].set_title('배고픔 유무별 평균 공부 시간')

sns.barplot('activity', 'study', data=df, ax=ax[1])
ax[1].set_title('외부 활동별 평균 공부 시간')

f, ax = plt.subplots(2, 1, figsize=(15,7))
sns.kdeplot(df[df['result']==1]['study'], ax=ax[0])
sns.kdeplot(df[df['result']==0]['study'], ax=ax[0])
ax[0].legend(['배 고팠던날', '배 안 고팠던날'])
ax[0].set_title('배고픔 유무 별 공부 시간')
ax[0].set_xlim(-5,25)
ax[0].set_ylim(0,0.15)

sns.kdeplot(df[df['result']==1][df['activity']=='없음']['study'], ax=ax[1])
sns.kdeplot(df[df['result']==0][df['activity']=='없음']['study'], ax=ax[1])
ax[1].legend(['배 고팠던날', '배 안 고팠던날'])
ax[1].set_title('외부 활동 없던 날의 공부 시간')
ax[1].set_xlim(-5,25)
ax[1].set_ylim(0,0.15)

# 상관관계 분석 - onehot
df['breakfast'] = df['breakfast'].map({'안먹음': 0, '먹음': 1})
df['lunch'] = df['lunch'].map({'안먹음': 0, '먹음': 1})
df['dinner'] = df['dinner'].map({'안먹음': 0, '먹음': 1})
df['workout'] = df['workout'].map({'안했음': 0, '했음': 1})
onehot_Data = pd.get_dummies(df)

df['Date'] = 0
heatmap_data=onehot_Data[['breakfast', 'lunch', 'dinner', 'workout', 'activity_데이트', 'activity_친구', 'activity_외출', 'activity_축구', 'activity_없음','activity_병원', 'walk', 'study', 'result']]
colormap = plt.cm.PRGn
plt.figure(figsize=(8,8))
plt.title('상관관계 히트맵', y=1.05, size=15)
sns.heatmap(heatmap_data.astype(float).corr(), linewidths=1, vmax=1.0,
           square=True,cmap=colormap, linecolor='white', annot=True, annot_kws={'size': 16}, fmt='.2f')
