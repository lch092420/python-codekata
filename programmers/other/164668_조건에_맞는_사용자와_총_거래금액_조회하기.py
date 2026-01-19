# 조건에 맞는 사용자와 총 거래금액 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/164668
# 작성자: 학생
# 작성일: 2026. 01. 19. 11:36:35

-- 코드를 입력하세요
SELECT U.USER_ID,U.NICKNAME,SUM(B.PRICE) AS TOTAL_SALES
FROM USED_GOODS_USER U JOIN USED_GOODS_BOARD B 
    ON U.USER_ID = B.WRITER_ID
WHERE B.STATUS='DONE'
GROUP BY 1,2
HAVING TOTAL_SALES >=700000
ORDER BY 3