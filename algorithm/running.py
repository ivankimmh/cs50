"""
달리기 경주

문제 설명
얀에서는 매년 달리기 경주가 열립니다. 
해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다. 
예를 들어 1등부터 3등까지 "mumu", "soe", "poe" 선수들이 순서대로 달리고 있을 때, 
해설진이 "soe"선수를 불렀다면 2등인 "soe" 선수가 1등인 "mumu" 선수를 추월했다는 것입니다. 
즉 "soe" 선수가 1등, "mumu" 선수가 2등으로 바뀝니다.

선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 해설진이 부른 이름을 담은 
문자열 배열 callings가 매개변수로 주어질 때, 
경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.

제한사항
5 ≤ players의 길이 ≤ 50,000
players[i]는 i번째 선수의 이름을 의미합니다.
players의 원소들은 알파벳 소문자로만 이루어져 있습니다.
players에는 중복된 값이 들어가 있지 않습니다.
3 ≤ players[i]의 길이 ≤ 10
2 ≤ callings의 길이 ≤ 1,000,000
callings는 players의 원소들로만 이루어져 있습니다.
경주 진행중 1등인 선수의 이름은 불리지 않습니다.
입출력 예
players	callings	result
["mumu", "soe", "poe", "kai", "mine"]	["kai", "kai", "mine", "mine"]	["mumu", "kai", "mine", "soe", "poe"]
입출력 예 설명
입출력 예 #1

4등인 "kai" 선수가 2번 추월하여 2등이 되고 앞서 3등, 2등인 "poe", "soe" 선수는 4등, 3등이 됩니다. 
5등인 "mine" 선수가 2번 추월하여 4등, 3등인 "poe", "soe" 선수가 5등, 4등이 되고 경주가 끝납니다. 
1등부터 배열에 담으면 ["mumu", "kai", "mine", "soe", "poe"]이 됩니다.

"""

"""
각 선수의 초기 위치를 추적하면서 호출되는 선수의 위치를 업데이트 한다.

- 인덱스와 이름을 엮어서 저장하는 방법 생각
- 업데이트는 인덱스 값을 바꿔서 새롭게 저장

"""


def solution(players, callings):
    result = []
    # 등수를 변경해야하기 때문에 인덱스 값을 value 로 둔다.
    index_dict = {player: i for i, player in enumerate(players)}
    init_ranking = list(index_dict)

    for calling in callings:
        # 처음 불린 이름의 인덱스 값
        current_index = index_dict[calling]  # 2
        if current_index > 0:
            # 1 칸 앞에 있는 사람
            ahead_player = init_ranking[current_index - 1]  # another name

            # 위치 변경
            init_ranking[current_index] = ahead_player
            # init_ranking[2] = "another name"
            init_ranking[current_index - 1] = calling
            # init_ranking[1] = "calling name"

            # dict 업데이트
            index_dict[ahead_player] = current_index
            index_dict[calling] = current_index - 1

    result = init_ranking
    return result


players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

print(solution(players, callings))  # ["mumu", "kai", "mine", "soe", "poe"]
