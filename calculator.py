import math
print("\t__calculator__")
def sum(a,b):
    return a+b
def sub(a,b):
    return abs(a-b)
def mul(a,b):
    return a*b
def div(a,b):
    q=a/b
    rem=a%b
    print("quotient=",q)
    print("remainder=",rem)
def sqr(a):
    return a*a

while(True):
    print("\n\nchoose the operation you want to perform :")
    
    print("1.addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    print("5. square")
    print("6.exit")
    choice=int(input('>'))
    if(choice==1):
        print("enter the numbers:")
        a=int(input())
        b=int(input())
        print("sum=",sum(a,b))
    elif choice==2:
        print("enter the numbers:")
        a=int(input())
        b=int(input())
        print("difference=",sub(a,b))
    elif choice==3:
        print("enter the numbers:")
        a=int(input())
        b=int(input())
        p=mul(a,b)
        print("product=%s"%p)
    elif choice==4:
        print("enter the numbers:")
        a=int(input( ))
        b=int(input( ))
        div(a,b)
    elif choice==5:
        print("enter the numbers:")
        a=int(input())
        print("square=",sqr(a))
    else:
        print("no option chosen")
        break
        
    
        
        
        
        
        
        
    
    
