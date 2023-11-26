"""
어떠한 스트링을 구분 지어서 양쪽 리스트에 반영
enumerate 를 사용하고 홀짝으로 분리
"""

text = "102#5021#14202#112314#91050#17245#294891#0124004"

splitted_text = text.split("#")
splitted_text_2 = [x for x in text.split("#") if x]


print(splitted_text)
#  ['102', '5021', '14202', '112314', '91050', '17245', '294891', '0124004']
print(splitted_text_2)
#  ['102', '5021', '14202', '112314', '91050', '17245', '294891', '0124004']

odd, even = [], []

for index, value in enumerate(splitted_text, 1):
    if index % 2 == 0:
        even.append(value)
    else:
        odd.append(value)

print("odd index :", odd)
print("Even index :", even)
