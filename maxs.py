def ternmat(s1,s2):
    print ("Введите матрицу:") 
    d=0     
    t=[]   
    s3=[] 
    if len(s2)!=len(s1[0]):
        print ("ошибка")        
    else:
        r1=len(s1) 
        c1=len(s1[0]) 
        r2=c1         
        c2=len(s2[0])  
        for z in range(0,r1):
            for j in range(0,c2):
                for i in range(0,c1):
                   d=d+s1[z][i]*s2[i][j]
                t.append(s)
                s=0
            s3.append(t)
            t=[]           
    return s3
s = [] 
for i in range(3): 
    s.append(list(map(int, input('Введите матрицу построчно: ').split())))
x=[[1], [1], [1]]
tot1=0
tot=1
a=s
k=0
while  tot-tot1 > 0.0001:
     a=ternmat(a,s)
     b=ternmat(a,s)
     t = ternmat(a,x)
     p = ternmat(b,x)
     if res!=1:
       res1=res
     tot=1/3*(p[0][0]/t[0][0]+p[1][0]/t[1][0]+p[2][0]/t[2][0])
     k+=1
     

print(tot)
print(k)
