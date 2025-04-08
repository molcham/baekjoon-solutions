"""
1. 문제 읽기
예를 들어 Queue에 4개의 문서(A B C D)가 있고, 
중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.
여러분이 할 일은, 
현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 
어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 
예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.
2. 문제 풀기
그냥 맥스힙이다. 
테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 
몇 번째로 인쇄되었는지 궁금한 문서가 
현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 
이때 맨 왼쪽은 0번째라고 하자. 
두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 
중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.
1 0
5
이 경우, 문서의 개수는 1, 0번째 문서가 언제 출력됐는지 궁금함. 문서 하나의 중요도는 5. 당연히 답은 1
4 2
1 2 3 4
이 경우는 3 문서가 언제 출력됐는지. 당연히 2.
주의사항: 중요도가 같은 문서가 여럿일 수 있다. 따라서 힙에 넣기 전에 인덱스를 같이 넣어야 한다.
큰 문제가 발생했다. 중요도를 기준으로 힙을 사용하면, 같으면 루트 이하의 노드들은 전부 어긋난다.
큐를 쓰긴 해야하는 거다.
큐랑 힙을 혼합 사용해야하는 건가? 그런 거 같다. 힙은 일단 현재 문서들의 최대 우선순위가 무엇인지는
저장하고 있을 수 있다.
그러면 그 max_priority가 아닌동안 큐에서 인큐, 디큐 과정을 반복해야 한다.
3. 수도 코드
(힙을 이용하여 문제를 푸는 함수: 문서 길이, 찾는 인덱스, 전체 문서 배열)
    (힙 소환)
    (힙에 그냥 우선순위 집어넣기)
    (전체 문서를 큐로 만들기)
    (target_prior에 찾는 문서의 우선순위 저장하기)
    (while문을 돌려서, target_prior < max_prior인 동안)
        (while head 인덱스가 타겟 인덱스가 아닌 동안)
            (인큐, 디큐를 반복해서 head prior를 업데이트)
        (head를 큐에서 제거, 힙에서도 팝.)
    (찾았으면 카운트 리턴(처음엔 1로 초기화))
(테스트케이스별로 반복)
확인할 점: 인덱스랑 같이 집어넣어도 맥스힙이 유지가 되나? 된다. 대신 중요도, 인덱스 순의 튜플을 써야함.
아 그냥 힙 써서 다 없앤 다음 인덱스 순으로 정렬해서 뽑으면 되는데.
이 풀이의 문제점: 수도코드에 의존해서 풀다가 그냥 구현하면서 차례로 로그 찍어서 해결하면 될걸
그냥 스스로 힘든 길을 가버렸다.
4. 코드 구현
"""

import heapq 
import sys
from collections import deque

def solve(n: int, target_idx: int, docs: list):
    que = deque([(docs[i], i) for i in range(n)])
    heap = []
    heapq.heapify(heap)
    for i in range(n):
        heapq.heappush(heap, -docs[i])
    print(f'que: {que}, heap: {heap}')
    root = -heapq.heappop(heap)
    cnt = 1
    while root > que[0][0]:
        tmp = que.popleft()
        que.append(tmp)
        cnt += 1
        if root == que[0][0]:
            root = -heapq.heappop(heap)
            que.popleft()
        print(f'que: {que}')

if __name__ == '__main__':
    input = sys.stdin.readline
    t = int(input().strip())
    for _ in range(t):
        n, m = tuple(map(int, input().split()))
        docs = tuple(map(int, input().split()))
        solve(n, m, docs)

"""
이슈: 
Phase1.
환경: 파이썬
로그: pop from an empty space
최근 변경 사항: 힙과 큐를 사용해 우선순위를 유지하며 문서 출력 함수 작성
Phase2.
확인: 
아래 입력에서 발생 해결
4 2
1 2 3 4
시도: 
분석: 
"""