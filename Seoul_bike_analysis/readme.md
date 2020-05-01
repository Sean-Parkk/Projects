# 서울시 따릉이 데이터 분석
* 데이터 소스: [대여소 정보](https://data.seoul.go.kr/dataList/OA-13252/F/1/datasetView.do), [이용 정보](https://data.seoul.go.kr/dataList/OA-15248/F/1/datasetView.do)
* 새로 알게된 것
  * folium plugin
    * HeatMap, Clustering을 자주 쓰게될 듯.
    * [folium github](https://github.com/python-visualization/folium/tree/master/examples)
    * [이를 구현 국내 블로그](https://dailyheumsi.tistory.com/85)
  * folium icon
    * icon을 맘대로 적용할 수 있음
    * [Font-Awesome](https://fontawesome.com/)에서 아이콘 찾은 후, 아이콘명과 접두사를 넣어주면 사용 
      ```python
      folium.Marker([lat, lng], icon=folium.Icon(color='black',icon="bicycle", prefix='fa')).add_to(map)
      ```
