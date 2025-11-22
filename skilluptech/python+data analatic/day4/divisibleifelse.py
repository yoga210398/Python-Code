# Get ip for a num and check whether it is div by both 3 &5 or not. If yes then print, The num is div by 3,5else print not div by 3,5
num = int(input("enter ur ip"))
if(num%5==0 and num%3==0):
    print("yesz, itse num is div by 3,5")
else:
    print("no the given num is not div by 3,5")
