import pandas as pd
import time

import os, psutil
process = psutil.Process(os.getpid())

start_memory=process.memory_info().rss  

start=time.time()

df=pd.read_csv('french_dictionary.csv',header=None)

dict={}
for i in range(len(df[0])):
    dict[df[0][i]]=df[1][i]
    

f=open("find_words.txt","r")

count=0

for x in f.readlines():
    if x.strip() in dict:
        count+=1
print("There are",count,"words in the replacement list which are in the dictionary")
print()      
f.close()
f=open("t8.shakespeare.txt","r")


text=f.read()
f.close()

sum=0
Unique_List={}
for i in dict.keys():
    Unique_List[i]=text.count(i[0].upper()+i[1:])+text.count(i.upper())+text.count(i)
    sum+=Unique_List[i]

print('Words to be replaced in the text considering the casing and their corresponding frequencies')
print()
print(Unique_List)
print()
print('Total of',sum,'words have been replaced by french words in the text file')  
print()  


for i in dict.keys():
    text=text.replace(i,dict[i])
    text=text.replace(i.upper(),dict[i].upper())
    text=text.replace(i[0].upper()+i[1:],dict[i][0].upper()+dict[i][1:])
    
        

file1=open("Translated.txt","w")
file1.write(text)
file1.close()

print('Time taken to process',time.time()-start,"seconds")

print("Memory taken to process",process.memory_info().rss-start_memory,"bytes")  


    
            
        



