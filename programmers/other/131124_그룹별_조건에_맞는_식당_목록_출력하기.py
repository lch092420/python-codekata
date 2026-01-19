# 그룹별 조건에 맞는 식당 목록 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131124
# 작성자: 학생
# 작성일: 2026. 01. 19. 11:56:21

-- 코드를 입력하세요
SELECT M.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE,'%Y-%m-%d') AS REVIEW_DATE
FROM REST_REVIEW R JOIN MEMBER_PROFILE M ON R.MEMBER_ID = M.MEMBER_ID
WHERE M.MEMBER_ID = (SELECT MEMBER_ID
                     FROM REST_REVIEW
                     GROUP BY 1
                     ORDER BY COUNT(*) DESC
                     LIMIT 1)
ORDER BY R.REVIEW_DATE, R.REVIEW_TEXT