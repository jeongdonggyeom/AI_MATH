# x²+3x-1=0 의 해를 구하라
def f(x):
  return (x**2 - 3*x - 1)

# sinx의 근을 구하라
import math as ms

def sin(x):
  return ms.sin(x)


# 근의 공식
def root_calc(a,b,c):
    D = (b**2) - (4*a*c)
    if D>0:
        r1= (-b + (b**2-4*a*c)**0.5)/(2*a)
        r2 = (-b - (b**2-4*a*c)**0.5)/(2*a)
        print("{} 또는 {} 입니다.".format(r1,r2))
    elif D==0:
        x = -b / 2*a
        print("중근입니다. 해는 {}입니다.". format(x))
    else:
        r1= (-b + (b**2-4*a*c)**0.5)/(2*a)
        r2 = (-b - (b**2-4*a*c)**0.5)/(2*a)
        print("허근입니다. 해는 {} 또는 {} 입니다.".format(r1,r2))



# ------------------------------------ 이분법 ------------------------------------

def bisect(a, b):
  for i in range(1000):
    m = (a+b)/2
    if i == 999:
      return m
    if sin(a)*sin(m) > 0:
      a = m
    elif sin(m)*sin(a) < 0:
      b = m
    else:
      return m
  
# rs1 = bisect(-1, 0);
# rs2 = bisect(3, 4);
# root_calc(1, 3, -1)
# print(rs1)
# print(rs2)
print(bisect(2, 4))

# ------------------------------------ 이분법 ------------------------------------



# ------------------------------------ 뉴턴법 ------------------------------------

def NewTonRaphson(x, h):
  m = (sin(x+h)-sin(x-h))/(2*h)
  return x-sin(x)/m

# for i in range(20):
#   print(NewTonRaphson(-2, 1e-5))

result = 3
for i in range(1000):
  result = NewTonRaphson(result, 1e-5)

print(result)

# ------------------------------------ 뉴턴법 ------------------------------------



# ------------------------------------ 경사하강법 ------------------------------------

def gf(x):
  return(x**4 - 4*x**3 + 3)

def GradientDescent(a, eps, h):
  m = (gf(a+h)-gf(a-h))/(2*h)
  return a-eps*m

rs = 0
for i in range(1000):
  rs = GradientDescent(-1, 1.5675, 1e-5)

print(rs)

# ------------------------------------ 경사하강법 ------------------------------------



# ------------------------------------ 경사상승법 ------------------------------------

def sinf(x):
  return ms.sin(x)/x

def D(f, x):
  h = 1e-5
  return (sinf(x+h)-sinf(x-h))/(2*h)

a1 = 0.2
r1 = 0.1

for i in range(10):
  a1 += D(sinf,a1)*r1

print((a1, sinf(a)))

# ------------------------------------ 경사상승법 ------------------------------------