text=input("enter a string:")
count=0
for i in text.split():
    if i[0] in "aeiouAEIOU":
      count+=1
print(count)
