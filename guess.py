import random as ran

print("안녕하세요! 이름이 뭐니?")

name=input()

print(f"{name}, 1에서 20 사이의 숫자를 생각하고 있어요.")
print("맞춰보세요.")

num=ran.randint(1, 20)
count=1

while True:
    num_user=int(input())
    
    if num_user > num :
        print("너무 높은 숫자네요.")
        print("맞춰 보세요.")
        count+=1
        continue
    if num_user < num :
        print("너무 낮은 숫자네요.")
        print("맞춰 보세요.")
        count+=1
        continue
    if num_user == num :
        print(f"잘했어요, {name}! {count}번 만에 제 숫자를 맞혔네요!")
        break
    