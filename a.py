m = int(input())
n = int(input())

  
def gcd_2(m,n):
  while m % n != 0:
    m = n
    n = m % n
    return n


print(gcd_2(m,n))

