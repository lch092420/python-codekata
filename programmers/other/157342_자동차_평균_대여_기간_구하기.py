# 자동차 평균 대여 기간 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/157342
# 작성자: 학생
# 작성일: 2026. 01. 19. 11:37:24

-- 코드를 입력하세요 --
SELECT CAR_ID,
ROUND(AVG(DATEDIFF(END_DATE,START_DATE)+1),1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY 1
HAVING AVERAGE_DURATION >= 6
ORDER BY 2 DESC, 1 DESC