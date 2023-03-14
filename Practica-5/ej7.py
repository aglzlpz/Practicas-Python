import string
abc=list(string.ascii_lowercase)

for i in range(len(abc),1,-1):
    if(i%3==0):
        abc.pop(i-1)
        
print(abc)
