'''#all string in words tht are substring of another word ?
words = input().split()
result = []
for i in words:
    for j in words:
        if i != j and i in j:
            result.append(i)
            break
print(result)'''



'''#sum of n numbers
a=[]
num=int(input("number: "))
for i in range(num):
    a.append(i)
sum=0
for i in a:
    sum=sum+i
print(sum)'''



'''#moving zeros
nums=eval(input())
a=[]
for i in nums:
    if i!=0:
        a.append(i)
for i in nums:
    if i==0:
        a.append(i)
print(a)'''


'''#anther method in moving zreos
nums=[0,1,0]
for i in range(len(nums)):
    if nums [i]==0:
        nums.append(nums[i])
        nums.remove(nums[i])
print(nums)'''


a=[]
string=input(" ").split()
for i in string:
    if i ==1:
      b=set()
    a.add(b) 
print(a)  

        

 
    
 

                         


