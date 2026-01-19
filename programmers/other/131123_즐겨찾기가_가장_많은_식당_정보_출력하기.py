# 즐겨찾기가 가장 많은 식당 정보 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131123
# 작성자: 학생
# 작성일: 2026. 01. 19. 11:36:46

-- 코드를 입력하세요
WITH RN AS(
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES,
    RANK() OVER (PARTITION BY FOOD_TYPE ORDER BY FAVORITES DESC) AS RNK
FROM REST_INFO
)
SELECT RN.FOOD_TYPE,RN.REST_ID, RN.REST_NAME, RN.FAVORITES
FROM RN
WHERE RNK = 1
ORDER BY 1 DESC