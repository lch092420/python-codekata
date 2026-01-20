# FrontEnd 개발자 찾기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/276035
# 작성자: 학생
# 작성일: 2026. 01. 20. 09:23:45

-- 코드를 작성해주세요
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS
WHERE SKILL_CODE & (SELECT SUM(CODE)
                    FROM SKILLCODES
                    WHERE CATEGORY = 'Front End') != 0
ORDER BY ID