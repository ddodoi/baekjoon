arr=[]

for i in range(10):
    arr.append(int(input()))

num=[]
for i in range(10):
    num.append(arr[i]/42)

k=0

for i in range(10):
    if (num[0]!=num[i+1]):
        k+=1

print(k)
'''-------------------------------------------------------
arr=[]
Arr=[]
for i in range(10):
    arr.append(int(input()))
    Arr[i]=(arr[i]/42)

print(Arr)'''

'''arr=[]

for i in range(10):
    arr.append(int(input()))

num=[]
for i in range(10):
    num.append(arr[i]/42)

k=0

for i in range(10):
    if (num[0]!=num[i+1]):
        k+=1

print(k)ㅇㄻㄴ'''
