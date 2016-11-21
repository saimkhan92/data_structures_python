# list files in windows desktop without numbers in filename

import os
import string

file_list=os.listdir("C:\\Users\\Saim\\Desktop\\")
print(file_list)

for file in file_list:
    temp_list=[]
    for character in file:
        if ord(character) in range(48,58):
            temp_list.append("")
        else:
            temp_list.append(character)
    print("".join(temp_list))
            
            
            
