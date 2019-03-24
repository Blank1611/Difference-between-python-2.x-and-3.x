import random
num = random.randint(1,100)
print(num)
a  = int(input("Enter a number :"))
if a in range(1,100):
    if a in range(num-10,num+11):
        print("WARM :"+str(num))
    else:
        print("COLD :"+str(num))
else:
    
        print("OUT Bounds!!")
