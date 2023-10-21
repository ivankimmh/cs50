import functools

"""
문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
"""


def compare(x, y):
    t1 = x + y  # "10" + "2" = "102"
    t2 = y + x  # "2" + "10" = "210"
    print(int(t1), int(t2), int(t1) > int(t2))
    print(int(t1), int(t2), int(t1) < int(t2))
    print("value :", (int(t1) > int(t2)) - (int(t1) < int(t2)))

    # true = 1, false = 0
    return (int(t1) > int(t2)) - (int(t1) < int(t2))  #  t1이 크다면 1, 작다면 -1, 같으면 0


def solution(numbers):
    answer = ""

    n = [str(x) for x in numbers]  # 리스트 컴프리헨션 문자 배열로 변환하여 n 에 저장
    print("before sorted: ", n)  # ['6', '10', '2']

    n = sorted(n, key=functools.cmp_to_key(compare), reverse=True)
    print("after sorted: ", n)  # ['6', '2', '10']

    answer = str(int("".join(n)))

    return answer


# 예시 데이터 1
numbers1 = [6, 10, 2]
print(solution(numbers1))  # 출력: "6210"

# 예시 데이터 2
numbers2 = [3, 30, 34, 5, 9]
print(solution(numbers2))  # 출력: "9534330"

# 예시 데이터 3
numbers3 = [900, 9, 99]
print(solution(numbers3))  # 출력: "999900"
