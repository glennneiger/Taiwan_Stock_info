'''
Created on 2013/4/30

@author: JKZhong
'''
def gcd(m, n):
    return m if n == 0 else gcd(n, m % n)

def lcm(m, n):
    return m * n // gcd(m, n)
    
m = int(input("m:"))
n = int(input("n:"))
print("Gcd: ", gcd(m, n))
print("Lcm: ", lcm(m, n))