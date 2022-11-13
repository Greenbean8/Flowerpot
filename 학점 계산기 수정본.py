#학점 계산기 만들기#
#시작 멘트
print("Hakjeom Carculator!")
print()

#학점 딕셔너리
point_dict1 = {"A+":4.3, "A":4.0, "A-":3.7,
               "B+":3.3, "B":3.0, "B-":2.7,
               "C+":2.3, "C":2.0, "C-":1.7,
               "D+":1.3, "D":1.0, "D-":0.7,
               "F":0}
point_dict2 = {"A+":4.5, "A":4.0,
               "B+":3.5, "B":3.0,
               "C+":2.5, "C":2.0,
               "D+":1.5, "D":1.0,
               "F":0}

#최고 학점 입력받기
while True:
    max_point = float(input("최고 학점을 입력하세요(4.3/4.5).: "))
    if max_point == 4.3 or max_point == 4.5:
        break
    else:
        print("잘못된 입력입니다.")
print()

#과목 개수 입력 받기
while True:
    num_subject = input("과목 개수를 입력하세요.: ")
    if num_subject.isdecimal():
        num_subject = int(num_subject)
        if num_subject > 0:
            break
        else:
            print("잘못된 입력입니다.")
    else:
        print("잘못된 입력입니다.")
print()

#학점 입력 함수 만들기
def input_grade(num_subject, point_dict):
    trial = 0
    grade_list = []
    while trial < num_subject:
        grade = input("학점을 입력하세요: ")
        while grade.upper() in point_dict:
            grade_list.append(grade.upper())
            trial += 1
            break
        else:
            print("잘못된 입력입니다.")
    return grade_list

#학점 입력 받기
if max_point == 4.3:
    grade_list = input_grade(num_subject, point_dict1)
else:
    grade_list = input_grade(num_subject, point_dict2)
            
#학점 계산 함수 만들기
def point_func(grade_list, point_dict):
    total = 0
    for grade in grade_list:
        total += point_dict[grade]
    final_point = total/len(grade_list)
    return final_point


#학점 계산하기
if max_point == 4.3:
    final_point = point_func(grade_list, point_dict1)
else:
    final_point = point_func(grade_list, point_dict2)

#마지막 출력
print()
print(f"당신의 학점은 {final_point:.2f}점 입니다.")
