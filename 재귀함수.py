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

#콜라츠 추측
#독일 수학자 콜라츠(Collatz -> L.)가 1937년에 아래 알고리즘을
#얼마나 많이 반복하면 최종적으로 숫자 1에 다다를 것인가를 질문했다.
#주어진 숫자가 짝수면 2로 나눈다.
#주어진 숫자가 홀수면 3배한 후 1을 더한다.

#콜라츠 알고리즘을 재귀 함수로 구현할 수 있다.
#기저 조건: num == 1
#num % 2 == 0: 짝수인 경우. 2로 나누기
#기타else: 홀수 인 경우. 3배 더하기 1.

def collatz(num):
    if num == 1:
        print(1)
    elif num%2 == 0:
        print(num, end=' -> ')
        collatz(num//2)
    else:
        print(num, end=' -> ')
        collatz(num*3 + 1)

#재귀 호출 횟수를 반환값으로 지정할 수 있다.
#n == 1: 재귀 호출 없음. 0 반환.
#짝수인 경우: 2로 나눈 값에 대한 재귀 호출 횟수 더하기 1
#홀수인 경우: 세 배 더하기 1에 대한 재귀 호출 횟수 더하기 1

def collatz_count(num):
    if num == 1:
        return 0
    elif num % 2 == 0:
        return collatz_count(num//2) + 1
    else:
        return collatz_count(num*3 + 1) + 1
    
#하노이의 탑
#for, while 반복문을 이용하여 해결하기 어려운 문제를 
#재귀 알고리즘으로 상대적으로 훨씬 간단하게 해결하는 
#예제로 하노이의 탑 문제를 다룬다.

#하노이의 탑Tower of Hanoi 문제는 세 개의 기둥 중에 
#하나의 기둥에 쌓여 있는 다양한 크기의 원판들을 다른 기둥으로 
#옮기는 게임이다. 단, 원판 이동 중에 아래 제한조건들을 
#반드시 지켜야 한다.

#한 번에 한개의 원판만 옮긴다.
#큰 원판이 그보다 작은 원판 위에 위치할 수 없다.

#참고: 일반적으로 원판이 n개 일 때, 2^n - 1번의 이동으로 
#원판을 모두 옮길 수 있다. 참고로 64개의 원판을 옮기는 데 총 
#2^64 -1번 원판을 움직여야 하고, 1초에 하나의 원판을 옮긴다고 
#가정했을 때 5,849억년 정도 걸린다.

#재귀 알고리즘
#n-1 개의 원판을 중간 지점의 위치에 옮긴다.
#가장 큰 원판을 목적지로 옮긴다.
#중간 지점에 위치한 n-1 개의 원판을 목적지로 옮긴다.
#위 재귀 알고리즘의 종료조건은 n=1일 때이며, 
#이때는 하나의 원판을 목적지로 옮기기만 하면 된다.

#height: 원판 개수
#from_pole: 출발 기둥
#with_pole: 중간 지점 기둥
#to_pole: 목적지 기둥

def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)

def move_disk(from_p, to_p):
    print(f"{from_p}에서 {to_p}로 탑 원판 옮기기")

move_tower(4, "A", "B", "C")
