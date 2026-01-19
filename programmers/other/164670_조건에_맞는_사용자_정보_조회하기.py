# 조건에 맞는 사용자 정보 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/164670
# 작성자: 학생
# 작성일: 2026. 01. 19. 11:37:08

-- 코드를 입력하세요
SELECT USER_ID, NICKNAME, CONCAT(CITY,' ',STREET_ADDRESS1,' ',STREET_ADDRESS2) AS 전체주소,
CONCAT(SUBSTR(TLNO,1,3),'-',SUBSTR(TLNO,4,4),'-',SUBSTR(TLNO,8,4)) AS 전화번호
FROM USED_GOODS_USER U
WHERE U.USER_ID IN(
SELECT B.WRITER_ID
FROM USED_GOODS_BOARD B
GROUP BY 1
HAVING COUNT(*) >= 3
)
ORDER BY 1 DESC