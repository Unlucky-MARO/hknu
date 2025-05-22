class Fraction:
    """Fraction 클래스"""

    def __init__(self, top, bottom):
        """생성자 메서드
        top: 분자
        bottom: 분모"""

        self.top = top
        self.bottom = bottom
    
    def __repr__(self):
        return f"{self.top}/{self.bottom}"
    
    def __add__(self, other):
        new_top = self.top * other.bottom + self.bottom * other.top
        new_bottom = self.bottom * other.bottom
        common = gcd(new_top, new_bottom)

        return Fraction(new_top // common, new_bottom // common)

#두 개의 정수 m과 n의 최대공약수를 가장 빠르고 
#효율적으로 계산하는 기법은 유클리드 호제법이다.
#m을 n으로 나눌 수 있으면 n이 최대공약수이다.
#그렇지 않으면 n과 m%n의 최대공약수가 원하는 최대공약수이다.

def gcd(m, n):  # 유클리드 호제법
    while m % n != 0:
        m, n = n, m % n
    return n

print(dir(Fraction))

f35 = Fraction(3, 5)
f12 = Fraction(1, 2)

print(f35)
print(f12)

print(f"피자의 {f35}를 먹었다.")
print(f"피자의 {f12}을 먹었다.")

f14 = Fraction(1, 4)
f12 = Fraction(1, 2)

print(f14 + f12)

print(gcd(6, 14))
print(gcd(8, 20))