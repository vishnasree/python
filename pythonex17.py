stones=input("enter a stone value: ")
jewels=input("enter a jewels value: ")
count=0
for i in stones:
    for j in jewels:
       if i==j:
           count+=1
print(count)
