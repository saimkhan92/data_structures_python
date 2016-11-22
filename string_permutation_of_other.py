# given two strings, write a program to decide if one is a permutation of other

import sys

a=input("enter first string")
b=input("enter second string")

if len(a)!=len(b):
    print("not a permutation")
    sys.exit()

else:
    dict_a={}
    dict_b={}

    for i in a:
        if i not in dict_a.keys():
            dict_a[i]=1
        else:
            dict_a[i]=dict_a[i]+1

    for i in b:
        if i not in dict_b.keys():
            dict_b[i]=1
        else:
            dict_b[i]=dict_b[i]+1

    if dict_a==dict_b:
        print("it is a permutation")
    else:
        print("it is not a permutation")

    
