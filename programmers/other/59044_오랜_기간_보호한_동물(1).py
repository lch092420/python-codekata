# 오랜 기간 보호한 동물(1)
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59044
# 작성자: 학생
# 작성일: 2026. 01. 19. 11:34:50

-- 코드를 입력하세요
SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS I
WHERE NOT EXISTS (
SELECT 1
FROM ANIMAL_OUTS O
WHERE I.ANIMAL_ID = O.ANIMAL_ID
) 
ORDER BY 2
LIMIT 3