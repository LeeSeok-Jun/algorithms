"""
1이 될 때까지
- 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행한다.
- 단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
    1. N에서 1을 뺀다.
    2. N을 K로 나눈다.
- N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오.

입력 조건
- 첫째 줄에 N(2 <= N <= 100,000)과 K(2 <= K <= 100,000)가 공백으로 구분되며 각각 자연수로 주어진다.
- 입력으로 주어지는 N은 항상 K보다 크거나 같다.

출력 조건
- 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야하는 횟수의 최솟값을 출력한다.
"""

### 1. 단순하게 푸는 답안 ###

# N, K를 공백으로 입력받아 확인
n, k = map(int, input().split())
result = 0

# N이 K 이상이면 K로 나누기 반복
while (n >= k):
    # N이 K로 나누어 떨어지지 않는 다면 1빼기
    if (n % k != 0):
        n -= 1
        result += 1
    
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
# 이 동작이 실행될 때 변수 n은 변수 k보다 작아진 상태이므로 더이상 나눗셈을 실행할 수 없다.
while (n > 1):
    n -= 1
    result += 1

print(result) # 결과 출력