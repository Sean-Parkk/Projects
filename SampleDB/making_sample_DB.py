import numpy as np
import pandas as pd
import random

df_sampleDB = pd.DataFrame(columns=['name', 'birth', 'sex', 'district', 'grade', 'regist', 'lastlogin', 'logincnt', 'cartcnt', 'ordercnt', 'orderqty', 'orderprice', 'couponcnt', 'couponused', 'refund'])
# 데이터 프레임 생성
Lastname, Firstname = '김이박최정강조윤장임한오서신권황안송전홍', '시림서환원태예우재빈석진이정준선연율강하사랑소찬건한리훈람유승성수아양현채안윤후은희린주혜인가도호민온세름다나영결완지동규혁'
# 랜덤 이름 생성을 위한 셋팅 (출처: https://koreanname.me/)
birth_random = pd.date_range(start='19800101', end='20011231')
# 20세부터 40세까지로 나이 제한
list_district = ['도봉구', '강북구', '노원구', '은평구', '종로구', '성북구', '중랑구', '동대문구', '서대문구', '중구', '성동구', '광진구', '강동구', '마포구', '용산구', '강서구', '양천구', '영등포구', '구로구', '동작구', '금천구', '관악구', '서초구', '강남구','송파구','강동구']
# 서울시 내 구단위로 거주지역 제한
regist_random = pd.date_range(start='20180101', end='20191231')
# 서비스 런칭 시점 18년 1월 1일로 설정
list_refundpcnt = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
# 구매제품 환불확률 5%로 설정 (구매 건수 당으로 설정, not each 구매 제품))

for i in range(0,1):
  dt_name = random.choice(Lastname) + random.choice(Firstname) + random.choice(Firstname)
  dt_birth = random.choice(birth_random.strftime("%Y%m%d").tolist())
  dt_sex = random.sample(['male', 'female'], 1)[0]
  dt_district = random.sample(list_district, 1)[0]
  dt_grade = random.randrange(1,4,1)
  dt_regist = random.choice(regist_random.strftime("%Y%m%d").tolist())
  lastlogin_random = pd.date_range(start=dt_regist, end='20191231')
  dt_lastlogin = random.choice(regist_random.strftime("%Y%m%d").tolist())
  dt_logincnt = (2**(dt_grade-1)) + random.randrange(0, 31, 1)
  dt_cartcnt = (3**(dt_grade-1)) + random.randrange(0, 11, 1)
  dt_ordercnt = random.randrange(0,int(dt_cartcnt/2)+1)+int(2**random.randrange(dt_grade-2,dt_grade+2)) + dt_grade-1
  dt_orderqty = sum(int(random.sample([1, 1, 1, 1, 1, 1, 2, 2, 2, 3], 1)[0]) for qty in range(0,dt_ordercnt))
  dt_orderprice = sum([random.randrange(5000, 35001, 5000) for odcnt in range(0, dt_ordercnt)])
  dt_couponcnt = sum([random.randint(0,1) for cpn in range(0,int(dt_logincnt/3))])
  dt_couponused = dt_couponcnt - sum([random.randint(0,1) for cpn in range(0, dt_couponcnt)])
  dt_refund = sum([int(random.sample(list_refundpcnt, 1)[0]) for rfd in range(0,dt_ordercnt)])

  df_sampleDB.loc[i] = {'name': dt_name,
                        'birth': dt_birth,
                        'sex': dt_sex,
                        'district': dt_district,
                        'grade': dt_grade,
                        'regist': dt_regist,
                        'lastlogin': dt_lastlogin,
                        'logincnt': dt_logincnt,
                        'cartcnt': dt_cartcnt,
                        'ordercnt': dt_ordercnt,
                        'orderqty': dt_orderqty,
                        'orderprice': dt_orderprice,
                        'couponcnt': dt_couponcnt,
                        'couponused': dt_couponused,
                        'refund': dt_refund
                         }
