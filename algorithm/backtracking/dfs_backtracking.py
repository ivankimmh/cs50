"""
DFS (Depth First Search) 깊이 우선 탐색

하나의 정점으로부터 시작하여 차례대로
모든 정점을 한번 씩 방문하는 것

예를 들어, 특정 도시에서 다른 도시로 갈 수 있는지 없는지,
전자 회로에서 특정 단자와 단자가 서로 연결되어 있는지 등

특징,
자기 자신을 호출하는 순환 알고리즘의 형태를 가지고 있다.
그래프 탐색의 경우, 어떤 노드를 방문했었는지 여부를 판단한다.
-> 그렇지 않으면 무한루프에 빠질 위험이 있다.

백트랙킹 (backtracking)
백트랙킹은 깊이 우선 탐색 중, "해가 아니면 다시 돌아온다." feat. 가지치기
즉, 불필요한 경로는 굳이 끝까지 탐색하지 않겠다는 것

현재 상태에서 가능한 모든 경로를 따라 들어가 탐색하다가,
원하는 값과 불일치하는 부분이 발생하면 더 이상 탐색을 진행하지 않고
전 단계로 돌아가는 알고리즘
"""

from typing import List


def dfs_backtracking(nums: List[int], target: int):
    print("what you got : ", nums, target)
    print("1")
    results = []

    def backtrack(remain: int, comb: List[int], start: int):
        print("2")
        # Base case, remain is 0
        if remain == 0:
            print("3")
            results.append(list(comb))
            return

        # Base case, remain < 0 (too high)
        elif remain < 0:
            print("4")
            return
        print("check : ", range(start, len(nums)))
        for i in range(start, len(nums)):
            print("5")
            comb.append(nums[i])
            backtrack(remain - nums[i], comb, i)
            comb.pop()
            # Cover the append and pop abit more

    print("6")
    backtrack(target, [], 0)
    print("7")
    return results


def dfs_unique_backtracking(nums: List[int]):
    results = []

    def backtrack(curr_nums: List[int], remain_nums: List[int], start: int):
        # Base case, remain is 0
        if len(remain_nums) == 0:
            results.append(list(curr_nums))
            return

        for i in range(start, len(remain_nums)):
            new_remain_nums = remain_nums[0:i] + remain_nums[i + 1 : len(remain_nums)]
            backtrack(curr_nums, new_remain_nums, i)  # Without that num
            backtrack(curr_nums + [remain_nums[i]], new_remain_nums, i)  # With that num

    backtrack([], nums, 0)
    return results


print(dfs_backtracking([3, 4, 5], 8))
print(dfs_unique_backtracking([3, 4, 5]))
