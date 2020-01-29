def fivecount(n):
    nl=n.split('1')
    nn=[i for i in nl if len(i)>=5 ]
    r=0
    for i in nn:
        r=r+1+len(i)-5
    print("5 consequtive 0's are",r)

n=input("enter binary string")
fivecount(n)
