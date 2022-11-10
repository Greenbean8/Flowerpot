#Korean Lottery Number Draw Program
import random

num_try = 0
lotto_list = []

while num_try < 6:
    num_try += 1
    lotto = random.randint(1,45)
    if lotto not in lotto_list:
        lotto_list.append(str(lotto))

lotto_str = ", ".join(lotto_list)

print(f"Suggestion For Your Lucky Strike: {lotto_str}")
