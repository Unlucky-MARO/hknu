def countdown(n):
    if n <= 0:
        print("발사")
    else:
        print(n)
        countdown(n-1)

#재귀 함수의 실행이 멈추려면 재귀 호출 과정에서 
#언젠가는 더 이상 자신을 호출하지 않아야 한다. 
#countdown() 함수는 0과 함께 호출될 때 더 이상 
#재귀 호출을 하지 않는다. 이렇게 더 이상 
#재귀 호출이 발생하지 않도록 하는 경우를 
#기저 조건base case이라 한다. 
#즉, countdown() 함수의 기저 조건은 n = 0이다.

def countdown_num(n):
    if n <= 0:
        return 0
    else:
        print(n, '이(가) 양수인 경우!')
        result = countdown_num(n-1) + 1
        return result

#만약 4를 넣으면 countdown_num(3)을 모르고
#그 다음은 countdown_num(2)를 모르고
#countdown_num(1), countdown_num(0)을 모르고
#countdown_num(0)이 return으로 0인게 확정되면
#num(1), num(2), num(3) 다 확정되니 
#최종적으로 num(4) 출력

