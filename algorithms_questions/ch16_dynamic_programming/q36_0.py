"""
편집 거리

- 두 개의 문자열 A와 B가 주어졌을 때, 문자열 A를 편집하여 문자열 B로 만들고자 한다.
- 문자열 A를 편집할 때는 다음의 세 연산 중에서 한 번에 하나씩 선택하여 이용할 수 있다.
    * 삽입(Insert) : 특정한 위치에 하나의 문자를 삽입힌다.
    * 삭제(Remove) : 특정한 위치에 있는 하나의 문자를 삭제한다.
    * 교체(Replace) : 특정한 위치에 있는 하나의 문자를 다른 문자로 교체한다.
- 편집 거리란 문자열 A를 편집하여 문자열 B로 만들기 위해 사용한 연산의 수를 의미한다.
- 문자열 A를 문자열 B로 만드는 최소 편집 거리를 계산하는 프로그램을 작성하시오.

입력 조건
- 두 문자열 A와 B가 한 줄에 하나씩 주어진다.

출력 조건
- 최소 편집 거리를 출력한다.
"""

# 풀이 제한 시간 : 30분
# 2020/12/15 12:40 ~ 13:00
# 실패 - 점화식 유도 실패

"""
a = input()
b = input()

answer = 0

# a가 더 길면 삭제
if len(a) > len(b):
    answer += (len(a) - len(b))
"""

# 최소 편집 거리 구하기
def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    # 열은 문자열 B의 길이 만큼, 행은 문자열 A의 길이 만큼 DP 테이블 할당
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # dp 테이블 초기 설정
    for i in range(1, n+1):
        dp[i][0] = i # 문자열 A에 대한 초기 설정
    for j in range(1, m+1):
        dp[0][j] = j # 문자열 B에 대한 초기 설정

    # 최소 편집 거리 계산
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 두 문자가 같은 경우
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # 두 문자가 다른 경우
            else:
                # 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽 위) 중 최소비용을 찾아 1 증가
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    return dp[n][m] # 마지막 값이 최소 편집 거리

str1 = input()
str2 = input()

print(edit_dist(str1, str2))