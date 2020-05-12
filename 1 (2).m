function sz = lavere(p)
sz=[];
p1=p;
sum=[];
l=size(p);
for j = 1 :l(1)
sum(j)=0;
  for i=1:l(1)
     sum(j)=sum(j)+p(i,i);
  end
  p=p*p1;
end
sz(1)=-sum(1);
k=1;
for i = 2 :l(1)
    k1=k/i;
  v=0;
   for j = 1 : i-1
       v=v+sz(j)*sum(i-j);
   end
   sz(i)=-k1*(sum(i)+v);
end  
sz=[1 sz]; 
end