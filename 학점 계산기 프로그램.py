#학점 계산기 만들기
print("Hakjeom Carculator!") #시작 멘트
print()
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
    num_subject = int(input("과목 개수를 입력하세요.: "))
    if num_subject > 0:
        break
    else:
        print("잘못된 입력입니다.")
input_subject = 0
print()

#4.3 만점에서 과목 개수 따라 학점 입력 받기
if max_point == 4.3:
    hakjeom_list = []
    all_hakjeom_list = "A+ A A- B+ B B- C+ C C- D+ D D- F".split()
    while input_subject in range(num_subject):
        hakjeom = input("학점을 입력하세요(A+, A, A- ... F).: ")
        if hakjeom in all_hakjeom_list:
            hakjeom_list.append(hakjeom)
            input_subject += 1
        else:
            print("잘못된 입력입니다.")
    print()
    #4.3 만점에서 학점 계산하기
    a1 = hakjeom_list.count("A+")*4.3
    a2 = hakjeom_list.count("A")*4.0
    a3 = hakjeom_list.count("A-")*3.7
    b1 = hakjeom_list.count("B+")*3.3
    b2 = hakjeom_list.count("B")*3.0
    b3 = hakjeom_list.count("B-")*2.7
    c1 = hakjeom_list.count('C+')*2.3
    c2 = hakjeom_list.count('C')*2.0
    c3 = hakjeom_list.count('C-')*1.7
    d1 = hakjeom_list.count('D+')*1.3
    d2 = hakjeom_list.count('D')*1.0
    d3 = hakjeom_list.count('D-')*0.7
    f = hakjeom_list.count('F')*0
    sum_hakjeom = a1 + a2 + a3 + b1 + b2 + b3 + c1 + c2 + c3 + d1 + d2 + d3 + f
    final_hakjeom = sum_hakjeom/len(hakjeom_list)
    #만점 4.5점에서 학점 계산하기
else:
    hakjeom_list = []
    all_hakjeom_list = "A+ A B+ B C+ C D+ D F".split()
    while input_subject in range(num_subject):
        hakjeom = input("학점을 입력하세요(A+, A ... F).: ")
        if hakjeom in all_hakjeom_list:
            hakjeom_list.append(hakjeom)
            input_subject += 1
        else:
            print("잘못된 입력입니다.")
    print()
    a1 = hakjeom_list.count("A+")*4.5
    a2 = hakjeom_list.count("A")*4.0
    b1 = hakjeom_list.count("B+")*3.5
    b2 = hakjeom_list.count("B")*3.0
    c1 = hakjeom_list.count('C+')*2.5
    c2 = hakjeom_list.count('C')*2.0
    d1 = hakjeom_list.count('D+')*1.5
    d2 = hakjeom_list.count('D')*1.0
    f = hakjeom_list.count('F')*0
    sum_hakjeom = a1+a2+b1+b2+c1+c2+d1+d2+f
    final_hakjeom = sum_hakjeom/len(hakjeom_list)

print(f"당신의 학점은 {final_hakjeom:.2f} 입니다.")
