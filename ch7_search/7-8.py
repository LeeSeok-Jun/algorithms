"""
떡볶이 떡 만들기
- 길이가 일정하지 않은 떡볶이용 떡이 있다. 이 떡의 총 길이는 절단기로 잘라서 맞춘다.
- 절딘가에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다.
- 길이가 H보다 긴 떡은 H 위의 부분이 잘리고 낮은 부분은 잘리지 않는다.
- 손님은 잘린 부분의 길이의 총합 만큼 떡을 가져간다.
- 손님이 요청한 총 길이가 M일 때, 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

입력 조건
- 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다.(1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000)
- 둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M 이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다.
  높이는 10억보다 작거나 같은 양의 정수 또는 0이다.

출력 조건
- 적어도 M만큼의 떡을 집에 가져가지 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
"""

# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력받기
n, m = list(map(int, input().split(' ')))
# 각 떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array) # 떡 중에서 가장 길이가 긴 떡의 길이를 끝점으로 설정

# 이진 탐색 수행(반복적인 방법)
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색) = 탐색 범위를 중간값 왼쪽으로 이동
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 더 적게 자르기(오른쪽 부분 탐색) = 탐색 범위를 중간값 오른쪽으로 이동
    else:
        result = mid # 최대한 절단 길이가 작을수록 정답 -> 반복문을 탈출하면 자연히 정답으로 도출
        start = mid + 1

# 정답 출력
print(result)