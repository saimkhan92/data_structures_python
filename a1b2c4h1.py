data=input("please enter string")
temp=data[0]
count=0
final=[]

for i in data:
    if temp==i:
        count=count+1
    else:
        final.append(temp)
        final.append(str(count))
        count=1
        temp=i
        
answer=''.join(final)

if len(answer)>len(data):
    print(data)
else:
    print(answer)
        
