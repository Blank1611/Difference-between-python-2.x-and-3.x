def set_calc(x,M):
    for i in range (M):
        #calculate remainder by dividing by 6
        r=(x[i]%6)
        #check for which type the remainder falls under
        if (r==0):
            if  opp_no(x[i]):
                print(x[i]-11, "WS", sep = " ")
            else:
                print(x[i]+1, "WS", sep = " ")
        elif (r==1):
            if opp_no(x[i]):
                print(x[i]+11, "WS", sep = " ")
            else:
                print(x[i]-1, "WS", sep = " ")
        elif (r==4):
            if  opp_no(x[i]):
                print(x[i]+5, "AS", sep = " ")
            else:
                print(x[i]-7, "AS", sep = " ")
        elif (r==3):
            if  opp_no(x[i]):
                print(x[i]+7, "AS", sep = " ")
            else:
                print(x[i]-5, "AS", sep = " ")
        elif (r==2):
            if  opp_no(x[i]):
                print(x[i]+9, "MS", sep = " ")
            else:
                print(x[i]-3, "MS", sep = " ")
        elif (r==5):
            if  opp_no(x[i]):
                print(x[i]+3, "MS", sep = " ")
            else:
                print(x[i]-9, "MS", sep = " ")
#check for odd or even
def opp_no(oe):
    if (oe//6)%2==0:
        return True
    else:
        return False
    
          
    
N = int(input())
b=[]
for i in range (N):
    a=int(input())
    b.append(a)
set_calc(b,N)
