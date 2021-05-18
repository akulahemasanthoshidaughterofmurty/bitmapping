n=5
base=int(input())
ans=1
while(n!=0):#5!=0,2!=0,1!=0
    if(n & 1==1): #1,0,1
        ans=ans*base #ans=1*3,ans=3,ans=3*81=243
    base=base*base #base=3*3=9,base=9*9=81,base=81*81
    n=n>>1#2,1,0
print(ans)#ans=243
    
