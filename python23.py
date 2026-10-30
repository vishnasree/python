s=input("enter a string:")
result=" "
for i in s:
      if 'A'<=i<='Z':
          result += chr (ord(i)+32)
      elif 'a'<=i<='z':
          result += chr (ord(i)-32)
print(result)    




          
