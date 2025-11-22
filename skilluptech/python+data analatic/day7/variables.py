# L-E-G-B....
 #Local variable
def food():
    item="Panner"# defined variable in local...
    print("I have ordered",item)
food()

    #------------Enclosing, nested fun
def food():# parent fun
    item="Chapathi"

    def quantity():# child fun
        print("you have ordered",item)
    quantity() 
food()
#Gobal variable

food_app="Swiggy"

def ordernow():
    item="Pizza"
    def quantity():

       
        print("you have ordered "+ item+  " using "+food_app)
    quantity()
ordernow()

print(__file__)#Builtin function
#ctrl+/...




#L..local variable
#E..Enclosing..(nexted function)
#G..Gobale variable
#B.. built in function....1234 4321  int num=1234..

#print(reverse.num)

# its a block of code which is runs once the fun is called...


#age=21
# def funname():
#   print("Age is:",age)


#example of function
Shop_app="Messhoo"#gobal declaration

def dstype():#enclosing
    dress="Short top"
    
    def quan():# local variable
        item=4
        print("ordered",item,dress,"using",Shop_app)
        #f function....
        print(f"ordered {item} {dress} using {Shop_app}")

        print(f"your have ordered {item} {dress} using {Shop_app}")
    quan()
dstype()