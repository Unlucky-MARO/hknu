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

def hour2min(hour):
    min = hour * 60
    return min

def hour2sec(hour):
    min = hour2min(hour)
    sec = 60 * min
    return sec

#함수가 실행되는 동안 발생하는 모든 정보는 
#컴퓨터 메모리 상에서 프레임frame 형식으로 관리된다. 
#프레임은 하나의 함수가 실행되는 동안 발생하는 
#지역 변수의 생성 및 값 할당, 할당된 값 업데이트 
#등을 관리한다. 함수의 실행과 함께 스택stack 메모리
#영역에서 생성된 프레임은 함수의 실행이 종료되면 
#스택에서 사라진다. 하지만 함수의 반환값은 지정된 
#변수에 할당되거나 다른 함수의 인자로 전달된다.

def list_sum(num_list):
    the_sum = 0
    for i in num_list:
        the_sum += i
    return the_sum

#((((0+1)+3)+5)+7)+9

def list_sum2(num_list):
    the_sum = 0
    for i in num_list[::-1]:
        the_sum += i
    return the_sum

#0+(1+(3+(5+(7+9))))

#------------------------

#계승
#음이 아닌 정수 n이 주어졌을 때 1부터 n까지의 곱을 
#n의 계승 또는 팩토리얼factorial이라 하고 
#n!로 표시한다.
# 0! = 1; n! = n(n-1)!
#계승을 계산하는 함수 factorial()을 재귀로 구현할 수 있다.
#기저 조건은 n == 0이고, 1을 반환한다.
#n이 0보다 크면 (n-1)의 계승과 n을 곱합 값을 반환한다.

def factorial(n):
    if n == 0:
        return 1
    else:
        recursion_step = factorial(n-1)
        result = n * recursion_step
        return result

#피보나치 수열
#피보나치 수열Fibonacci sequence은 처음엔 1과 1로 
#시작한 후에 이후의 항목은 이전 두 개의 항목의 합으로 생성된다.
#1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
#피보나치 수열의 두 항목의 관계 점화식은 다음과 같다.
# f0 = 1
# f1 = 1
# fn = fn-1 + fn-2 단, n>=2.

def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(10):
    print(fibonacci(n), end=', ')

print('...')
