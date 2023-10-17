"""
문제 설명
n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 
타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.

"""

from itertools import product


def solution(numbers, target):
    def dfs(index, total):
        if index == len(numbers):
            if total == target:
                return 1
            return 0
        return dfs(index + 1, total + numbers[index]) + dfs(
            index + 1, total - numbers[index]
        )

    return dfs(0, 0)


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))  # 출력: 5


def solution3(numbers, target):
    l = [(x, -x) for x in numbers]
    print(l)  # [(1, -1), (2, -2), (3, -3), (4, -4), (5, -5)]
    s = list(map(sum, product(*l)))  # *l -> 튜플 언팩킹
    print(
        s
    )  # [15, 5, 7, -3, 9, -1, 1, -9, 11, 1, 3, -7, 5, -5, -3, -13, 13, 3, 5, -5, 7, -3, -1, -11, 9, -1, 1, -9, 3, -7, -5, -15]
    return s.count(target)  # s 안에서 target 과 같은 숫자를 가진 인자를 카운트


numbers = [1, 2, 3, 4, 5]
target = 3
print(solution3(numbers, target))  # 출력: 4
