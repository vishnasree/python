n=input("enter a string:")
for i in n:
    if i.isalnum():
      if i.isupper():
        print(i.lower(),end="")
for j in n:
     if j.islower():
        print(j.upper(),end="")
        
 
