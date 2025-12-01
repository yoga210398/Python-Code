#reverse number


num=int(input("Enter ur input"))
orgval=num
rev=0
while(num>0):
    rev=rev*10+num%10
    num=num//10
if(orgval==rev):
    print("Its a plainnrome")
else:
    print("its not a plainrome")

 