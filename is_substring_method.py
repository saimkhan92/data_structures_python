import sys

master=input("enter master string")
slave=input("enter slave string")

if master==slave:
    print("is a substring")
    sys.exit()
elif len(slave)>len(master):
    print("not a substring")
    sys.exit()
    
def check_slave_equality(i,l):
    #print("inside the function")
    for j in slave:
        if j==master[i]:
            i=i+1
            if i>l:
                print("Not a substring")
                sys.exit()
        else:
            return(False)
    return(True)

for i in range(len(master)):
    i
    3f master[i]==slave[0]:
        result=check_slave_equality(i,len(master))
        if result==True:
            print("It is a substring")
            sys.exit()
        else:
            continue
print("not a substring")
sys.exit()



