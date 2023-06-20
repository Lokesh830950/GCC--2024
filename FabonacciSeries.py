def fib(n):
  a,b=0,1
  l=[]
  while a<=n:
    l.append(a)
    a,b=b,a+b
  print(*l)
n=int(input())
fib(n)
