# 🛍️비지도학습 - 비슷한 행동을 보이는 고객 세분화 분석
</br>

## 데이터셋: Mall_Customers.csv

<details>
<summary>컬럼별 설명</summary>
<div markdown="1">

- CustomerID: 고객의 고유 번호
- Gender: 성별
- Age: 나이
- Annual Income(k$): 연간 소득
- Spending Score(1-100): 고객 지출 기반 점수

</div>
</details>
</br>

## 🤖 고객 세분화 분석

1. **데이터셋 탐색 및 전처리**
    - 결측치 처리
    - 이상치 처리
    - 데이터 시각화
    - 스케일링
        - 데이터의 스케일을 조정하기 위해 표준화(Standardization) 또는 정규화(Normalization)를 수행
2. **클러스터링 기법 적용**
    - K-means
    - 계층적 군집화
    - DBSCAN 등의 알고리즘
3. **최적의 클러스터 수 결정**
    - 엘보우 방법 또는 실루엣 점수를 사용하여 최적의 클러스터 수 찾기
4. **결과 시각화**
    - 클러스터링 결과를 2D 또는 3D로 시각화하여 고객 세분화 결과 분석
        - **시각화**: matplotlib 또는 seaborn을 사용하여 클러스터를 색상으로 구분하여 시각화, 2D 플롯을 사용하여 각 클러스터를 다른 색으로 표현