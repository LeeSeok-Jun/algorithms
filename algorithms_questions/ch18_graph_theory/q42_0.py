"""
탑승구
- 공항에는 각각 1 ~ G 까지의 번호로 구분된 G개의 탑승구가 있다.
- 공항에는 P개의 비행기가 차례대로 도착할 예정이며, i번째 비행기를 1번부터 g[i]번째 탑승구 중 하나에 영구적으로 도킹한다.
- 이때, 다른 비행기가 도킹하지 않은 탑승구에만 도킹할 수 있다.
- 또한 P개의 비행기를 순서대로 도킹하다가 만약에 어떠한 탑승구에도 도킹할 수 없는 비행기가 나오는 경우,
  그 시점에서 공항의 운행을 중지한다.
- 공항의 관리자는 최대한 많은 비행기를 공항에 도킹하고자 한다.
- 비행기를 최대 몇 대 도킹할 수 있는지를 출력하는 프로그램을 작성하시오.

입력 조건
- 첫째 줄에는 탑승구의 수 G가 주어진다.
- 둘째 줄에는 비행기의 수 P가 주어진다.
- 다음 P개의 줄에는 각 비행기가 도킹할 수 있는 탑승구의 정보 g[i]가 주어진다.
    * 이는 i번째 비행기가 1번부터 g[i]번째 탑승구 중 하나에 도킹할 수 있다는 의미이다.

출력 조건
- 첫째 줄에 도킹할 수 있는 비행기의 최대 개수를 출력한다.
"""

# 풀이 제한 시간 : 50분
# 2020/12/29 11:15 ~ 11:34
# 실패 - 서로소 집합 알고리즘 사용하기

g = int(input())
p = int(input())

goal = []
for _ in range(p):
    goal.append(int(input()))

goal.sort()

gate = [0] * g

for gi in goal:
    for i in range(gi):
        if gate[i] == 0:
            gate[i] = 1
            break

result = 0
for i in range(g):
    if gate[i] == 1:
        result += 1

print(result)

