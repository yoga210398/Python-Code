#count the num which are divisble by 3,5 range 1,100

count =0
for i in range (1,101):
    if(i%3==0 and i%5==0):
        count=count+1
print(count)
