"""
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 
흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 
종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
입출력 예
numbers	return
"17"	3
"011"	2
입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

11과 011은 같은 숫자로 취급합니다.

"""

from itertools import permutations
import math


def is_prime(n):
    if n < 2:
        return False

    # 2 부터 루트 n 이하 까지만 골라서 n 을 나누어 보면 됨
    # 그래서 + 1 을 해서 "이하" 로 만들어 줌
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# if numbers = "17"
def solution(numbers):
    paper = set()

    # 1 부터 nubers 의 길이만큼 횟수 반복
    # range(1, 3) => i = 1, i = 2
    for i in range(1, len(numbers) + 1):
        # perm = permutations("17", i)
        perm = permutations(numbers, i)
        # 1일 때 생성되는 순열: ('1',), ('7',)
        # 2일 때 생성되는 순열: ('1', '7'), ('7', '1')
        for p in perm:
            paper.add(int("".join(p)))
            print(paper)
            # 1일 때: '1' 과 '7' 을 정수로 변환하여 {1, 7} 을 paper 에 추가
            # 2일 때: '17' 과 '71' 을 정수로 변환하여 {17, 71} 을 paper 에 추가
            """
            {1}
            {1, 7}
            {1, 17, 7}
            {1, 71, 17, 7}
            """
    answer = 0
    for number in paper:
        if is_prime(number):
            answer += 1

    return answer


numbers = "17"
print(solution(numbers))  # 3

# numbers = "011"
# print(solution(numbers))  # 2
