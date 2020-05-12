
def matrixmult(m1,m2):
    s=0     
    t=[]   
    m3=[] 
    if len(m2)!=len(m1[0]):
        print ("error")        
    else:
        r1=len(m1) 
        c1=len(m1[0]) 
        r2=c1         
        c2=len(m2[0])  
        for z in range(0,r1):
            for j in range(0,c2):
                for i in range(0,c1):
                   s=s+m1[z][i]*m2[i][j]
                t.append(s)
                s=0
            m3.append(t)
            t=[]           
    return m3
m = [] 
for i in range(3): 
    m.append(list(map(int, input().split())))
y=[[1], [1], [1]]
res1=0
res=1
a=m
k=0
while  res-res1 > 0.0001:
     a=matrixmult(a,m)
     b=matrixmult(a,m)
     t = matrixmult(a,y)
     p = matrixmult(b,y)
     if res!=1:
       res1=res
     res=1/3*(p[0][0]/t[0][0]+p[1][0]/t[1][0]+p[2][0]/t[2][0])
     k=k+1
     

print(res)
print(k)
