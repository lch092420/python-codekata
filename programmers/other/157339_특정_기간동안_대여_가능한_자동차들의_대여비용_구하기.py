# 특정 기간동안 대여 가능한 자동차들의 대여비용 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/157339
# 작성자: 학생
# 작성일: 2026. 01. 21. 10:57:57

-- 코드를 입력하세요
-- 세단 혹은 SUV
-- 2022년 11월 대여 가능
-- 30일간 대여 금액이 50만원 이상 200만원 미만
SELECT *
FROM (
    SELECT
        R.CAR_ID,
        R.CAR_TYPE,
        ROUND(
            R.DAILY_FEE * 30 * (1 - D.DISCOUNT_RATE / 100),
            0
        ) AS FEE
    FROM CAR_RENTAL_COMPANY_CAR R
    JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN D
      ON R.CAR_TYPE = D.CAR_TYPE
     AND D.DURATION_TYPE = '30일 이상'
    WHERE R.CAR_TYPE IN ('세단', 'SUV')
      AND NOT EXISTS (
          SELECT 1
          FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H
          WHERE H.CAR_ID = R.CAR_ID
            AND H.START_DATE <= '2022-11-30'
            AND H.END_DATE   >= '2022-11-01'
      )
) T
WHERE FEE >= 500000
  AND FEE < 2000000
ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC;

