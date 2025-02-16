def evenodd(n):
    if n&1 == 1:
        print("odd")
    else:
        print("even")

def mulpow2(x,y):
    return x << y

def divpow2(x,y):
    return x >> y

t = int(input())
while t:
    x,y = map(int,input().split())
    print(mulpow2(x,y))
    print(divpow2(x,y))
    t=t-1