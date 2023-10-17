"""
문제 설명
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 
예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 
컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 
따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 
네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

제한사항
컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
computer[i][i]는 항상 1입니다.
입출력 예
n	computers	return
3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1
"""

def dfs(computers, visited, start):
    stack = [start]
    while stack:
        j = stack.pop()
        if visited[j] == 0: # 방문했으니 값이 변한다.
            visited[j] = 1
        for i in range(len(computers)): # 비교해서 stack 쌓기
            if computers[j][i] == 1 and visited[i] == 0: # 컴퓨터가 돌 때, j 값의 컴퓨터가 i 값의 컴퓨터를 방문했을 때
                # 방문했다면 visited 가 변하지
                stack.append(i) # 스택을 쌓아서 더 돌리게 

def solution(n, computers):
    visited = [0] * n # 인자를 0 으로 가지는 길이 n 의 배열을 만듬
    print("visited : ", visited) # [0, 0, 0]

    answer = 0 # 네트워크의 갯수 -> 컴퓨터와 컴퓨터가 연결이 되어 있으면 네트워크 1

    for i in range(n): # 0, 1, 2 돌리면서 실행
        if visited[i] == 0:
            dfs(computers, visited, i) # 실행시켜서 연결시켜본다.
            print("더해진다?")
            answer += 1
    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# computer[0][0] -> 컴퓨터 0 과 컴퓨터 0 은 연결 되어 있음
# computer[0][1] -> 컴퓨터 0 과 컴퓨터 1 은 연결 되어 있음
# computer[0][2] -> 컴퓨터 0 과 컴퓨터 2 는 연결 되어 있지 않음
# computer[1][0] -> 컴퓨터 1 과 컴퓨터 0 은 연결 되어 있음
# computer[1][1] -> 컴퓨터 1 과 컴퓨터 0 은 연결 되어 있음
# computer[1][2] -> 컴퓨터 1 과 컴퓨터 2 는 연결 되어 있지 않음


computers2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers)) # return 2
# print(solution(n, computers2)) # return 1