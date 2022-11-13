#피보나치 수열 구현하기

print("Welcome to Fibonacci Sequence!")
print()

#몇 번째 숫자까지 볼 건지 입력받기
while True:
    end_num = input("몇 번째 숫자까지 반복할까요?: ")
    if end_num.isdecimal():
        if int(end_num) > 0:
            end_num = int(end_num)
            break
        else:
            print("잘못된 입력입니다.")
    else:
        print("잘못된 입력입니다.")
print()

#리스트로 피보나치 수열 구현하기
fib_list = [0, 1]
start_num = 1
if end_num in (1, 2):
    result = fib_list[end_num-1]
    print(f"피보나치 수열의 {end_num}번째 숫자는 {result} 입니다.")
else:
    while start_num < end_num - 1:
        result = fib_list[start_num-1] + fib_list[start_num]
        fib_list.append(result)
        start_num += 1
    print(fib_list)
    print(f"피보나치 수열의 {end_num}번째 숫자는 {fib_list[-1]} 입니다.")
