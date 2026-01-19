# 특정 세대의 대장균 찾기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/301650
# 작성자: 학생
# 작성일: 2026. 01. 19. 16:00:20

-- 코드를 작성해주세요
SELECT ID
FROM ECOLI_DATA
WHERE PARENT_ID IN (SELECT B.ID
FROM ECOLI_DATA A JOIN ECOLI_DATA B ON A.ID = B.PARENT_ID
WHERE A.PARENT_ID IS NULL)
ORDER BY ID 