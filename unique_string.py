import sys

a=input("enter a string")

def unique_characters_or_not(a):
    dict1={}
    for i in a:
        if i in dict1.keys():
            print("not unique")
            sys.exit(0)
        else:
            dict1[i]=1
            
    print("it is unique")
    
unique_characters_or_not(a)
