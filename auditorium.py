f=False
ip=input
p=print
a=int(ip())
b=int(ip())
for i in range(b):
    c,d=[int(j) for j in ip().split()]
    if (c-d)>=a:
        p(i+1)
        f=True
if not f:
    p("No free")