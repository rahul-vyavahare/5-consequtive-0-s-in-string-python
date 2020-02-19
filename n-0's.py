def fivecount(s,n):
    nl=s.split('1')
    nn=[i for i in nl if len(i)>=n ]
    r=0
    for i in nn:
        r=r+1+len(i)-n
    print(n, "consequtive 0's are",r)

s=input("enter binary string")
n=int(input("how many consequtive 0's you want"))
fivecount(s,n)
