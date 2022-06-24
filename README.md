# HowDoYouFeel
딥러닝 프로젝트 컴퓨터비전을 통한 반려견 감정분석

## 프로젝트 배경

---

## 프로젝트 목표

- 크롤링을 통해 구글 이미지 수집
- 딥러닝 모델링
- 웹 어플리케이션 구축 및 배포

---

### 데이터 셋

- 구글 키워드 수집 이미지
  - happy
  - angry
  - sad
  - hurgry
  - amazed

---

### 데이터파이프라인

![Untitled (14)](https://user-images.githubusercontent.com/86764734/175530392-70de8f3a-72f3-4300-bb54-381eab8abddc.png)

---

### 분석과정

- 데이터 수집
    - selenium으로 구글검색 이미지 스크래핑
- 데이터 전처리
    - Class 분류
    - 정규화
    
    ![Untitled (15)](https://user-images.githubusercontent.com/86764734/175530570-c4612c75-1eab-408b-84d1-e673472e7735.png)
    
    - 데이터 증강
    
    ![Untitled (16)](https://user-images.githubusercontent.com/86764734/175530641-312f49d7-5d77-4334-be45-c22c59d9bddc.png)
    
- 모델 선정
    - CNN (Val_Acc = 0.328)
    - ResNet50 (Val_Acc = 0.449)
- 하이퍼파라미터 튜닝 (Val_Acc = 0.524)
    - Early stopping
    - ModelCheckpiont

---

### 개선사항

- 모델 성능 향상
  - 추가 데이터 수집
  - 모델 파라미터 튜닝
- 웹개발
  - 모델삽입
  - 배포
